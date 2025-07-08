import pandas as pd
import streamlit as st

lvwc = pd.read_csv('Full.csv')
st.set_page_config(page_title="We Are Not Really Strangers", page_icon="💬", layout="centered")
st.markdown("<h1 style='text-align: center; color: #e63946;'>🎲 We Are Not Really Strangers</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Click the button to reveal a random question and emotionally wreck your friends.</p>", unsafe_allow_html=True)
st.markdown("###")

col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("💥 Reveal Question"):
        sample = lvwc.sample(n=1)
        for _, row in sample.iterrows():
            st.markdown("---")
            st.markdown(f"<div style='font-size: 22px; color: #264653;'><b>{row['Source']}</b></div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size: 28px; color: #1d3557; font-weight: bold;'>❝ {row['Questions']} ❞</div>", unsafe_allow_html=True)
            st.markdown("---")
