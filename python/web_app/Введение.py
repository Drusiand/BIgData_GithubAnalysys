import streamlit as st
import sys
from PIL import Image

st.set_page_config(
    page_title="Введение",
)

st.markdown('# Анализ github-репозиториев\n'
            'В данном приложении отображены результаты исследования репозиториев, опубликованных на github. Для анализа'
            ' были отобраны репозитории, созданные с 2010 года по 26 ноября 2022 года и заработавшие 5 и более звезд (звезды'
            ' оставляют пользователи дабы показать свою симпатию к проекту).')

print(sys.argv)

image = Image.open('/python/web_app/GitHub_logo.webp')

st.image(image, caption='Sunrise by the mountains')
