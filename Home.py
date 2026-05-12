"""Home / Story Overview — Trading Time for Affordability."""

from html import escape
from pathlib import Path

import streamlit as st

from src.config import APP_TITLE, ASSETS_DIR, CUSTOM_CSS_PATH
from src.data_helpers import (
    DataLoadError,
    load_commute_story,
    load_national_story,
    national_commute_trend,
    render_data_error,
)
from src.text_blocks import (
    APP_SUBTITLE,
    HOME_CENTRAL_QUESTION,
    HOME_DATA_SCOPE,
    HOME_INTRO,
    HOME_INTRO_2,
    HOME_LENS_LEADIN,
    HOME_LENS_SECTION_TITLE,
    HOME_SNAPSHOT_BRIDGE,
    HOME_SNAPSHOT_SECTION_TITLE,
    HOME_SNAPSHOT_SUBTITLE,
    HOME_STORY_PATH_CALLOUT,
)

ILLUSTRATIONS_DIR = ASSETS_DIR / "illustrations"

_LENS_EQUATION_CARDS = [
    {
        "key": "housing",
        "title": "Housing pressure",
        "desc": "What do homes cost?",
        "svg": "housing_pressure.svg",
        "final": False,
    },
    {
        "key": "income",
        "title": "Price-to-income pressure",
        "desc": "How much income does housing require?",
        "svg": "price_income_pressure.svg",
        "final": False,
    },
    {
        "key": "access",
        "title": "Access burden",
        "desc": "How much time does location require?",
        "svg": "access_burden.svg",
        "final": False,
    },
    {
        "key": "final",
        "title": "Practical affordability",
        "desc": "Housing cost and access read together.",
        "svg": "practical_affordability.svg",
        "footer": "Housing + access",
        "final": True,
    },
]


def load_css() -> None:
    if CUSTOM_CSS_PATH.exists():
        st.markdown(f"<style>{CUSTOM_CSS_PATH.read_text()}</style>", unsafe_allow_html=True)


def _read_svg(name: str) -> str:
    path = ILLUSTRATIONS_DIR / name
    if path.exists():
        return path.read_text()
    return ""


def _lens_equation_html() -> str:
    separators = ["+", "+", "→"]
    parts: list[str] = []

    for i, card in enumerate(_LENS_EQUATION_CARDS):
        if i > 0:
            sep = separators[i - 1]
            cls = "lens-eq-sep--arrow" if sep == "→" else ""
            parts.append(
                f'<div class="lens-eq-sep {cls}">{escape(sep)}</div>'
            )

        svg_markup = _read_svg(card["svg"])
        modifier = f"lens-eq-card--{card['key']}"
        if card["final"]:
            modifier += " lens-eq-card--final"

        footer_html = ""
        if card.get("footer"):
            footer_html = f'<div class="lens-eq-footer-label">{escape(card["footer"])}</div>'

        parts.append(
            f'<div class="lens-eq-card {modifier}">'
            f'  <div class="lens-eq-icon">{svg_markup}</div>'
            f'  <div class="lens-eq-title">{escape(card["title"])}</div>'
            f'  <div class="lens-eq-desc">{escape(card["desc"])}</div>'
            f'  {footer_html}'
            f'</div>'
        )

    return f'<div class="lens-equation">{"".join(parts)}</div>'


def _snapshot_html(price_s: str, ratio_s: str, commute_s: str) -> str:
    blocks = [
        ("Real median home sale price", price_s, "2024 dollars"),
        ("Home price-to-income ratio", ratio_s, "median home price / real median household income"),
        ("National mean one-way commute", commute_s, "ACS-era access lens"),
    ]
    cards = []
    for label, value, cap in blocks:
        cards.append(
            f'<div class="snapshot-card story-card">'
            f'<div class="snapshot-card__label">{escape(label)}</div>'
            f'<div class="snapshot-card__value">{escape(value)}</div>'
            f'<div class="snapshot-card__caption">{escape(cap)}</div>'
            f'</div>'
        )
    return f'<div class="snapshot-grid">{"".join(cards)}</div>'


st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)
load_css()

st.title(APP_TITLE)
st.markdown(f'<p class="home-subtitle">{escape(APP_SUBTITLE)}</p>', unsafe_allow_html=True)

st.markdown(f'<p class="home-intro story-readable">{escape(HOME_INTRO)}</p>', unsafe_allow_html=True)
st.markdown(f'<p class="home-intro story-readable">{escape(HOME_INTRO_2)}</p>', unsafe_allow_html=True)
st.markdown(
    f'<p class="story-callout">{escape(HOME_CENTRAL_QUESTION)}</p>',
    unsafe_allow_html=True,
)

# ── Data for metrics ──
try:
    national = load_national_story()
    commute = national_commute_trend(load_commute_story())
except DataLoadError as exc:
    render_data_error(exc)

home_price = national.loc[national["year"].eq(2024), "real_median_home_price"].dropna()
ratio = national.loc[national["year"].eq(2024), "home_price_to_real_income_ratio"].dropna()
commute_2024 = commute.loc[commute["year"].eq(2024), "mean_commute_minutes"].dropna()

price_str = f"${home_price.iloc[0]:,.0f}" if not home_price.empty else "—"
ratio_str = f"{ratio.iloc[0]:.1f}x" if not ratio.empty else "—"
commute_str = f"{commute_2024.iloc[0]:.1f} min" if not commute_2024.empty else "—"

# ── Three Lenses: illustrated equation ──
st.markdown(
    f'<h3 class="section-kicker">{escape(HOME_LENS_SECTION_TITLE)}</h3>',
    unsafe_allow_html=True,
)
st.markdown(
    f'<p class="lens-leadin">{escape(HOME_LENS_LEADIN)}</p>',
    unsafe_allow_html=True,
)
st.markdown(_lens_equation_html(), unsafe_allow_html=True)

# ── National snapshot ──
st.markdown(
    f'<h3 class="section-kicker">{escape(HOME_SNAPSHOT_SECTION_TITLE)}</h3>',
    unsafe_allow_html=True,
)
st.markdown(
    f'<p class="snapshot-subtitle">{escape(HOME_SNAPSHOT_SUBTITLE)}</p>',
    unsafe_allow_html=True,
)
st.markdown(_snapshot_html(price_str, ratio_str, commute_str), unsafe_allow_html=True)

st.markdown(f'<p class="data-scope-note source-note">{escape(HOME_DATA_SCOPE)}</p>', unsafe_allow_html=True)
st.markdown(f'<p class="home-intro story-readable">{escape(HOME_SNAPSHOT_BRIDGE)}</p>', unsafe_allow_html=True)
st.markdown(
    f'<div class="takeaway-callout"><p>{escape(HOME_STORY_PATH_CALLOUT)}</p></div>',
    unsafe_allow_html=True,
)
