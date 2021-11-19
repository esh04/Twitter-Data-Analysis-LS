import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt


st.title("Twitter Data Visualisation")
st.markdown("The dashboard will visualize the different opinions of the citizens of India regarding what their National Language or Lingua Franca should be.")
# st.markdown("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, b")
st.sidebar.title("Visualization Selector")
st.sidebar.markdown("Select the Charts/Plots accordingly:")



def load_data():
    data=pd.read_csv("translated_data.csv")
    return data

df=load_data()

st.map(df)

st.sidebar.checkbox("Show Analysis by Hashtags", True, key=1)
select = st.sidebar.selectbox('Select a Hashtag', ['#StopHindiImposition'])

st.sidebar.checkbox("Show Analysis by Region", True, key=1)
select = st.sidebar.selectbox('Select a Region', ['Banglore'])