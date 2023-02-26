import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

st.title("Employee Attrition Dashboard")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "ea.png")
DATA_PATH = os.path.join(dir_of_interest, "data", "Employee_Attrition.csv")


img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

species = st.selectbox("Attrition:", df['Attrition'].unique())

fig_1 = px.histogram(df[df['Attrition'] == species], x="BusinessTravel")
st.plotly_chart(fig_1, use_container_width=True)

fig_1 = px.histogram(df[df['Attrition'] == species], x="Gender")
st.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.histogram(df[df['Attrition'] == species], y="MaritalStatus")
st.plotly_chart(fig_2, use_container_width=True)

fig_2 = px.histogram(df[df['Attrition'] == species], y="JobRole")
st.plotly_chart(fig_2, use_container_width=True)

fig_2 = px.histogram(df[df['Attrition'] == species], y="Department")
st.plotly_chart(fig_2, use_container_width=True)
