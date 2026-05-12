"""Data loading helpers for the Streamlit prototype."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st

from src.config import (
    COMMUTE_STORY_PATH,
    FINAL_COMMUTE_YEAR,
    FINAL_NATIONAL_YEAR,
    HOUSING_ACCESS_PATH,
    NATIONAL_STORY_PATH,
    OMITTED_COMMUTE_YEAR,
)

HOUSING_PRICE_STORY_FIRST_YEAR = 1963
HOUSING_PRICE_STORY_LAST_YEAR = 2024
PAYCHECKS_STORY_FIRST_YEAR = 1984
PAYCHECKS_STORY_LAST_YEAR = 2024

_QUADRANT_LABELS = {
    "higher housing pressure / higher commute burden": "Higher housing pressure / higher commute burden",
    "lower housing pressure / higher commute burden": "Lower housing pressure / higher commute burden",
    "higher housing pressure / lower commute burden": "Higher housing pressure / lower commute burden",
    "lower housing pressure / lower commute burden": "Lower housing pressure / lower commute burden",
}


class DataLoadError(RuntimeError):
    """Raised when an expected processed data file is missing or invalid."""


def _read_csv(path: Path, required_columns: list[str]) -> pd.DataFrame:
    if not path.exists():
        raise DataLoadError(
            f"Missing required processed file: {path}. "
            "Run the notebook data pipeline before launching the app."
        )

    df = pd.read_csv(path)
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise DataLoadError(f"{path.name} is missing required columns: {missing}")

    return df


@st.cache_data(show_spinner=False)
def load_national_story(max_year: int = FINAL_NATIONAL_YEAR) -> pd.DataFrame:
    """Load national story data and cap final charts at the approved endpoint."""

    df = _read_csv(
        NATIONAL_STORY_PATH,
        [
            "year",
            "real_median_home_price",
            "real_median_household_income",
            "home_price_to_real_income_ratio",
            "mortgage_rate_annual_avg",
        ],
    )
    df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")
    return df[df["year"].le(max_year)].copy()


def housing_prices_story_series(df: pd.DataFrame) -> pd.DataFrame:
    """Filter national data for the housing-prices page: 1963–2024, non-missing real median price."""

    out = df[["year", "real_median_home_price"]].copy()
    out = out.dropna(subset=["real_median_home_price"])
    out = out[out["year"].ge(HOUSING_PRICE_STORY_FIRST_YEAR) & out["year"].le(HOUSING_PRICE_STORY_LAST_YEAR)]
    return out.sort_values("year").reset_index(drop=True)


def housing_prices_stat_endpoints(plot_df: pd.DataFrame) -> tuple[int, float, int, float, float]:
    """First and last years/values for stat cards (prefer 1963 and 2024; else first/last row). Returns ratio hi/lo."""

    if plot_df.empty:
        raise DataLoadError("No housing price rows after filtering.")

    df = plot_df.sort_values("year").reset_index(drop=True)
    lo_row = df.loc[df["year"].eq(HOUSING_PRICE_STORY_FIRST_YEAR)]
    if not lo_row.empty:
        row_lo = lo_row.iloc[0]
    else:
        row_lo = df.iloc[0]
    hi_row = df.loc[df["year"].eq(HOUSING_PRICE_STORY_LAST_YEAR)]
    if not hi_row.empty:
        row_hi = hi_row.iloc[0]
    else:
        row_hi = df.iloc[-1]

    y_lo = int(row_lo["year"])
    v_lo = float(row_lo["real_median_home_price"])
    y_hi = int(row_hi["year"])
    v_hi = float(row_hi["real_median_home_price"])
    ratio = v_hi / v_lo if v_lo else float("nan")
    return y_lo, v_lo, y_hi, v_hi, ratio


def paychecks_story_series(df: pd.DataFrame) -> pd.DataFrame:
    """Filter national data for paychecks page: 1984–2024, non-missing ratio."""

    out = df[["year", "home_price_to_real_income_ratio"]].copy()
    out = out.dropna(subset=["home_price_to_real_income_ratio"])
    out = out[
        out["year"].ge(PAYCHECKS_STORY_FIRST_YEAR)
        & out["year"].le(PAYCHECKS_STORY_LAST_YEAR)
    ]
    return out.sort_values("year").reset_index(drop=True)


def paychecks_stat_endpoints(plot_df: pd.DataFrame) -> tuple[int, float, int, float, float]:
    """First and last years/values for paychecks stat cards; final value is percent change."""

    if plot_df.empty:
        raise DataLoadError("No paychecks ratio rows after filtering.")

    df = plot_df.sort_values("year").reset_index(drop=True)
    lo_row = df.loc[df["year"].eq(PAYCHECKS_STORY_FIRST_YEAR)]
    row_lo = lo_row.iloc[0] if not lo_row.empty else df.iloc[0]
    hi_row = df.loc[df["year"].eq(PAYCHECKS_STORY_LAST_YEAR)]
    row_hi = hi_row.iloc[0] if not hi_row.empty else df.iloc[-1]

    y_lo = int(row_lo["year"])
    v_lo = float(row_lo["home_price_to_real_income_ratio"])
    y_hi = int(row_hi["year"])
    v_hi = float(row_hi["home_price_to_real_income_ratio"])
    pct_change = ((v_hi / v_lo) - 1.0) * 100.0 if v_lo else float("nan")
    return y_lo, v_lo, y_hi, v_hi, pct_change


@st.cache_data(show_spinner=False)
def load_commute_story() -> pd.DataFrame:
    """Load ACS commute data for national trend and selected county proxies."""

    df = _read_csv(
        COMMUTE_STORY_PATH,
        ["geo_level", "geography", "year", "B08012_001E", "mean_commute_minutes"],
    )
    df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")
    return df.copy()


@st.cache_data(show_spinner=False)
def load_housing_access_snapshot() -> pd.DataFrame:
    """Load the approved selected county proxy housing + access snapshot."""

    df = _read_csv(
        HOUSING_ACCESS_PATH,
        [
            "year",
            "case_geography",
            "NAME",
            "mean_commute_minutes",
            "median_home_value",
            "median_household_income",
            "home_value_to_income_ratio",
            "housing_access_quadrant",
        ],
    )
    df["display_geography"] = (
        df["case_geography"].str.replace(" area proxy", "", regex=False)
        .str.replace(" proxy", "", regex=False)
    )
    if "housing_access_quadrant" in df.columns:
        def _normalize_quadrant(val):
            if pd.isna(val):
                return val
            key = str(val).strip().lower()
            return _QUADRANT_LABELS.get(key, str(val).strip())

        df["housing_access_quadrant"] = df["housing_access_quadrant"].map(_normalize_quadrant)
    return df.copy()


def national_commute_trend(commute: pd.DataFrame) -> pd.DataFrame:
    """Return national ACS commute trend: national rows only, year <= 2024, 2020 omitted."""

    trend = commute[commute["geo_level"].eq("national")].copy()
    trend = trend[trend["year"].ne(OMITTED_COMMUTE_YEAR)]
    trend = trend[trend["year"].le(FINAL_COMMUTE_YEAR)]
    return trend.sort_values("year")


def selected_county_commute_rank(snapshot: pd.DataFrame) -> pd.DataFrame:
    """Return selected county proxy commute data ranked from highest to lowest."""

    return snapshot.sort_values("mean_commute_minutes", ascending=False).copy()


def commute_summary_points(national_trend: pd.DataFrame) -> tuple[tuple[int, float], tuple[int, float], tuple[int, float]]:
    """Return summary points for 2005, pre-2020 max, and latest (<=2024) with graceful fallback."""

    if national_trend.empty:
        raise DataLoadError("No national commute rows after filtering.")

    trend = national_trend.sort_values("year").dropna(subset=["mean_commute_minutes"]).copy()
    if trend.empty:
        raise DataLoadError("National commute rows are missing mean_commute_minutes.")

    row_2005 = trend.loc[trend["year"].eq(2005)]
    first_row = row_2005.iloc[0] if not row_2005.empty else trend.iloc[0]

    pre_2020 = trend[trend["year"].lt(2020)]
    if pre_2020.empty:
        pre_row = trend.iloc[trend["mean_commute_minutes"].idxmax()]
    else:
        pre_row = pre_2020.loc[pre_2020["mean_commute_minutes"].idxmax()]

    latest_row = trend.iloc[-1]
    return (
        (int(first_row["year"]), float(first_row["mean_commute_minutes"])),
        (int(pre_row["year"]), float(pre_row["mean_commute_minutes"])),
        (int(latest_row["year"]), float(latest_row["mean_commute_minutes"])),
    )


def render_data_error(error: Exception) -> None:
    """Show a concise Streamlit error for missing or invalid processed data."""

    st.error(str(error))
    st.stop()

