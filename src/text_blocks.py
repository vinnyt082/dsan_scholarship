"""Narrative copy for the Streamlit data story."""

APP_SUBTITLE = "A data story about housing prices, paychecks, and the hidden cost of access"

HOME_INTRO = (
    "Most housing affordability stories begin with price. This one starts there too — then asks what price "
    "leaves out. Home prices and incomes describe the dollar side of affordability, while commute time adds "
    "a second lens: the access burden that comes with location."
)
HOME_INTRO_2 = (
    "Together, these lenses frame a broader question: what changes when affordability is read not only as "
    "housing cost, but also as time and access?"
)

HOME_CENTRAL_QUESTION = "What does housing affordability look like when commute time enters the story?"

HOME_LENS_SECTION_TITLE = "Three lenses"

HOME_LENS_CARDS = [
    {
        "title": "Price",
        "question": "What does housing cost?",
        "description": "Real median home sale prices show long-run housing pressure.",
    },
    {
        "title": "Paycheck",
        "question": "What can households afford?",
        "description": "The home price-to-income ratio adds price-to-income pressure to the sticker-price view.",
    },
    {
        "title": "Access",
        "question": "How much time does location require?",
        "description": "Mean one-way commute time reveals access burden that dollars alone miss.",
    },
]

HOME_AFFORDABILITY_FORMULA = [
    ("Housing pressure", "chip"),
    ("+", "op"),
    ("Price-to-income pressure", "chip"),
    ("+", "op"),
    ("Access burden", "chip"),
    ("→", "arrow"),
    ("Practical affordability", "chip--outcome"),
]

HOME_LENS_LEADIN = "Each lens adds one part of the affordability picture."

HOME_SNAPSHOT_SECTION_TITLE = "The national picture in 2024"
HOME_SNAPSHOT_SUBTITLE = "Three national reference points anchor the story before the geographic comparison."

HOME_DATA_SCOPE = (
    "Data scope: median home sale price context, 1963–2024; home price-to-income ratio, 1984–2024; "
    "commute/access data cover 2005–2024 with 2020 omitted; geographic comparisons use 2023 selected county "
    "proxies, not full metro areas."
)

HOME_SNAPSHOT_BRIDGE = (
    "Taken together, these three reference points sketch the national backdrop for the story. Home prices "
    "remain high in real terms, the home price-to-income ratio gives that pressure a household lens, and "
    "commute time introduces the access side of affordability. From here, the pages that follow unpack "
    "those pieces one at a time."
)
HOME_STORY_PATH_CALLOUT = (
    "The story moves from dollars to time: sticker price, then paycheck context, then access burden. "
    "The final view brings those lenses together."
)

# Page 2 — Housing Prices
HOUSING_TITLE = "The Sticker Price Story"
HOUSING_INTRO = (
    "The first layer is the sticker price: the national median home sale price. Adjusting for inflation "
    "puts past and present prices on the same scale in 2024 dollars. Once the dollars are comparable, "
    "the pattern is clear: real home prices rose substantially over the long run."
)
HOUSING_SOURCE_CAPTION = (
    "Source: FRED `MSPUS` and `CPIAUCSL`; quarterly median sale prices annualized and adjusted to 2024 dollars."
)
HOUSING_BRIDGE = (
    "Viewed this way, the story is not just that nominal prices rose over time. Even after translating the "
    "series into 2024 dollars, the long-run level of home prices is much higher than where it began. That "
    "makes sticker price a useful starting point \u2014 but not the full affordability picture."
)
HOUSING_TAKEAWAY_CALLOUT = (
    "Takeaway: Inflation adjustment removes the simplest explanation \u2014 real median home sale prices "
    "still more than doubled between 1963 and 2024. The next question is how those prices compare with "
    "household income."
)

