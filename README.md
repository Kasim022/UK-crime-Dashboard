# UK Crime Dashboard (Beta)

An interactive dashboard for exploring UK street-level crime data, built with Streamlit and Plotly.

As a data analyst, I wanted a hands-on project to practice building interactive dashboards — this pulls together real UK police data (Merseyside, West Yorkshire, South Yorkshire) into a filterable map and charts.

**Status:** Early beta functionality works (map, filters, KPIs), UI polish is still in progress.

<img width="1912" height="902" alt="screenshot1" src="https://github.com/user-attachments/assets/8f8d6b52-38b0-46cd-8880-988bc938f0f0" />

<img width="1606" height="877" alt="screenshot2" src="https://github.com/user-attachments/assets/672aa071-7b4a-4c8e-8b48-5bae0c19543d" />



## Features
- Interactive map with hover details (crime type, outcome, location)
- Filter by city and crime type
- KPI overview (total crimes, most common crime type, outcome recorded %)
- Crimes by type and by month charts

## Data
Source: [data.police.uk](https://data.police.uk) — official UK Police open data (street-level crimes, June–July 2026).

## Running it locally
\`\`\`
pip install -r requirements.txt
streamlit run Streamlit.py
\`\`\`
