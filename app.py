import streamlit as st
import pandas as pd

st.set_page_config(page_title="IPL Dashboard", layout="wide")

# Load data
matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

# Sidebar Menu
menu = st.sidebar.selectbox("Select Page", ["Home", "IPL Dashboard"])

# ---------------- HOME ----------------
if menu == "Home":
    st.title("🏏 Sports Analytics Portfolio")
    st.write("Welcome to IPL Dashboard Project")

# ---------------- IPL DASHBOARD ----------------
elif menu == "IPL Dashboard":

    st.header("Season Filter")

    seasons = sorted(matches['season'].unique())
    selected_season = st.selectbox("Select Season", seasons)

    season_match_ids = matches[matches['season'] == selected_season]['id']
    season_data = deliveries[deliveries['match_id'].isin(season_match_ids)]

    if season_data.empty:
        st.warning("No data found for selected season.")
        st.stop()

    players = sorted(season_data['batsman'].unique())

    if not players:
        st.warning("No players available.")
        st.stop()

    selected_player = st.selectbox("Select Player", players)

    player_data = season_data[season_data['batsman'] == selected_player]

    total_runs = player_data['batsman_runs'].sum()
    balls = len(player_data)
    strike_rate = (total_runs / balls) * 100 if balls > 0 else 0

    st.metric("Total Runs", total_runs)
    st.metric("Balls Faced", balls)
    st.metric("Strike Rate", round(strike_rate, 2))
     
