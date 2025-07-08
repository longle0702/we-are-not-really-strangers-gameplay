import pandas as pd
import streamlit as st
lvwc = pd.read_csv('lvwc.csv')
st.title("🎲 We Are Not Really Strangers")
if st.button("Get a Random Question"):
    sample = lvwc.sample(n=1)
    for _, row in sample.iterrows():
        st.markdown(f"**{row['Source']}**: {row['Questions']}")
