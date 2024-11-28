import streamlit as st
import pandas as pd

st.write(
# My first app
print ("Hello *world!*")
)

df = pd.read_csv("iris.csv")
st.line_chart(df)