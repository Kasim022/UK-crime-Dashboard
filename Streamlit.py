import streamlit as st
import pandas as pd 
import numpy as np 
import plotly.express as px

st.set_page_config(page_title='Crime in UK', layout='wide')
st.title('Crime in UK stats')

df = pd.read_excel("crimedata2026.xlsx")

st.subheader("Data Preview")
st.dataframe(df)

with st.sidebar:
    st.header("Filters")

    city_options = ["ALL"] + sorted(df["City"].unique().tolist())
    selected_city = st.selectbox("Select City", city_options)

    crime_options = ["ALL"] + sorted(df["Crime type"].unique().tolist())
    selected_crime = st.selectbox("Select Crime Type", crime_options)

filtered_df = df.copy()
if selected_city != "ALL":
    filtered_df = filtered_df[filtered_df["City"] == selected_city]
if selected_crime != "ALL":
    filtered_df = filtered_df[filtered_df["Crime type"] == selected_crime]

st.subheader("Overview")
kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:
    st.metric("Total Crimes", f"{len(filtered_df):,}")

with kpi2:
    top_crime = filtered_df['Crime type'].value_counts().idxmax()
    st.metric("Most Common Crime", top_crime)

with kpi3:
    resolved_pct = (filtered_df['Last outcome category'] != 'N/A').mean() * 100
    st.metric("Outcome Recorded", f"{resolved_pct:.1f}%")

#Visualisation

#crimes By Date
crime_counts = filtered_df['Crime type'].value_counts()
fig1 = px.bar(crime_counts, x=crime_counts.index, y=crime_counts.values,
              labels={'x': 'Crime Type', 'y': 'Count'},
              title='Crimes by Type')

month_counts = filtered_df['Month'].value_counts().sort_index()
fig2 = px.bar(month_counts, x=month_counts.index, y=month_counts.values,
              labels={'x': 'Month', 'y': 'Count'},
              title='Crimes by Month')

map_df = filtered_df.copy()
map_df['Longitude'] = pd.to_numeric(map_df['Longitude'], errors='coerce')
map_df['Latitude'] = pd.to_numeric(map_df['Latitude'], errors='coerce')
map_df = map_df.dropna(subset=['Longitude', 'Latitude'])

#Build Map
st.subheader("Crime Map")
fig_map = px.scatter_map(
    map_df,
    lat="Latitude",
    lon="Longitude",
    hover_name="Crime type",
    hover_data=["Last outcome category", "Location"],
    zoom=8,
    height=600
)

fig_map.update_layout(map_style="open-street-map")
st.plotly_chart(fig_map, use_container_width=True)

#Plot Graph
col1, col2 = st.columns(2)
with col1:
    st.subheader("Crimes by Type")
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    st.subheader("Crimes by Month")
    st.plotly_chart(fig2, use_container_width=True)

    