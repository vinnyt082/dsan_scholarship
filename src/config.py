"""Project configuration for the Streamlit prototype."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
ASSETS_DIR = PROJECT_ROOT / "assets"
CSS_DIR = ASSETS_DIR / "css"
CUSTOM_CSS_PATH = CSS_DIR / "custom.css"

NATIONAL_STORY_PATH = PROCESSED_DATA_DIR / "national_story_series.csv"
COMMUTE_STORY_PATH = PROCESSED_DATA_DIR / "commute_story_series.csv"
HOUSING_ACCESS_PATH = PROCESSED_DATA_DIR / "housing_access_geo_snapshot.csv"

APP_TITLE = "Trading Time for Affordability"
FINAL_NATIONAL_YEAR = 2024
FINAL_COMMUTE_YEAR = 2024
OMITTED_COMMUTE_YEAR = 2020

# Aligned with assets/css/custom.css (--housing, --access, etc.)
COLORS = {
    "background": "#F7F4EF",
    "paper": "#FFFFFF",
    "surface_soft": "#FBFAF7",
    "text": "#22313A",
    "muted": "#667783",
    "border": "#DEDBD4",
    "grid": "#DEDBD4",
    "housing": "#9A3F2F",
    "accent": "#9A3F2F",
    "income": "#5F6F7E",
    "commute": "#2F7A7D",
    "reference": "#A8ACA5",
}
