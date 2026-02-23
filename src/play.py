import pandas as pd
import streamlit as st

st.set_page_config(page_title="We Are Not Really Strangers", page_icon="💬", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #1e1e1e, #121212);
        color: white;
    }
    html, body, [class*="css"] {
        color: white;
        background-color: transparent;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: #e63946;'>🎲 We Are Not Really Strangers</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Pick your level, then click to reveal a random question.</p>", unsafe_allow_html=True)
st.markdown("###")

level_options = {
    "Level 1 💬 (Surface)": "questions/1wc.csv",
    "Level 2 💭 (Personal)": "questions/2wc.csv",
    "Level 3 ❤️ (Deep)": "questions/3wc.csv",
    "All levels 🎴 (All Cards)": "questions/Full.csv"
}

selected_level = st.selectbox("Choose your level:", list(level_options.keys()))

@st.cache_data
def load_questions(file):
    return pd.read_csv(file)

df = load_questions(level_options[selected_level])

if "used_indices" not in st.session_state:
    st.session_state.used_indices = {}
if selected_level not in st.session_state.used_indices:
    st.session_state.used_indices[selected_level] = set()

if st.button("💥 Reveal Question"):
    used = st.session_state.used_indices[selected_level]
    remaining_indices = list(set(df.index) - used)

    if not remaining_indices:
        st.markdown(
            "<div style='color: #ff6b6b; font-size: 20px; font-weight: bold;'>"
            "⚠️ You've seen all the questions at this level! Try another level."
            "</div>",
            unsafe_allow_html=True
        )
    else:
        random_index = pd.Series(remaining_indices).sample(n=1).iloc[0]
        row = df.loc[random_index]
        used.add(random_index)  

        st.markdown("---")
        st.markdown(
            f"<div style='font-size: 24px; color: #00f5d4; font-weight: bold;'>{row['Source']}</div>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<div style='font-size: 30px; color: white; font-weight: bold;'>❝ {row['Questions']} ❞</div>",
            unsafe_allow_html=True
        )
        st.markdown("---")

if st.button("🔄 Reset this level"):
    st.session_state.used_indices[selected_level] = set()
    st.success("Questions have been reset for this level!")
