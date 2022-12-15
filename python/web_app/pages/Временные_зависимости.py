import streamlit as st
import pandas as pd
import altair as alt
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "/pretty_csv"

st.set_page_config(
    page_title="Временные зависимости",
    layout='wide'
)

languages = pd.read_csv(path + '/language_count.csv',
                        names=['language', 'Количество'])

time_languages = pd.read_csv(path + '/time_language_count.csv',
                             names=['Дата', 'language', 'Количество'])

languages = languages['language']

option = st.selectbox('Язык программирования', languages)

st.markdown('### Ежедневно')

filtered = time_languages[time_languages.language == option]

filtered = filtered.drop('language', axis=1)
filtered['Дата'] = pd.to_datetime(filtered['Дата'], yearfirst=True)
st.bar_chart(filtered, x='Дата', y='Количество')

tmp = pd.DataFrame(filtered.groupby(pd.Grouper(key='Дата', freq='M'))['Количество'].sum())

st.markdown('### Ежемесячно')
st.bar_chart(tmp)
