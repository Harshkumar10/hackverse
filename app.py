import streamlit as st

st.set_page_config(layout = "wide")

col1 = st.sidebar

st.title("Build your Dream 11 - A Data Web App")

details_expander = st.beta_expander("App Details")
details_expander.markdown("""This app performs simple calculations based on the player's past data of batting and bowling
- **Python Libraries:** *pandas, base64, streamlit*
- **Data Source:** [cricbuzz](https://www.cricbuzz.com)
- **Repository:** [GitHub Link](https://github.com/Harshkumar10/hackverse)""")

points_expander = st.beta_expander("Points Distribution")
points_expander.markdown("""
- **Runs:** Total Runs Scored (1 Point)
- **SR:** Batting Strike Rate
- **4s:** No. of fours (1 Point)
- **6s:** No. of Sixes (2 Points)
- **50:** No. of Half Centuries (8 Points)
- **100:** No. of Centuries (16 Points)
- **200:** No. of Double Centuries (32 Points)
- **Wkts:** No. of Wickets taken (25 Points)
- **Econ:** Bowler Economy Rate
- **5W:** No. of times bowler took 5 wickets in a single match (8 Points)
- **10W:** No. of times bowler took 10 wickets in a single match (16 Points)
""")

col1.header("User Input Features")
selected_type = col1.selectbox('Match Type', match_types, index = 2)
team1 = col1.selectbox('Team 1', teams)
team2 = col1.selectbox('Team 2', teams[1:], index = 2)
sort_type = col1.selectbox('Sort by', sort_types)
batsman = col1.slider('No. of Batsman', 1, 9, 3)
bowlers = col1.slider('No. of Bowlers', 1, (11-batsman), 2)

col1.write("** Rest of the players will be selected based on their overall performances")
