import streamlit as st
import pandas as pd
import sys
import plotly.express as px

# print("counters", sys.argv)
path = sys.argv[1] if len(sys.argv) > 1 else "/pretty_csv"

st.set_page_config(
    page_title="Счётчики",
    layout='wide'
)

pages = ['Наличие обсуждений', 'Наличие скачиваний', 'Наличие issues', 'Наличие pages',
         'Ведение проекта (projects)', 'Наличие wiki']
tab_discussions, tab_downloads, tab_issues, tab_pages, tab_projects, tab_wiki = st.tabs(pages)

# with tab_fork:
# st.markdown('## Количество fork репозиториев')
# wiki_data = pd.read_csv(path + '/fork_count.csv',
# names=['Является ли репозиторий fork', 'Количество репозиториев'])

# st.bar_chart(wiki_data, x='Является ли репозиторий fork', y='Количество репозиториев')


with tab_discussions:
    cols = st.columns([2, 3])
    with cols[0]:
        st.markdown('### Статистика наличия обсуждения в репозитории')
        wiki_data = pd.read_csv(path + '/has_discussions_count.csv',
                                names=['Наличие обсуждения', 'Количество репозиториев'])

        st.bar_chart(wiki_data, x='Наличие обсуждения', y='Количество репозиториев')
    with cols[1]:
        star_discussions = pd.read_csv(path + '/star_has_discussions_count.csv',
                                       names=['Наличие обсуждения', 'Количество звезд'])
        st.markdown('### Количество звезд в зависимости от наличия обсуждений')
        fig = px.pie(star_discussions, values="Количество звезд", names='Наличие обсуждения',
                     height=350, width=250)
        fig.update_layout(margin=dict(l=10, r=10, t=50, b=0), font=dict(size=17))
        st.plotly_chart(fig, use_container_width=True)

with tab_downloads:
    cols = st.columns([2, 3])
    with cols[0]:
        st.markdown('### Статистика скачиваний')
        wiki_data = pd.read_csv(path + '/has_wiki_count.csv',
                                names=['Наличие скачиваний', 'Количество репозиториев'])

        st.bar_chart(wiki_data, x='Наличие скачиваний', y='Количество репозиториев')
    with cols[1]:
        star_downloads = pd.read_csv(path + '/star_has_downloads_count.csv',
                                     names=['Наличие скачиваний', 'Количество звезд'])
        st.markdown('### Количество звезд в зависимости от наличия скачиваний')
        fig = px.pie(star_downloads, values="Количество звезд", names='Наличие скачиваний',
                     height=350, width=250)
        fig.update_layout(margin=dict(l=10, r=10, t=50, b=0), font=dict(size=17))
        st.plotly_chart(fig, use_container_width=True)

with tab_issues:
    cols = st.columns([2, 3])
    with cols[0]:
        st.markdown('### Статистика использования issues')
        wiki_data = pd.read_csv(path + '/has_issues_count.csv',
                                names=['Наличие issues', 'Количество репозиториев'])

        st.bar_chart(wiki_data, x='Наличие issues', y='Количество репозиториев')
    with cols[1]:
        star_issues = pd.read_csv(path + '/star_has_issues_count.csv',
                                  names=['Наличие issues', 'Количество звезд'])
        st.markdown('### Количество звезд в зависимости от наличия issues')
        fig = px.pie(star_issues, values="Количество звезд", names='Наличие issues',
                     height=350, width=250)
        fig.update_layout(margin=dict(l=10, r=10, t=50, b=0), font=dict(size=17))
        st.plotly_chart(fig, use_container_width=True)

with tab_pages:
    cols = st.columns([2, 3])
    with cols[0]:
        st.markdown('### Статистика ведения документации посредством github.pages')
        wiki_data = pd.read_csv(path + '/has_pages_count.csv',
                                names=['Наличие pages', 'Количество репозиториев'])

        st.bar_chart(wiki_data, x='Наличие pages', y='Количество репозиториев')
    with cols[1]:
        star_pages = pd.read_csv(path + '/star_has_pages_count.csv',
                                 names=['Наличие pages', 'Количество звезд'])
        st.markdown('### Количество звезд в зависимости от наличия pages')
        fig = px.pie(star_pages, values="Количество звезд", names='Наличие pages',
                     height=350, width=250)
        fig.update_layout(margin=dict(l=10, r=10, t=50, b=0), font=dict(size=17))
        st.plotly_chart(fig, use_container_width=True)

with tab_projects:
    cols = st.columns([2, 3])
    with cols[0]:
        st.markdown('### Статистика ведения проекта (projects)')
        wiki_data = pd.read_csv(path + '/has_projects_count.csv',
                                names=['Наличие projects', 'Количество репозиториев'])

        st.bar_chart(wiki_data, x='Наличие projects', y='Количество репозиториев')
    with cols[1]:
        star_projects = pd.read_csv(path + '/star_has_projects_count.csv',
                                    names=['Наличие projects', 'Количество звезд'])
        st.markdown('### Количество звезд в зависимости от наличия projects')
        fig = px.pie(star_projects, values="Количество звезд", names='Наличие projects',
                     height=350, width=250)
        fig.update_layout(margin=dict(l=10, r=10, t=50, b=0), font=dict(size=17))
        st.plotly_chart(fig, use_container_width=True)

with tab_wiki:
    cols = st.columns([2, 3])
    with cols[0]:
        st.markdown('### Статистика использования встроенной вики')
        wiki_data = pd.read_csv(path + '/has_wiki_count.csv',
                                names=['Наличие вики', 'Количество репозиториев'])

        st.bar_chart(wiki_data, x='Наличие вики', y='Количество репозиториев')
    with cols[1]:
        star_wiki = pd.read_csv(path + '/star_has_wiki_count.csv',
                                names=['Наличие wiki', 'Количество звезд'])
        st.markdown('### Количество звезд в зависимости от наличия wiki')
        fig = px.pie(star_wiki, values="Количество звезд", names='Наличие wiki',
                     height=350, width=250)
        fig.update_layout(margin=dict(l=10, r=10, t=50, b=0), font=dict(size=17))
        st.plotly_chart(fig, use_container_width=True)
