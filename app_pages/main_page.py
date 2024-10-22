import streamlit as st
import base64
from utils import get_base64_image
from nav_bar import render_navbar
from meet_team import meet_team

def main_page():
    image_base64 = get_base64_image("images/main_page.png")

    st.markdown(
        """
    <style>
    html, body {
            height: 100%;
            background-color: #f0f0f0;  /* Body is now red */
            color: #191E29;
            font-family: 'Poppins', sans-serif;
            margin: 0;
            padding: 0;
        }
    [data-testid="stApp"] {
            background: transparent;
            display: flex;
            justify-content: center;
            width: 100%;
             }
    .custom-title {
        width: 150%;
        font-weight: bold;
        text-align: left;
        margin-bottom: 20px;
        margin-top: 80px;
        color: #01C38D;
        font-family: 'Roboto', sans-serif;
        font-size: 40px;
    }
    .custom-text {
        width: 150%;
        font-size: 18px;
        color: #1e1e49;
        font-family: 'Poppins', sans-serif;
        text-align: left;
        line-height: 1.9;
        margin-bottom: 30px;
    }
    .custom-button {
        background-color: #1e1e49;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 15px 50px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s ease;
        display: inline-block;
        text-align: center;
    }

    .custom-button:hover {
        background-color: #01C38D;
    }

     .stColumn {
        padding-left: 20px;
        padding-right: 20px;
    }
    .image-container {
        margin-left: -100px; /* Adjust this value to control how much the image moves to the left */
    }
    </style>
    """,
        unsafe_allow_html=True
    )



    col1, col2 = st.columns(2)

    with col1:
        # Use f-string to properly format the base64 image into HTML
        st.markdown(
            f"""
            <div class="image-container">
                <img src="data:image/png;base64,{image_base64}" width="350" alt="Right Image"/>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        # Use st.markdown with custom classes to style the title and text
        st.markdown('<div class="custom-title">Welcome to Peaklytics!</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="custom-text">Helping companies predict their success and providing tailored advice.</div>',
            unsafe_allow_html=True
        )

        if st.button("👉 Try it now"):
            st.session_state.page = "form"

    meet_team()
