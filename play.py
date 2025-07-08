import pandas as pd
import streamlit as st

st.set_page_config(page_title="We Are Not Really Strangers", page_icon="💬", layout="centered")
st.markdown("<h1 style='text-align: center; color: #e63946;'>🎲 We Are Not Really Strangers</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Pick your level, then click to reveal a random question.</p>", unsafe_allow_html=True)
st.markdown("###")

level_options = {
    "Level 1 💬 (Surface)": "1wc.csv",
    "Level 2 💭 (Personal)": "2wc.csv",
    "Level 3 ❤️ (Deep)": "3wc.csv",
    "Wildcard 🎴 (All Cards)": "Full.csv"
}

selected_level = st.selectbox("Choose your level:", list(level_options.keys()))

@st.cache_data
def load_questions(file):
    return pd.read_csv(file)

df = load_questions(level_options[selected_level])
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("💥 Reveal Question"):
        sample = df.sample(n=1)
        for _, row in sample.iterrows():
            st.markdown("---")
            st.markdown(f"<div style='font-size: 24px; color: #00f5d4; font-weight: bold;'>{row['Source']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size: 30px; color: #ffd166; font-weight: bold;'>❝ {row['Questions']} ❞</div>", unsafe_allow_html=True)
            st.markdown("---")
