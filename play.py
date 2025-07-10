import pandas as pd
import streamlit as st
import time

st.set_page_config(page_title="We Are Not Really Strangers", page_icon="💬", layout="centered")
st.markdown("""
    <style>
    body {
        background-color: black;
        color: white;
    }
    .stApp {
        background-color: black;
        color: white;
    }
    .css-18e3th9, .css-1d391kg, .css-1cpxqw2, .css-1v0mbdj {
        background-color: black !important;
        color: white !important;
    }
    #wow-container {
        position: fixed;
        top: 10%;
        right: 5%;
        z-index: 9999;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #e63946;'>🎲 We Are Not Really Strangers</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Pick your level, then click to reveal a random question.</p>", unsafe_allow_html=True)
st.markdown("###")

level_options = {
    "Level 1 💬 (Surface)": "1wc.csv",
    "Level 2 💭 (Personal)": "2wc.csv",
    "Level 3 ❤️ (Deep)": "3wc.csv",
    "All levels 🎴 (All Cards)": "Full.csv"
}

selected_level = st.selectbox("Choose your level:", list(level_options.keys()))

@st.cache_data
def load_questions(file):
    return pd.read_csv(file)

df = load_questions(level_options[selected_level])

if "show_wow" not in st.session_state:
    st.session_state.show_wow = False

if st.button("💥 Reveal Question"):
    st.session_state.show_wow = True 
    sample = df.sample(n=1)
    for _, row in sample.iterrows():
        st.markdown("---")
        st.markdown(f"<div style='font-size: 24px; color: #00f5d4; font-weight: bold;'>{row['Source']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='font-size: 30px; color: white; font-weight: bold;'>❝ {row['Questions']} ❞</div>", unsafe_allow_html=True)
        st.markdown("---")

if st.session_state.show_wow:
    st.markdown(
        f"""
        <div id="wow-container">
            <img src="wow.png" width="200">
        </div>
        <script>
            setTimeout(() => {{
                const el = document.getElementById("wow-container");
                if (el) {{
                    el.remove();
                }}
            }}, 5000);
        </script>
        """,
        unsafe_allow_html=True
    )
    st.session_state.show_wow = False