# Page 3 — Paychecks
PAYCHECKS_TITLE = "Prices Versus Paychecks"
PAYCHECKS_INTRO = (
    "Sticker price shows what homes cost; income shows what households can absorb. This page pairs the "
    "national median home sale price with real median household income, creating a simple pressure gauge: "
    "how large the median home price is relative to a typical household\u2019s income. It is not a full "
    "affordability audit, but it makes the paycheck side of the story visible."
)
PAYCHECKS_INTERPRETATION_NOTE = (
    "A ratio of 5.0x means the median home sale price was about five times real median household income. "
    "It is a national pressure gauge, not a complete affordability measure."
)
PAYCHECKS_SOURCE_CAPTION = (
    "Source: FRED `MSPUS`, `CPIAUCSL`, and `MEHOINUSA672N`; home prices adjusted to 2024 dollars; "
    "income already real and not deflated again."
)
PAYCHECKS_BRIDGE = (
    "Seen as a ratio, the same home price becomes more personal. The question is no longer only whether "
    "homes cost more, but how much of a typical household\u2019s income the median home price represents. "
    "That comparison makes the paycheck side of affordability visible, while still leaving out the time "
    "and location side of the story."
)
PAYCHECKS_TAKEAWAY_CALLOUT = (
    "Takeaway: By 2024, the median home sale price was about five times real median household income, "
    "up from about four times in 1984. The next page adds time: the access burden of reaching work."
)
MORTGAGE_EXPANDER_LABEL = "Financing context: mortgage rates"
MORTGAGE_CONTEXT_INTRO = (
    "Home prices and incomes tell one part of the story. Mortgage rates change the monthly payment "
    "attached to a given price, which is why affordability can feel different even when the sticker "
    "price looks similar."
)
MORTGAGE_CONTEXT_NOTE = (
    "Mortgage rates matter because they translate a sticker price into a monthly payment. That makes them "
    "useful context for interpreting buying conditions across time. Still, this project keeps the main "
    "thread narrower: first the price-to-income pressure, then the access burden that price alone does "
    "not capture."
)

# Page 4 — Commute
COMMUTE_TITLE = "Access Has a Time Cost"
COMMUTE_INTRO_1 = (
    "Earlier pages measured affordability in dollars. This page adds time. Mean one-way commute time is one "
    "way to see the access burden that comes with location: time spent reaching work instead of using that "
    "time elsewhere."
)
COMMUTE_INTRO_2 = (
    "The commute record is shorter than the housing record, so this is a recent access lens rather than a "
    "60-year trend. Where housing data show shelter cost, commute data add a view of what people may pay "
    "in time to reach opportunity."
)
COMMUTE_DATA_NOTE = (
    "Data note: ACS commute data start much later than the housing series. The 2020 point is omitted, "
    "and post-2020 readings should be read with remote- and hybrid-work shifts in mind."
)
COMMUTE_POST2020_NOTE = (
    "Post-2020 context: The 2020 ACS value is omitted because the pandemic disrupted normal commuting "
    "patterns and ACS data collection. Even with remote and hybrid work more common after 2020, the "
    "national mean one-way commute in 2024 remains close to the pre-2020 peak shown in this series."
)
COUNTY_PROXY_NOTE = (
    "Geographic comparisons use selected county proxies for major U.S. regions, not full metro areas."
)
COMMUTE_NATIONAL_CAPTION = "Source: Census ACS 1-year, United States. Years 2005–2019 and 2021–2024; 2020 omitted."
COMMUTE_RANK_CAPTION = "Source: Census ACS 5-year 2023. Selected county proxies, not full metro areas."
COMMUTE_PLACE_HEADING = "Access burden varies by place"
COMMUTE_PLACE_INTRO = (
    "National averages hide local variation. The ranked chart below uses the same 2023 selected county "
    "proxies that appear in the combined housing + access view."
)
COMMUTE_NATIONAL_BRIDGE = (
    "On its own, the national series is a modest movement in minutes, not a dramatic long-run price chart. "
    "But that is part of the point: time burden can change slowly and still matter in daily life. By 2024, "
    "the national mean one-way commute remains close to its pre-2020 high, even after the disruption of "
    "remote and hybrid work."
)
COMMUTE_RANK_BRIDGE = (
    "The ranked view shifts the story from a national average to place-to-place variation. Among these "
    "selected county proxies, commute burden is not evenly distributed: some places sit several minutes "
    "above the group\u2019s lower end. That variation is what makes access useful to carry into the combined "
    "housing-and-commute view."
)
COMMUTE_TRANSITION = (
    "Next: the combined page places this time burden next to housing pressure for the same selected county proxies."
)

