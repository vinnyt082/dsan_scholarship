"""Reusable Plotly chart helpers for the Streamlit data story."""

from __future__ import annotations

import numpy as np
import plotly.graph_objects as go

from src.config import COLORS
from src.data_helpers import housing_prices_story_series, paychecks_story_series


def _layout_title_text(main: str, subtitle: str | None = None) -> str:
    if not subtitle:
        return main
    return (
        f"{main}<br><span style='font-size:14px;color:{COLORS['muted']}'>{subtitle}</span>"
    )


def _base_layout(fig: go.Figure, title: str, height: int = 430, subtitle: str | None = None) -> go.Figure:
    fig.update_layout(
        title={
            "text": _layout_title_text(title, subtitle),
            "x": 0,
            "xanchor": "left",
            "font": {"size": 20},
        },
        height=height,
        margin={"l": 20, "r": 24, "t": 72, "b": 40},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(247,244,239,0.42)",
        font={
            "family": "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif",
            "color": COLORS["text"],
            "size": 13,
        },
        hoverlabel={
            "bgcolor": COLORS["paper"],
            "bordercolor": COLORS["border"],
            "font": {"family": "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif", "size": 13, "color": COLORS["text"]},
        },
        showlegend=False,
    )
    fig.update_xaxes(
        showgrid=False,
        zeroline=False,
        linecolor=COLORS["grid"],
        tickfont={"color": COLORS["muted"], "size": 12},
        title_font={"color": COLORS["text"], "size": 13},
    )
    fig.update_yaxes(
        gridcolor=COLORS["grid"],
        gridwidth=1,
        zeroline=False,
        linecolor=COLORS["grid"],
        tickfont={"color": COLORS["muted"], "size": 12},
        title_font={"color": COLORS["text"], "size": 13},
    )
    return fig


def real_home_price_chart(df) -> go.Figure:
    plot_df = housing_prices_story_series(df)
    fig = go.Figure()
    if plot_df.empty:
        _base_layout(fig, "", subtitle=None, height=420)
        return fig

    vmin = float(plot_df["real_median_home_price"].min())
    vmax = float(plot_df["real_median_home_price"].max())
    pad = (vmax - vmin) * 0.08
    lo = max(0.0, vmin - pad)
    hi = vmax + pad
    step = 50_000.0
    tick_vals = np.arange(np.floor(lo / step) * step, np.ceil(hi / step) * step + 1, step)
    tick_text = [f"${int(t / 1000)}k" for t in tick_vals]

    hover = "Year: %{x}<br>Real median home sale price: $%{y:,.0f}<extra></extra>"
    fig.add_trace(
        go.Scatter(
            x=plot_df["year"],
            y=plot_df["real_median_home_price"],
            mode="lines",
            line={"color": COLORS["housing"], "width": 4},
            hovertemplate=hover,
        )
    )

    first = plot_df.iloc[0]
    last = plot_df.iloc[-1]
    lab_lo = f"${first['real_median_home_price'] / 1000:.0f}k"
    lab_hi = f"${last['real_median_home_price'] / 1000:.0f}k"
    fig.add_trace(
        go.Scatter(
            x=[first["year"], last["year"]],
            y=[first["real_median_home_price"], last["real_median_home_price"]],
            mode="markers+text",
            marker={
                "size": 12,
                "color": COLORS["housing"],
                "line": {"color": COLORS["paper"], "width": 1.5},
            },
            text=[lab_lo, lab_hi],
            textposition=["top center", "top right"],
            textfont={"size": 11, "color": COLORS["text"]},
            hovertemplate=hover,
        )
    )

    _base_layout(fig, "", subtitle=None, height=500)
    fig.update_layout(margin={"l": 20, "r": 24, "t": 42, "b": 48})
    fig.update_yaxes(
        title="Median home sale price, 2024 dollars",
        title_font={"color": COLORS["text"]},
        tickfont={"color": COLORS["muted"]},
        tickmode="array",
        tickvals=tick_vals,
        ticktext=tick_text,
    )
    fig.update_xaxes(title="", tickfont={"color": COLORS["muted"]})
    return fig


