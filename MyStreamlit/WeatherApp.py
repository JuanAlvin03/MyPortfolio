from email.policy import default
from locale import format_string
import streamlit as st
import requests
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Weather App", layout="wide")

@st.cache_data(ttl=900)
def fetch_data():
    APILinkWeather = "https://api.open-meteo.com/v1/forecast?latitude=-37.814&longitude=144.9633&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,uv_index_max,precipitation_probability_max&hourly=temperature_2m,rain,showers,relative_humidity_2m,wind_speed_10m,wind_direction_10m,precipitation_probability&timezone=Australia%2FSydney"
    response = requests.get(APILinkWeather).json()
    return response

data = fetch_data()

# Make DataFrame for data
hourly_weather_df = pd.DataFrame(data["hourly"])
daily_weather_df = pd.DataFrame(data["daily"], index=data["daily"]["time"])

# Title
st.title("Melbourne Weather Forecast")

# Timezone
weather_timezone = data["timezone"] + " (" + data["timezone_abbreviation"] + ")"
st.write(f"Timezone = {weather_timezone}")

# Day Selection
options = daily_weather_df["time"]
selected_day = st.segmented_control("Day", options, selection_mode="single", default=options.iloc[0])

# Display selected day
st.table(daily_weather_df.loc[[options.iloc[0] if selected_day is None else selected_day]])

#plot chart
fig = px.line(hourly_weather_df.head(24), x="time", y="temperature_2m", title="Hourly Temperature Forecast")
st.plotly_chart(fig)