# Page 5 — Housing + Access
ACCESS_TITLE = "The Combined Burden"
ACCESS_INTRO = (
    "This view brings housing pressure and access burden together. Each point is a selected county proxy: "
    "the horizontal axis shows the home value-to-income ratio, and the vertical axis shows mean one-way "
    "commute time."
)
ACCESS_HOW_TO_READ = (
    "How to read this chart: points farther right have higher home value-to-income ratios; points higher up "
    "have longer mean one-way commutes. The dashed median lines divide the selected proxies into four "
    "affordability profiles."
)
ACCESS_METRIC_DISTINCTION_NOTE = (
    "Note: this geographic snapshot uses ACS home value and income, so it should be read as a selected-place "
    "comparison rather than the same national home sale price series used earlier."
)
ACCESS_GUIDE_LABELS = [
    "Lower housing pressure / lower commute burden",
    "Higher housing pressure / lower commute burden",
    "Lower housing pressure / higher commute burden",
    "Higher housing pressure / higher commute burden",
]
ACCESS_CHART_TITLE = "Housing pressure and commute burden, 2023"
ACCESS_CHART_SUBTITLE = "Selected county proxies; ACS 5-year estimates"
ACCESS_SOURCE_CAPTION = "Source: Census ACS 5-year 2023. Selected county proxies, not full metro areas."
ACCESS_STANDS_OUT_TITLE = "What stands out"
ACCESS_COMBINED_BRIDGE = (
    "Taken together, the points make the combined lens more useful than either axis alone. A place can "
    "look less pressured on the housing axis while still carrying a high commute burden, or it can show "
    "the opposite pattern. The value of the chart is not in naming a single most burdened place, but in "
    "showing that affordability profiles take different shapes."
)
ACCESS_TAKEAWAY = (
    "Takeaway: Affordability does not line up on a single axis. Reading housing pressure and access burden "
    "together reveals different profiles across the selected places."
)
ACCESS_FUTURE_WORK_TITLE = "Future work"
ACCESS_FUTURE_WORK = (
    "A useful next step would be metro-scale maps showing how the geographic “cloud” of commuting—where workers "
    "travel from, and how wide that pattern is—evolves from 2005 through 2024 for a few carefully chosen cities. "
    "That kind of view would add spatial intuition to the housing + access story, but it needs additional data "
    "collection, geocoding, and cartography work beyond what this one-week build could take on."
)
ACCESS_BRIDGE = "The conclusion summarizes the logic — and what this lens does not claim."

# Page 6 — Conclusion
CONCLUSION_TITLE = "What Affordability Really Costs"
CONCLUSION_OPENING = (
    "This project began with the visible side of affordability: price. National data show real median home sale "
    "prices rose sharply over the long run. Adding the paycheck lens clarifies price-to-income pressure. "
    "Even then, the story is incomplete if affordability is treated only as dollars."
)
CONCLUSION_OPENING_2 = (
    "Mean one-way commute time adds a second dimension: access also has a cost \u2014 in minutes, routine, flexibility, "
    "and proximity to opportunity."
)
CONCLUSION_OPENING_3 = (
    "Over time, the national picture points to a clear shift: housing became more expensive in real terms, "
    "and by 2024 the median home sale price represented a larger multiple of real median household income "
    "than it did in the mid-1980s. Commute data cover a shorter period, but they add a recent access lens: "
    "the time cost of reaching work remains part of the lived affordability picture. The project\u2019s "
    "conclusion is not that one metric explains cost of living, but that the story has become harder to "
    "read from prices alone."
)
CONCLUSION_RECAP_TITLE = "The story in four steps"
CONCLUSION_RECAP_STEP_REAL_PRICES = "Real median home sale prices more than doubled from 1963 to 2024."
CONCLUSION_RECAP_STEP_PAYCHECK = (
    "By 2024, the median home sale price was about five times real median household income \u2014 a simple "
    "marker of price-to-income pressure."
)
CONCLUSION_RECAP_STEP_ACCESS = (
    "Commute data cover a shorter period, but from 2005 to 2024 they add a recent view of how access "
    "burden fits into the cost-of-living story."
)
CONCLUSION_RECAP_STEP_COMBINED = (
    "The selected-county snapshot shows that housing pressure and access burden do not always line up in the "
    "same way \u2014 practical affordability reads best as a combined lens."
)
CONCLUSION_LAYERS_TITLE = "The affordability story has layers"
CONCLUSION_LAYER_CARDS = [
    (
        "Sticker price",
        "Real median home sale prices rose even after inflation.",
        "~$419k in 2024",
    ),
    (
        "Paycheck pressure",
        "Home price-to-income ratio clarifies price-to-income pressure.",
        "5.0x in 2024",
    ),
    (
        "Access burden",
        "Mean one-way commute time makes location’s time cost visible.",
        "27.2 min in 2024",
    ),
    (
        "Practical affordability",
        "Read housing pressure together with access burden.",
        "Housing + access",
    ),
]
CONCLUSION_THESIS = (
    "Affordability should be measured not only by the sticker price of housing, but by the combined "
    "burden of housing pressure and access."
)
CONCLUSION_IMPLICATIONS_TITLE = "What this means"
CONCLUSION_IMPLICATIONS_INTRO = (
    "These recommendations are intentionally focused on measurement and planning. The analysis does not "
    "identify one cause of affordability pressure, but it does show why housing cost, income, and access "
    "should be read together."
)
CONCLUSION_IMPLICATION_1_TITLE = (
    "Housing policymakers and planners should evaluate affordability with access, not only unit cost."
)
CONCLUSION_IMPLICATION_1_TEXT = (
    "This analysis shows that housing pressure and commute burden do not always move together across "
    "selected places. A lower home value-to-income ratio may still come with a higher time burden."
)
CONCLUSION_IMPLICATION_2_TITLE = (
    "Transportation planners should treat commute burden as part of affordability."
)
CONCLUSION_IMPLICATION_2_TEXT = (
    "The commute data show that mean one-way commute time remains close to its pre-2020 high nationally, "
    "and the selected county snapshot shows meaningful place-to-place variation."
)
CONCLUSION_IMPLICATION_3_TITLE = (
    "Advocates and analysts should avoid single-score affordability rankings."
)
CONCLUSION_IMPLICATION_3_TEXT = (
    "The combined view shows different affordability profiles: some places have higher housing pressure, "
    "some have higher commute burden, and some have both. A useful affordability story should preserve "
    "those differences."
)
CONCLUSION_NOT_CLAIM_TITLE = "What this does not claim"
CONCLUSION_NOT_CLAIM_TEXT = (
    "This project does not claim that rising home prices caused longer commutes. It does not rank entire "
    "metro areas, and it does not measure every part of cost of living. Its contribution is a more complete "
    "affordability lens \u2014 one that reads housing pressure alongside access burden."
)
CONCLUSION_BRIDGE = (
    "Taken together, the recommendations point to the same lesson: affordability is not a single number. "
    "Housing prices matter, incomes matter, and access matters too. Read together, they suggest that the "
    "lived burden of a home depends not only on what it costs, but also on how that location connects "
    "people to work and daily life."
)
CONCLUSION_CLOSING = (
    "The practical question is not only whether a household can afford a home. It is whether that home still "
    "connects them to work, time, and daily life."
)

