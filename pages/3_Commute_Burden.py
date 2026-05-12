"""Page 4 — Access Has a Time Cost."""

from html import escape

import streamlit as st

from src.config import APP_TITLE, CUSTOM_CSS_PATH
from src.data_helpers import (
    commute_summary_points,
    DataLoadError,
    load_commute_story,
    load_housing_access_snapshot,
    national_commute_trend,
    render_data_error,
    selected_county_commute_rank,
)
from src.text_blocks import (
    COMMUTE_DATA_NOTE,
    COMMUTE_INTRO_1,
    COMMUTE_INTRO_2,
    COMMUTE_NATIONAL_BRIDGE,
    COMMUTE_NATIONAL_CAPTION,
    COMMUTE_PLACE_HEADING,
    COMMUTE_PLACE_INTRO,
    COMMUTE_POST2020_NOTE,
    COMMUTE_RANK_BRIDGE,
    COMMUTE_RANK_CAPTION,
    COMMUTE_TRANSITION,
    COMMUTE_TITLE,
)
from src.viz_helpers import commute_rank_chart, national_commute_chart


def load_css() -> None:
    if CUSTOM_CSS_PATH.exists():
        st.markdown(f"<style>{CUSTOM_CSS_PATH.read_text()}</style>", unsafe_allow_html=True)


st.set_page_config(page_title=f"{COMMUTE_TITLE} | {APP_TITLE}", layout="wide")
load_css()

st.title(COMMUTE_TITLE)
st.markdown(f'<p class="paychecks-page-intro story-readable">{escape(COMMUTE_INTRO_1)}</p>', unsafe_allow_html=True)
st.markdown(f'<p class="paychecks-page-intro story-readable">{escape(COMMUTE_INTRO_2)}</p>', unsafe_allow_html=True)
st.markdown(f'<p class="data-note">{escape(COMMUTE_DATA_NOTE)}</p>', unsafe_allow_html=True)

try:
    commute = load_commute_story()
    snapshot = load_housing_access_snapshot()
except DataLoadError as exc:
    render_data_error(exc)

trend = national_commute_trend(commute)
(year_a, val_a), (year_b, val_b), (year_c, val_c) = commute_summary_points(trend)

cards = [
    (str(year_a), f"{val_a:.1f} min", "national mean one-way commute"),
    (str(year_b), f"{val_b:.1f} min", "pre-2020 peak in this series"),
    (str(year_c), f"{val_c:.1f} min", "latest national reading"),
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

st.markdown('<h3 class="chart-title">National mean one-way commute time, 2005–2024</h3>', unsafe_allow_html=True)
st.markdown('<p class="chart-subtitle">ACS 1-year, United States; 2020 omitted</p>', unsafe_allow_html=True)
st.plotly_chart(national_commute_chart(trend), use_container_width=True, config={"displayModeBar": False})
st.caption(COMMUTE_NATIONAL_CAPTION)
st.markdown(f'<p class="method-note">{escape(COMMUTE_POST2020_NOTE)}</p>', unsafe_allow_html=True)
st.markdown(f'<p class="story-page-intro story-readable">{escape(COMMUTE_NATIONAL_BRIDGE)}</p>', unsafe_allow_html=True)

st.markdown(f'<h3 class="section-kicker section-head-normal">{escape(COMMUTE_PLACE_HEADING)}</h3>', unsafe_allow_html=True)
st.markdown(f'<p class="paychecks-page-intro story-readable">{escape(COMMUTE_PLACE_INTRO)}</p>', unsafe_allow_html=True)
st.markdown(
    '<h3 class="chart-title">Selected county proxies, ranked by commute time</h3>',
    unsafe_allow_html=True,
)
st.markdown('<p class="chart-subtitle">2023 ACS 5-year estimates</p>', unsafe_allow_html=True)
st.plotly_chart(commute_rank_chart(selected_county_commute_rank(snapshot)), use_container_width=True, config={"displayModeBar": False})
st.caption(COMMUTE_RANK_CAPTION)
st.markdown(f'<p class="story-page-intro story-readable">{escape(COMMUTE_RANK_BRIDGE)}</p>', unsafe_allow_html=True)
st.markdown(
    f'<div class="takeaway-callout housing-takeaway"><p>{escape(COMMUTE_TRANSITION)}</p></div>',
    unsafe_allow_html=True,
)