def home_price_income_ratio_chart(df) -> go.Figure:
    plot_df = paychecks_story_series(df)
    fig = go.Figure()
    if plot_df.empty:
        _base_layout(fig, "", subtitle=None, height=460)
        return fig

    ymin = float(plot_df["home_price_to_real_income_ratio"].min())
    ymax = float(plot_df["home_price_to_real_income_ratio"].max())
    pad = (ymax - ymin) * 0.12 if ymax > ymin else 0.3
    lo = max(0.0, ymin - pad)
    hi = ymax + pad
    step = 0.5
    tick_vals = np.arange(np.floor(lo / step) * step, np.ceil(hi / step) * step + 1e-9, step)
    tick_text = [f"{t:.1f}x" for t in tick_vals]

    fig.add_trace(
        go.Scatter(
            x=plot_df["year"],
            y=plot_df["home_price_to_real_income_ratio"],
            mode="lines",
            line={"color": COLORS["housing"], "width": 4},
            hovertemplate="Year: %{x}<br>Home price-to-income ratio: %{y:.1f}x<extra></extra>",
        )
    )
    first = plot_df.iloc[0]
    last = plot_df.iloc[-1]
    fig.add_trace(
        go.Scatter(
            x=[first["year"], last["year"]],
            y=[first["home_price_to_real_income_ratio"], last["home_price_to_real_income_ratio"]],
            mode="markers+text",
            marker={
                "size": 11,
                "color": COLORS["housing"],
                "line": {"color": COLORS["paper"], "width": 1.5},
            },
            text=[f'{first["home_price_to_real_income_ratio"]:.1f}x', f'{last["home_price_to_real_income_ratio"]:.1f}x'],
            textposition=["top center", "top right"],
            textfont={"size": 11, "color": COLORS["text"]},
            hovertemplate="Year: %{x}<br>Home price-to-income ratio: %{y:.1f}x<extra></extra>",
        )
    )
    _base_layout(fig, "", subtitle=None, height=500)
    fig.update_layout(margin={"l": 20, "r": 24, "t": 28, "b": 48})
    fig.update_yaxes(
        title="Home price-to-income ratio (national)",
        title_font={"color": COLORS["text"]},
        tickfont={"color": COLORS["muted"]},
        tickmode="array",
        tickvals=tick_vals,
        ticktext=tick_text,
    )
    fig.update_xaxes(title="", tickfont={"color": COLORS["muted"]})
    return fig


def mortgage_rate_chart(df) -> go.Figure:
    plot_df = df[["year", "mortgage_rate_annual_avg"]].dropna()
    plot_df = plot_df[plot_df["year"].le(2024)]
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=plot_df["year"],
            y=plot_df["mortgage_rate_annual_avg"],
            mode="lines",
            line={"color": COLORS["income"], "width": 2.4},
            hovertemplate="Year: %{x}<br>Rate: %{y:.2f}%<extra></extra>",
        )
    )
    _base_layout(fig, "", subtitle=None, height=330)
    fig.update_layout(margin={"l": 20, "r": 24, "t": 24, "b": 44})
    fig.update_yaxes(
        title="Percent",
        ticksuffix="%",
        title_font={"color": COLORS["text"]},
        tickfont={"color": COLORS["muted"]},
    )
    fig.update_xaxes(title="", tickfont={"color": COLORS["muted"]})
    return fig


def national_commute_chart(df) -> go.Figure:
    plot_df = df[["year", "mean_commute_minutes"]].dropna().sort_values("year")
    fig = go.Figure()
    seg_1 = plot_df[plot_df["year"].le(2019)]
    seg_2 = plot_df[plot_df["year"].ge(2021)]
    hover = "Year: %{x}<br>Mean one-way commute: %{y:.1f} min<extra></extra>"
    for seg in [seg_1, seg_2]:
        if seg.empty:
            continue
        fig.add_trace(
            go.Scatter(
                x=seg["year"],
                y=seg["mean_commute_minutes"],
                mode="lines+markers",
                marker={"size": 7, "color": COLORS["commute"]},
                line={"color": COLORS["commute"], "width": 3.2},
                hovertemplate=hover,
                showlegend=False,
            )
        )
    for yr in [2005, 2019, 2024]:
        row = plot_df.loc[plot_df["year"].eq(yr)]
        if row.empty:
            continue
        val = float(row["mean_commute_minutes"].iloc[0])
        fig.add_trace(
            go.Scatter(
                x=[yr],
                y=[val],
                mode="text",
                text=[f"{val:.1f} min"],
                textposition="top center",
                textfont={"size": 11, "color": COLORS["text"]},
                hovertemplate=hover,
                showlegend=False,
            )
        )
    _base_layout(fig, "", subtitle=None, height=470)
    fig.update_layout(margin={"l": 20, "r": 24, "t": 28, "b": 48})
    fig.update_yaxes(
        title="Mean one-way commute time, minutes",
        title_font={"color": COLORS["text"]},
        tickfont={"color": COLORS["muted"]},
    )
    fig.update_xaxes(title="", tickfont={"color": COLORS["muted"]})
    return fig


