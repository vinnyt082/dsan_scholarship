"""Page 7 — Methods and References."""

import streamlit as st

from src.config import APP_TITLE, CUSTOM_CSS_PATH
from src.text_blocks import (
    AI_ASSISTANCE_NOTE,
    CLAIM_GUARDRAILS,
    METHODS_INTRO,
    METHODS_LIMITS,
    METHODS_NOTES,
    METHODS_REFERENCES,
    METHODS_TITLE,
    METHODS_PAGE_DISPLAY_TITLE,
)


def load_css() -> None:
    if CUSTOM_CSS_PATH.exists():
        st.markdown(f"<style>{CUSTOM_CSS_PATH.read_text()}</style>", unsafe_allow_html=True)


st.set_page_config(page_title=f"{METHODS_TITLE} | {APP_TITLE}", layout="wide")
load_css()

st.title(METHODS_PAGE_DISPLAY_TITLE)
st.markdown(METHODS_INTRO)

st.markdown("### Data sources and transformations")
for note in METHODS_NOTES:
    st.markdown(f"- {note}")

st.markdown("### Limitations")
for item in METHODS_LIMITS:
    st.markdown(f"- {item}")

st.markdown("### Claim boundaries")
st.markdown(CLAIM_GUARDRAILS)

st.markdown("### References")
for ref in METHODS_REFERENCES:
    st.markdown(f"- {ref}")

st.markdown("### AI assistance")
st.markdown(AI_ASSISTANCE_NOTE)
