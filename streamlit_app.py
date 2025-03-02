# Commands to run:
# conda activate telegram_bot
# streamlit run Prospecta.py --server.maxUploadSize 2

import pandas as pd
import streamlit as st
import numpy as np

st.logo("logo.png", size="large")
st.set_page_config(layout="wide")
st.sidebar.title("Wellcome to PROSPECT")

col1, col2, col3 = st.columns([0.25, 0.25, 0.5])

uploaded_file = st.sidebar.file_uploader("Choose a file (NIR file)", type="csv")

model = st.sidebar.selectbox("Select a model", ["Decision Tree", "Logistic Regression"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    NIR_list = df.columns.to_list()
    option = st.sidebar.selectbox("Select the NIR source", [None] + NIR_list)

with col1:
    st.header("Sensor readings")
    if uploaded_file is not None:
        st.write(df)

with col2:
    st.header("Summary statistics")
    if uploaded_file is not None:
        st.write(df.describe())

with col3:
    st.header("Data analysis")

    with st.container():
        if uploaded_file is not None:
            model_output = "None"
            st.write("Classification result:" + model_output)

    with st.container():
        if uploaded_file is not None:
            if option in NIR_list:
                st.line_chart(df, y=option, x_label="Wavelength")