def commute_rank_chart(df) -> go.Figure:
    plot_df = df.sort_values("mean_commute_minutes", ascending=False)
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=plot_df["mean_commute_minutes"],
            y=plot_df["case_geography"],
            orientation="h",
            marker={"color": COLORS["commute"]},
            text=[f"{v:.1f} min" for v in plot_df["mean_commute_minutes"]],
            textposition="outside",
            hovertemplate="Geography: %{y}<br>Mean one-way commute: %{x:.1f} min<extra></extra>",
        )
    )
    _base_layout(fig, "", subtitle=None, height=560)
    fig.update_layout(margin={"l": 20, "r": 72, "t": 28, "b": 44})
    fig.update_traces(cliponaxis=False)
    fig.update_xaxes(
        title="Mean one-way commute time, minutes",
        title_font={"color": COLORS["text"]},
        tickfont={"color": COLORS["muted"]},
    )
    fig.update_yaxes(
        title="",
        tickfont={"color": COLORS["muted"]},
        categoryorder="array",
        categoryarray=plot_df["case_geography"],
        autorange="reversed",
    )
    return fig


QUADRANT_FILLS = {
    "ll": "rgba(144,169,144,0.15)",   # lower-left: sage
    "lr": "rgba(194,163,130,0.16)",   # lower-right: sand
    "ul": "rgba(47,122,125,0.14)",    # upper-left: teal
    "ur": "rgba(154,63,47,0.14)",     # upper-right: rose
}

QUADRANT_ACCENT = {
    "ll": "#90a990",
    "lr": "#c8a882",
    "ul": "#7bb8ba",
    "ur": "#c07060",
}


def housing_access_scatter(df) -> go.Figure:
    x_median = df["home_value_to_income_ratio"].median()
    y_median = df["mean_commute_minutes"].median()

    x_vals = df["home_value_to_income_ratio"]
    y_vals = df["mean_commute_minutes"]
    x_pad = (x_vals.max() - x_vals.min()) * 0.15
    y_pad = (y_vals.max() - y_vals.min()) * 0.15
    x_lo = float(x_vals.min() - x_pad)
    x_hi = float(x_vals.max() + x_pad)
    y_lo = float(y_vals.min() - y_pad)
    y_hi = float(y_vals.max() + y_pad)

    fig = go.Figure()

    quadrants = [
        (x_lo, x_median, y_lo, y_median, QUADRANT_FILLS["ll"]),
        (x_median, x_hi, y_lo, y_median, QUADRANT_FILLS["lr"]),
        (x_lo, x_median, y_median, y_hi, QUADRANT_FILLS["ul"]),
        (x_median, x_hi, y_median, y_hi, QUADRANT_FILLS["ur"]),
    ]
    for x0, x1, y0, y1, fill in quadrants:
        fig.add_shape(
            type="rect", x0=x0, x1=x1, y0=y0, y1=y1,
            fillcolor=fill, line_width=0, layer="below",
        )

    fig.add_trace(
        go.Scatter(
            x=df["home_value_to_income_ratio"],
            y=df["mean_commute_minutes"],
            mode="markers+text",
            text=df["case_geography"],
            textposition="top center",
            textfont={"size": 10, "color": COLORS["text"]},
            marker={
                "size": 12,
                "color": COLORS["housing"],
                "line": {"color": COLORS["paper"], "width": 1.5},
            },
            customdata=df[["housing_access_quadrant"]],
            hovertemplate=(
                "Geography: %{text}<br>"
                "Home value-to-income ratio: %{x:.1f}x<br>"
                "Mean one-way commute: %{y:.1f} min<br>"
                "Profile: %{customdata[0]}<extra></extra>"
            ),
        )
    )
    fig.add_vline(
        x=x_median,
        line={"color": COLORS["reference"], "dash": "dash", "width": 1},
        annotation_text="Median housing pressure",
        annotation_position="top left",
        annotation_font_size=11,
        annotation_font_color=COLORS["muted"],
    )
    fig.add_hline(
        y=y_median,
        line={"color": COLORS["reference"], "dash": "dash", "width": 1},
        annotation_text="Median one-way commute",
        annotation_position="bottom right",
        annotation_font_size=11,
        annotation_font_color=COLORS["muted"],
    )
    _base_layout(fig, "", subtitle=None, height=590)
    fig.update_layout(margin={"l": 20, "r": 40, "t": 36, "b": 54})
    fig.update_xaxes(
        title="Home value-to-income ratio",
        ticksuffix="x",
        tickfont={"color": COLORS["muted"]},
        title_font={"color": COLORS["text"]},
        range=[x_lo, x_hi],
    )
    fig.update_yaxes(
        title="Mean one-way commute time, minutes",
        tickfont={"color": COLORS["muted"]},
        title_font={"color": COLORS["text"]},
        range=[y_lo, y_hi],
    )
    return fig
