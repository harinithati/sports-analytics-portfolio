elif menu == "IPL Dashboard":

    st.header("Season Filter")

    seasons = sorted(matches['season'].unique())
    selected_season = st.selectbox("Select Season", seasons)
    selected_season = int(selected_season)

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
balls = player_data.shape[0]
strike_rate = (total_runs / balls) * 100 if balls > 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total Runs", total_runs)
col2.metric("Balls Faced", balls)
col3.metric("Strike Rate", round(strike_rate, 2))
     
