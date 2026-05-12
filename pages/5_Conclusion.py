"""Page 6 — What Affordability Really Costs."""

from html import escape

import streamlit as st

from src.config import APP_TITLE, CUSTOM_CSS_PATH
from src.data_helpers import (
    DataLoadError,
    housing_prices_stat_endpoints,
    housing_prices_story_series,
    load_commute_story,
    load_national_story,
    national_commute_trend,
    render_data_error,
)
from src.text_blocks import (
    CONCLUSION_BRIDGE,
    CONCLUSION_CLOSING,
    CONCLUSION_IMPLICATION_1_TEXT,
    CONCLUSION_IMPLICATION_1_TITLE,
    CONCLUSION_IMPLICATION_2_TEXT,
    CONCLUSION_IMPLICATION_2_TITLE,
    CONCLUSION_IMPLICATION_3_TEXT,
    CONCLUSION_IMPLICATION_3_TITLE,
    CONCLUSION_IMPLICATIONS_TITLE,
    CONCLUSION_NOT_CLAIM_TEXT,
    CONCLUSION_NOT_CLAIM_TITLE,
    CONCLUSION_OPENING,
    CONCLUSION_OPENING_2,
    CONCLUSION_RECAP_STEP_ACCESS,
    CONCLUSION_RECAP_STEP_COMBINED,
    CONCLUSION_RECAP_STEP_PAYCHECK,
    CONCLUSION_RECAP_STEP_REAL_PRICES,
    CONCLUSION_RECAP_TITLE,
    CONCLUSION_THESIS,
    CONCLUSION_TITLE,
)


def load_css() -> None:
    if CUSTOM_CSS_PATH.exists():
        st.markdown(f"<style>{CUSTOM_CSS_PATH.read_text()}</style>", unsafe_allow_html=True)


def _step_cards_html(v_mult: str, v_ratio: str, v_commute: str) -> str:
    steps = [
        ("housing", "Real prices", CONCLUSION_RECAP_STEP_REAL_PRICES, v_mult),
        ("paycheck", "Paycheck pressure", CONCLUSION_RECAP_STEP_PAYCHECK, v_ratio),
        ("access", "Access burden", CONCLUSION_RECAP_STEP_ACCESS, v_commute),
        ("combined", "Combined lens", CONCLUSION_RECAP_STEP_COMBINED, "Housing + access"),
    ]
    cards = []
    for key, title, body, stat in steps:
        cards.append(
            f'<div class="conclusion-step-card conclusion-step-card--{key}">'
            f'<div class="conclusion-step-card__title">{escape(title)}</div>'
            f'<p class="conclusion-step-card__body">{escape(body)}</p>'
            f'<div class="conclusion-step-card__stat">'
            f'<div class="conclusion-step-card__stat-value">{escape(stat)}</div>'
            f'</div></div>'
        )
    return f'<div class="conclusion-step-grid">{"".join(cards)}</div>'


def _implication_cards_html() -> str:
    items = [
        (CONCLUSION_IMPLICATION_1_TITLE, CONCLUSION_IMPLICATION_1_TEXT),
        (CONCLUSION_IMPLICATION_2_TITLE, CONCLUSION_IMPLICATION_2_TEXT),
        (CONCLUSION_IMPLICATION_3_TITLE, CONCLUSION_IMPLICATION_3_TEXT),
    ]
    cards = []
    for title, body in items:
        cards.append(
            f'<div class="implication-card">'
            f'<div class="implication-card__title">{escape(title)}</div>'
            f'<p class="implication-card__body">{escape(body)}</p>'
            f'</div>'
        )
    return f'<div class="implication-grid">{"".join(cards)}</div>'


st.set_page_config(page_title=f"{CONCLUSION_TITLE} | {APP_TITLE}", layout="wide")
load_css()

st.title(CONCLUSION_TITLE)
st.markdown(f'<p class="paychecks-page-intro story-readable">{escape(CONCLUSION_OPENING)}</p>', unsafe_allow_html=True)
st.markdown(f'<p class="paychecks-page-intro story-readable">{escape(CONCLUSION_OPENING_2)}</p>', unsafe_allow_html=True)

try:
    national = load_national_story()
    commute = national_commute_trend(load_commute_story())
    hp_series = housing_prices_story_series(national)
    _, _, _, _, price_mult = housing_prices_stat_endpoints(hp_series)
except DataLoadError as exc:
    render_data_error(exc)

ratio_2024 = national.loc[national["year"].eq(2024), "home_price_to_real_income_ratio"].dropna()
commute_2024 = commute.loc[commute["year"].eq(2024), "mean_commute_minutes"].dropna()

price_mult_str = f"{price_mult:.1f}x" if price_mult == price_mult and price_mult > 0 else "\u2014"
ratio_str = f"{ratio_2024.iloc[0]:.1f}x" if not ratio_2024.empty else "\u2014"
commute_str = f"{commute_2024.iloc[0]:.1f} min" if not commute_2024.empty else "\u2014"

st.markdown(f'<h3 class="section-heading-md">{escape(CONCLUSION_RECAP_TITLE)}</h3>', unsafe_allow_html=True)
st.markdown(_step_cards_html(price_mult_str, ratio_str, commute_str), unsafe_allow_html=True)

st.markdown(
    f'<div class="thesis-callout"><p>{escape(CONCLUSION_THESIS)}</p></div>',
    unsafe_allow_html=True,
)

st.markdown(
    f'<h3 class="section-kicker section-head-normal">{escape(CONCLUSION_IMPLICATIONS_TITLE)}</h3>',
    unsafe_allow_html=True,
)
st.markdown(_implication_cards_html(), unsafe_allow_html=True)

st.markdown(f'<p class="conclusion-bridge">{escape(CONCLUSION_BRIDGE)}</p>', unsafe_allow_html=True)

st.markdown(
    f'<h3 class="section-kicker section-head-normal">{escape(CONCLUSION_NOT_CLAIM_TITLE)}</h3>',
    unsafe_allow_html=True,
)
st.markdown(f'<p class="conclusion-not-claim caveat-callout">{escape(CONCLUSION_NOT_CLAIM_TEXT)}</p>', unsafe_allow_html=True)
st.markdown(f'<p class="conclusion-closing">{escape(CONCLUSION_CLOSING)}</p>', unsafe_allow_html=True)
