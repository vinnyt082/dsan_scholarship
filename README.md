# Trading Time for Affordability

This project is a professional DSAN scholarship data storytelling project about the combined burden of housing cost and access. The core idea is that housing affordability should not be understood only as the sticker price of housing; real affordability also depends on how much time, distance, and transportation burden is required to reach work and participate in daily economic life.

## Research Question

Has the pursuit of affordable housing increasingly required Americans to pay in commute time and access?

## Claim Style

The project will use careful, non-causal language. It should describe patterns as being "associated with," "consistent with," "coinciding with," "suggesting," or "revealing a tradeoff." It should not claim that housing prices directly caused commute times to rise or that the analysis proves suburbanization.

## Planned Story Structure

1. Home / Story Overview
2. Housing Prices
3. Paychecks and Purchasing Power
4. Commute Burden
5. Housing + Access
6. Methods / References

The final product should be a guided Streamlit data story, not a broad dashboard. Every chart should support the central narrative.

## Planned Data Sources

Primary sources should be transparent and controlled:

- FRED direct CSV downloads where possible.
- `fredapi` if an API key is provided.
- Manually downloaded CSVs placed in `data/raw/`.
- Census ACS data only if FRED-hosted commute/access data is insufficient.

Candidate FRED series include:

- `MSPUS`: Median Sales Price of Houses Sold for the United States.
- `CPIAUCSL` or equivalent CPI all-items series for inflation adjustment.
- `CSUSHPINSA`: Case-Shiller U.S. National Home Price Index.
- `MORTGAGE30US`: 30-Year Fixed Rate Mortgage Average.
- `MEHOINUSA672N`: Real Median Household Income in the United States.
- `CUUR0000SAS2RS` or related shelter/rent CPI series.
- `CUSR0000SAS4` or related transportation services CPI series.

Commute/access data will start with an inventory of FRED-hosted ACS mean commute-time options. If FRED is not sufficient, a later phase may evaluate controlled Census ACS ingestion, potentially using aggregate travel time to work and worker counts where methodologically appropriate.

## Workflow Phases

1. Project scope and data inventory.
2. FRED source review and controlled housing/income/inflation ingestion.
3. Commute/access data source review and controlled ingestion.
4. Notebook-first cleaning, exploratory analysis, and metric design.
5. Visual prototyping.
6. Export of processed CSVs and app-ready assets.
7. Streamlit data story implementation.

The analytical workflow is notebook-first. The Streamlit app should read processed CSVs created by notebooks.

## Running the data story

From the project root (with dependencies installed):

```bash
streamlit run Home.py
```

The entry file is `Home.py` so the sidebar labels the overview as **Home** (instead of defaulting to “app” when the script was named `app.py`).

