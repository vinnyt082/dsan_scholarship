"""Page 3 — Prices Versus Paychecks."""

from html import escape

import streamlit as st

from src.config import APP_TITLE, CUSTOM_CSS_PATH
from src.data_helpers import (
    DataLoadError,
    load_national_story,
    paychecks_stat_endpoints,
    paychecks_story_series,
    render_data_error,
)
from src.text_blocks import (
    MORTGAGE_CONTEXT_INTRO,
    MORTGAGE_CONTEXT_NOTE,
    MORTGAGE_EXPANDER_LABEL,
    PAYCHECKS_BRIDGE,
    PAYCHECKS_INTERPRETATION_NOTE,
    PAYCHECKS_INTRO,
    PAYCHECKS_SOURCE_CAPTION,
    PAYCHECKS_TAKEAWAY_CALLOUT,
    PAYCHECKS_TITLE,
)
from src.viz_helpers import home_price_income_ratio_chart, mortgage_rate_chart


def load_css() -> None:
    if CUSTOM_CSS_PATH.exists():
        st.markdown(f"<style>{CUSTOM_CSS_PATH.read_text()}</style>", unsafe_allow_html=True)


st.set_page_config(page_title=f"{PAYCHECKS_TITLE} | {APP_TITLE}", layout="wide")
load_css()

st.title(PAYCHECKS_TITLE)
st.markdown(f'<p class="paychecks-page-intro story-readable">{escape(PAYCHECKS_INTRO)}</p>', unsafe_allow_html=True)
st.markdown(
    f'<p class="paychecks-interpretation-note method-note story-readable">{escape(PAYCHECKS_INTERPRETATION_NOTE)}</p>',
    unsafe_allow_html=True,
)

try:
    national = load_national_story()
    ratio_df = paychecks_story_series(national)
    y_lo, v_lo, y_hi, v_hi, pct_change = paychecks_stat_endpoints(ratio_df)
except DataLoadError as exc:
    render_data_error(exc)

cards = [
    (str(y_lo), f"{v_lo:.1f}x", "home price-to-income ratio"),
    (str(y_hi), f"{v_hi:.1f}x", "home price-to-income ratio"),
    ("Change", f"{pct_change:+.0f}%", "stronger price-to-income pressure"),
]
parts = []
for title, value, cap in cards:
    parts.append(
        f"""<div class="snapshot-card story-card">
        <div class="snapshot-card__label">{escape(title)}</div>
        <div class="snapshot-card__value">{escape(value)}</div>
        <div class="snapshot-card__caption">{escape(cap)}</div>
        </div>"""
    )
st.markdown(f'<div class="snapshot-grid page-stat-row">{"".join(parts)}</div>', unsafe_allow_html=True)

st.markdown(
    '<h3 class="chart-title">Home price-to-income ratio, 1984–2024</h3>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="chart-subtitle">Median home sale price divided by real median household income</p>',
    unsafe_allow_html=True,
)
st.plotly_chart(home_price_income_ratio_chart(national), use_container_width=True, config={"displayModeBar": False})
st.caption(PAYCHECKS_SOURCE_CAPTION)
st.markdown(f'<p class="story-page-intro story-readable">{escape(PAYCHECKS_BRIDGE)}</p>', unsafe_allow_html=True)
st.markdown(
    f'<div class="takeaway-callout housing-takeaway"><p>{escape(PAYCHECKS_TAKEAWAY_CALLOUT)}</p></div>',
    unsafe_allow_html=True,
)

with st.expander(MORTGAGE_EXPANDER_LABEL, expanded=False):
    st.markdown(MORTGAGE_CONTEXT_INTRO)
    st.markdown(
        '<h3 class="chart-title chart-title--secondary">30-year fixed mortgage rate, 1971–2024</h3>',
        unsafe_allow_html=True,
    )
    st.markdown('<p class="chart-subtitle chart-subtitle--secondary">Annual average</p>', unsafe_allow_html=True)
    st.plotly_chart(mortgage_rate_chart(national), use_container_width=True, config={"displayModeBar": False})
    st.caption(MORTGAGE_CONTEXT_NOTE)
