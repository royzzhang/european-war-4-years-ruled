import streamlit as st

st.header('European War 4 Years Ruled Calculator')

continent = st.segmented_control('Conquest Map', ['Europe', 'America'], default='Europe')

num_generals = st.slider('Number of Generals', min_value=0, max_value=12, value=0)

general_ranks = [0] * num_generals
general_nobilities = [0] * num_generals
if num_generals:
    with st.expander('General Rank & Nobility', expanded=True):
        for i in range(num_generals):
            general_ranks[i] = st.select_slider(f'General {i + 1} Rank',
                                                [5, 10, 25, 20, 28, 36, 44, 54, 64, 74, 86, 98, 110, 125, 150],
                                                value=5)
            general_nobilities[i] = st.select_slider(f'General {i + 1} Nobility', [0, 1, 2, 3, 4, 5, 6, 7, 8, 10],
                                                     value=0)

headquarter_score = 0
general_rank_score = {5: 350,
                      10: 550,
                      25: 850,
                      20: 1250,
                      28: 1750,
                      36: 2350,
                      44: 3050,
                      54: 3850,
                      64: 4750,
                      74: 5750,
                      86: 6850,
                      98: 8050,
                      110: 9350,
                      125: 10750,
                      150: 12250}
general_nobility_score = {0: 0,
                          1: 500,
                          2: 1250,
                          3: 2250,
                          4: 3500,
                          5: 5000,
                          6: 6750,
                          7: 8750,
                          8: 11000,
                          10: 13500}
for i in range(num_generals):
    headquarter_score += general_rank_score[general_ranks[i]] + general_nobility_score[general_nobilities[i]]
europe_america_headquarter_score = min(headquarter_score, 34990)
asia_headquarter_score = min(headquarter_score, 87500)

gold = st.number_input('Gold', min_value=0, max_value=9999, value=0)
iron = st.number_input('Iron', min_value=0, max_value=9999, value=0)
food = st.number_input('Food', min_value=0, max_value=9999, value=0)
resource_score = gold + iron * 2 + food / 2

rounds = st.number_input('Round', min_value=1, max_value=300, value=1)

europe_america_rounds_score = 90960
if rounds > 31:
    europe_america_rounds_score -= (1716 + (min(45, rounds) - 31 - 1) * 832.5) * 2
if rounds > 45:
    europe_america_rounds_score -= (8326 + (min(55, rounds) - 45 - 1) * 693.75) * 2
if rounds > 55:
    europe_america_rounds_score -= (6798 + (min(65, rounds) - 55 - 1) * 555) * 2
if rounds > 65:
    europe_america_rounds_score -= (5272 + (min(75, rounds) - 65 - 1) * 416.25) * 2
if rounds > 75:
    europe_america_rounds_score -= (3746 + (min(100, rounds) - 75 - 1) * 277.5) * 2

asia_rounds_score = -52500
if rounds <= 20:
    asia_rounds_score *= -1
elif rounds == 21:
    asia_rounds_score = 50200
elif (continent == 'Europe' and 22 <= rounds <= 30) or (continent == 'America' and 22 <= rounds <= 25):
    asia_rounds_score = 77500 - 1300 * rounds
elif (continent == 'Europe' and 31 <= rounds <= 40) or (continent == 'America' and 26 <= rounds <= 35):
    asia_rounds_score = 45000 - 975 * rounds
elif (continent == 'Europe' and 41 <= rounds <= 50) or (continent == 'America' and 36 <= rounds <= 45):
    asia_rounds_score = 12500 - 650 * rounds
elif (continent == 'Europe' and 51 <= rounds <= 60) or (continent == 'America' and 46 <= rounds <= 50):
    asia_rounds_score = -20000 - 325 * rounds

stars = st.number_input('Campaign Stars', min_value=0, max_value=420, value=0)
europe_america_star_score = min(stars * 50, 11660)
asia_star_score = min(stars * 85, 35000)

europe_america_score = (resource_score + europe_america_star_score + europe_america_rounds_score +
                        europe_america_headquarter_score) / 186.6
asia_score = (resource_score + asia_star_score + asia_rounds_score + asia_headquarter_score) / 280

st.text(f'Years Ruled ({continent}, real): {europe_america_score}')
st.text(f'Years Ruled (Asia, real): {asia_score}')
st.text(f'Years Ruled ({continent}, displayed): {max(0, int(europe_america_score / 50) * 50)}')
st.text(f'Years Ruled (Asia, displayed): {max(0, int(asia_score / 50) * 50)}')
