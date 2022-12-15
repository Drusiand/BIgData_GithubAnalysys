import streamlit as st
import pandas as pd
import altair as alt
import sys

# print("counters", sys.argv)
path = sys.argv[1] if len(sys.argv) > 1 else "/pretty_csv"

st.set_page_config(
    page_title="Языки и технологии",
    layout='wide'
)

st.markdown('## 20 самых широко используемых языков')
language_data = pd.read_csv(path + '/language_count.csv',
                            names=['Язык', 'Число репозиториев'])
# st.bar_chart(language_data[:20], x='language', y='count')
# st.write(alt.Chart(language_data[:20], width=800, height=300).mark_bar().encode(
# x=alt.X('Язык', sort=None),
# y='Число репозиториев',
# ))

bar_chart = alt.Chart(language_data[:20], width=800, height=300).mark_bar().encode(
    x=alt.X('Язык', sort=None),
    y='Число репозиториев',
)
st.altair_chart(bar_chart, use_container_width=True)

st.markdown('## 20 языков, имеющих наибольшее количество звезд')
language_data = pd.read_csv(path + '/star_language_count.csv',
                            names=['Язык', 'Число звезд'])
# st.bar_chart(language_data[:20], x='language', y='count')
bar_chart = alt.Chart(language_data[:20], width=800, height=300).mark_bar().encode(
    x=alt.X('Язык', sort=None),
    y='Число звезд',
)
st.altair_chart(bar_chart, use_container_width=True)