# Page 7 — Methods / References
METHODS_TITLE = "Methods and References"
METHODS_PAGE_DISPLAY_TITLE = "Methods & References"
METHODS_INTRO = "Sources, transformations, and limits for this data story."
METHODS_NOTES = [
    "FRED: `MSPUS` (median sale price), `CPIAUCSL` (CPI-U), `MEHOINUSA672N` (real median household income), `MORTGAGE30US` (30-year fixed).",
    "Nominal median sale prices were converted to 2024 dollars using CPI-U; real median household income was not deflated again.",
    "Higher-frequency series were annualized as documented in the project notebooks (averages within calendar year).",
    "National charts end at 2024; later years are excluded from the story views.",
    "Census ACS: national mean one-way commute from ACS 1-year, United States, 2005–2019 and 2021–2024; 2020 omitted.",
    "Geographic snapshot: 2023 ACS 5-year selected county proxies; mean commute uses aggregate travel time divided by the commuting-worker denominator from the pipeline.",
]
METHODS_LIMITS = [
    "Commute/access coverage is shorter than long-run housing data; interpret commutes as a recent lens.",
    "2020 is omitted; post-2020 commute patterns may reflect remote- and hybrid-work change.",
    "Geographic points are selected county proxies, not full metro areas or exhaustive national rankings.",
]
METHODS_REFERENCES = [
    "Federal Reserve Economic Data (FRED), Federal Reserve Bank of St. Louis: https://fred.stlouisfed.org/",
    "U.S. Census Bureau, American Community Survey (ACS): https://www.census.gov/programs-surveys/acs/",
]
CLAIM_GUARDRAILS = (
    "Language stays non-causal: findings add context and suggest tradeoffs. The story does not claim housing prices "
    "caused longer commutes or that the analysis proves suburbanization."
)
AI_ASSISTANCE_NOTE = (
    "Claude was used in an assistive capacity to generate the standalone SVG icons used in the Home page "
    "\"Three Lenses\" equation cards. AI was also used as a final check for spelling and grammar. (ChatGBT 5.5)."
)
