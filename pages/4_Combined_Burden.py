"""Page 5 — The Combined Burden."""

from html import escape

import streamlit as st

from src.config import APP_TITLE, CUSTOM_CSS_PATH
from src.data_helpers import DataLoadError, load_housing_access_snapshot, render_data_error
from src.text_blocks import (
    ACCESS_BRIDGE,
    ACCESS_CHART_SUBTITLE,
    ACCESS_CHART_TITLE,
    ACCESS_COMBINED_BRIDGE,
    ACCESS_FUTURE_WORK,
    ACCESS_FUTURE_WORK_TITLE,
    ACCESS_GUIDE_LABELS,
    ACCESS_HOW_TO_READ,
    ACCESS_INTRO,
    ACCESS_METRIC_DISTINCTION_NOTE,
    ACCESS_SOURCE_CAPTION,
    ACCESS_STANDS_OUT_TITLE,
    ACCESS_TAKEAWAY,
    ACCESS_TITLE,
    COUNTY_PROXY_NOTE,
)
from src.viz_helpers import housing_access_scatter


def load_css() -> None:
    if CUSTOM_CSS_PATH.exists():
        st.markdown(f"<style>{CUSTOM_CSS_PATH.read_text()}</style>", unsafe_allow_html=True)


_GUIDE_QUADRANT_KEYS = ["ll", "lr", "ul", "ur"]


def _profile_legend_html(labels: list[str]) -> str:
    items = []
    for key, label in zip(_GUIDE_QUADRANT_KEYS, labels):
        items.append(
            f'<li class="quadrant-guide__item">'
            f'<span class="q-chip q-chip--{key}"></span>{escape(label)}'
            f'</li>'
        )
    return (
        '<div class="quadrant-guide">'
        '<div class="quadrant-guide__title">Affordability profiles</div>'
        f'<ul class="quadrant-guide__list">{"".join(items)}</ul>'
        '</div>'
    )


st.set_page_config(page_title=f"{ACCESS_TITLE} | {APP_TITLE}", layout="wide")
load_css()

st.title(ACCESS_TITLE)
st.markdown(f'<p class="paychecks-page-intro story-readable">{escape(ACCESS_INTRO)}</p>', unsafe_allow_html=True)
st.markdown(f'<p class="method-note story-readable">{escape(ACCESS_HOW_TO_READ)}</p>', unsafe_allow_html=True)
st.markdown(f'<p class="data-note story-readable">{escape(ACCESS_METRIC_DISTINCTION_NOTE)}</p>', unsafe_allow_html=True)
st.markdown(_profile_legend_html(ACCESS_GUIDE_LABELS), unsafe_allow_html=True)

try:
    snapshot = load_housing_access_snapshot()
except DataLoadError as exc:
    render_data_error(exc)

st.markdown(f'<h3 class="chart-title">{escape(ACCESS_CHART_TITLE)}</h3>', unsafe_allow_html=True)
st.markdown(f'<p class="chart-subtitle">{escape(ACCESS_CHART_SUBTITLE)}</p>', unsafe_allow_html=True)
st.plotly_chart(housing_access_scatter(snapshot), use_container_width=True, config={"displayModeBar": False})
st.caption(ACCESS_SOURCE_CAPTION)
st.caption(COUNTY_PROXY_NOTE)

# ── What stands out ──
x_med = snapshot["home_value_to_income_ratio"].median()
y_med = snapshot["mean_commute_minutes"].median()

upper_right = snapshot[
    (snapshot["home_value_to_income_ratio"] >= x_med)
    & (snapshot["mean_commute_minutes"] >= y_med)
]["case_geography"].tolist()
upper_right_names = ", ".join(upper_right[:3]) if upper_right else "Several selected proxies"

chicago_row = snapshot.loc[snapshot["case_geography"].str.contains("Chicago", case=False, na=False)]
if not chicago_row.empty:
    c = chicago_row.iloc[0]
    chicago_line = (
        f"{c['case_geography']} has the highest mean one-way commute in this snapshot "
        f"({float(c['mean_commute_minutes']):.1f} min), even though its home value-to-income ratio "
        f"({float(c['home_value_to_income_ratio']):.1f}x) sits below the group median. That contrast "
        "shows why commute burden adds information beyond housing pressure alone."
    )
else:
    chicago_line = (
        "Mean one-way commute time varies across selected county proxies and adds information "
        "beyond housing pressure alone."
    )

denver_row = snapshot.loc[snapshot["case_geography"].str.contains("Denver", case=False, na=False)]
if not denver_row.empty:
    d = denver_row.iloc[0]
    denver_line = (
        f"{d['case_geography']} shows a different split: housing pressure is relatively high "
        f"({float(d['home_value_to_income_ratio']):.1f}x), while mean one-way commute time is "
        f"relatively lower ({float(d['mean_commute_minutes']):.1f} min). The point is not that places "
        "rank on a single burden scale, but that affordability profiles differ."
    )
else:
    denver_line = (
        "Some selected county proxies show higher housing pressure with lower commute burden, and "
        "others show the opposite \u2014 the aim is profiles, not a single ranking."
    )

st.markdown(
    f'<h3 class="section-kicker section-head-normal">{escape(ACCESS_STANDS_OUT_TITLE)}</h3>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="standout-grid">'
    '<div class="standout-card standout-card--ur">'
    '<div class="standout-card__title">Upper-right combined burden</div>'
    f'<p class="standout-card__body">{escape(upper_right_names)} sit in the upper-right portion of the chart, '
    'where both home value-to-income ratios and mean one-way commute times are above the medians for these '
    'selected proxies.</p></div>'
    '<div class="standout-card standout-card--ul">'
    '<div class="standout-card__title">Access adds information</div>'
    f'<p class="standout-card__body">{escape(chicago_line)}</p></div>'
    '<div class="standout-card standout-card--lr">'
    '<div class="standout-card__title">Different profiles</div>'
    f'<p class="standout-card__body">{escape(denver_line)}</p></div>'
    '</div>',
    unsafe_allow_html=True,
)

st.markdown(f'<p class="story-page-intro story-readable">{escape(ACCESS_COMBINED_BRIDGE)}</p>', unsafe_allow_html=True)
st.markdown(
    f'<div class="takeaway-callout housing-takeaway"><p>{escape(ACCESS_TAKEAWAY)}</p></div>',
    unsafe_allow_html=True,
)
st.markdown(
    f'<p class="future-work-note"><strong>{escape(ACCESS_FUTURE_WORK_TITLE)}:</strong> {escape(ACCESS_FUTURE_WORK)}</p>',
    unsafe_allow_html=True,
)
st.markdown(f'<p class="data-scope-note source-note">{escape(ACCESS_BRIDGE)}</p>', unsafe_allow_html=True)
