import pandas as pd
import streamlit as st
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    st.write(pd.read_csv(uploaded_file))