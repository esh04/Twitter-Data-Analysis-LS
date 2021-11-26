import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from functions import hashtags, hashtags_list

st.title("Twitter Data Visualisation")
st.markdown("The dashboard will visualize the different opinions of the citizens of India regarding what their National Language or Lingua Franca should be.")
# st.markdown("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, b")
st.sidebar.title("Visualization Selector")
st.sidebar.markdown("Select the Charts/Plots accordingly:")

df_m=pd.read_csv("./data/translated_data.csv")
df = pd.read_csv("./data/data.csv")

st.map(df_m)

st.sidebar.checkbox("Show Analysis by Language", True, key=1)
select = st.sidebar.selectbox('Select a Language', df["lang"].unique())

df = hashtags(df)

st.sidebar.checkbox("Show Analysis by Hashtags", True, key=1)

hashtagList = hashtags_list(df["hashtags"].explode().tolist())

select = st.sidebar.selectbox('Select a Hashtags', hashtagList)