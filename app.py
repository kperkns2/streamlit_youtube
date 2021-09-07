# https://share.streamlit.io/kperkns2/streamlit_youtube/main/app.py

# Create a streamlit dashboard which shows displays youtube videos (thumbnail, title, number of views)

# pd.columns = ['videoId', 'numberOfLikes', 'numberOfDislikes', 'numberOfComments',
#       'videoDuration', 'videoCategory', 'videoTags', 'title', 'channel_title',
#       'description', 'publishTime', 'channel_id', 'url', 'thumbnails']

import pandas as pd
import streamlit as st
# import altair as alt
import numpy as np
# import pydeck as pdk
# import plotly.express as px
# import plotly.graph_objects as go
# import matplotlib.pyplot as plt


@st.cache
def load_data():
     return pd.read_csv('traeger.csv')


df = load_data()

# Show a thumbnail, title and number of views together


def show_thumbnail_title_views(df):
    st.write(
        f'<div style="background-color:tomato;"><p style="color:white;font-size:50px;">{df.iloc[0]["title"]}</p></div>', unsafe_allow_html=True)
    st.image(df.iloc[0]['thumbnails'], use_column_width=True)
    st.write(f'<p style="font-size:20px;">{df.iloc[0]["numberOfViews"]} views</p>', unsafe_allow_html=True)
