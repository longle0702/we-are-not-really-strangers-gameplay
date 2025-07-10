import pandas as pd
import streamlit as st
import base64
import time

st.set_page_config(
    page_title="We Are Not Really Strangers", 
    page_icon="💬", 
    layout="centered"
)

st.markdown("""
    <style>
    body, .stApp {
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
        animation: popInOut 0.5s ease-in, fadeOut 0.5s ease-out 4.5s forwards;
    }
    @keyframes fadeOut {
        to { opacity: 0; }
    }
    @keyframes popInOut {
        0% { transform: scale(0); opacity: 0; }
        50% { transform: scale(1.1); opacity: 1; }
        100% { transform: scale(1); }
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
def load_questions(file_path):
    return pd.read_csv(file_path)

df = load_questions(level_options[selected_level])

if "wow_clicks" not in st.session_state:
    st.session_state.wow_clicks = 0

clicked = st.button("💥 Reveal Question", key=f"btn_{st.session_state.wow_clicks}")

if clicked:
    st.session_state.wow_clicks += 1
    sample = df.sample(n=1).iloc[0]
    
    st.markdown("---")
    st.markdown(f"<div style='font-size: 24px; color: #00f5d4; font-weight: bold;'>{sample['Source']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-size: 30px; color: white; font-weight: bold;'>❝ {sample['Questions']} ❞</div>", unsafe_allow_html=True)
    st.markdown("---")

    def get_base64_of_image(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    image_base64 = get_base64_of_image("wow.png")
    st.markdown(
        f"""
        <div id="wow-container">
            <img src="data:image/png;base64,{image_base64}" width="200">
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
