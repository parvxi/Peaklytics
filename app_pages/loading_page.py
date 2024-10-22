import streamlit as st
from streamlit_lottie import st_lottie
from utils import load_lottiefile

def loading_page():
    st.markdown("<h1 style='text-align: center;'>Work in Progress</h1>", unsafe_allow_html=True)
    lottie_animation = load_lottiefile("images/1729425524995.json")
    st_lottie(lottie_animation, height=400, key="loading")
