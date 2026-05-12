"""Page 2 — The Sticker Price Story."""

from html import escape

import streamlit as st

from src.config import APP_TITLE, CUSTOM_CSS_PATH
from src.data_helpers import (
    DataLoadError,
    housing_prices_stat_endpoints,
    housing_prices_story_series,
    load_national_story,
    render_data_error,
)
from src.text_blocks import HOUSING_BRIDGE, HOUSING_INTRO, HOUSING_SOURCE_CAPTION, HOUSING_TAKEAWAY_CALLOUT, HOUSING_TITLE
from src.viz_helpers import real_home_price_chart


def load_css() -> None:
    if CUSTOM_CSS_PATH.exists():
        st.markdown(f"<style>{CUSTOM_CSS_PATH.read_text()}</style>", unsafe_allow_html=True)


def _fmt_price_thousands(v: float) -> str:
    return f"${v / 1000:.1f}k"


def _housing_stat_cards_html(y_lo: int, v_lo: float, y_hi: int, v_hi: float, ratio: float) -> str:
    ratio_s = f"{ratio:.1f}x" if ratio == ratio and ratio > 0 else "—"
    cards = [
        (str(y_lo), _fmt_price_thousands(v_lo), "real median home sale price"),
        (str(y_hi), _fmt_price_thousands(v_hi), "real median home sale price"),
        ("Change", ratio_s, "higher in real terms"),
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
    return f'<div class="snapshot-grid page-stat-row">{"".join(parts)}</div>'


st.set_page_config(page_title=f"{HOUSING_TITLE} | {APP_TITLE}", layout="wide")
load_css()

st.title(HOUSING_TITLE)
st.markdown(f'<p class="housing-page-intro story-readable">{escape(HOUSING_INTRO)}</p>', unsafe_allow_html=True)

try:
    national = load_national_story()
    hp = housing_prices_story_series(national)
    y_lo, v_lo, y_hi, v_hi, ratio = housing_prices_stat_endpoints(hp)
except DataLoadError as exc:
    render_data_error(exc)

st.markdown(_housing_stat_cards_html(y_lo, v_lo, y_hi, v_hi, ratio), unsafe_allow_html=True)

st.markdown(
    '<h3 class="chart-title">Real median home sale price, 1963–2024</h3>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="chart-subtitle">Annualized U.S. median sale price, adjusted to 2024 dollars</p>',
    unsafe_allow_html=True,
)
st.plotly_chart(real_home_price_chart(national), use_container_width=True, config={"displayModeBar": False})
st.caption(HOUSING_SOURCE_CAPTION)
st.markdown(f'<p class="story-page-intro story-readable">{escape(HOUSING_BRIDGE)}</p>', unsafe_allow_html=True)
st.markdown(
    f'<div class="takeaway-callout housing-takeaway"><p>{escape(HOUSING_TAKEAWAY_CALLOUT)}</p></div>',
    unsafe_allow_html=True,
)
