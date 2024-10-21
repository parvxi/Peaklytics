import streamlit as st
import base64
from utils import get_base64_image

def main_page():
    image_base64 = get_base64_image("images/main_page.png")

    st.markdown(
        """
        <style>
            .stApp {
            background-color: white;
            font-family: 'Roboto', sans-serif;
            }
        .custom-container {
            padding-top: 50px;
            padding-left: 20px;
            padding-right: 20px;
            padding-bottom: 20px;
            border-radius: 10px;
            width: 143%;
            max-width: none;
            margin-left: 50%;
            transform: translateX(-50%);
            }
        .custom-div {
            padding-top: 100px;
            border-radius: 10px;
        }
        h1 {
            color: #1e1e49;
            font-family: 'Roboto', sans-serif;
            font-size: 40px;
        }
        h4 {
            color: #1e1e49;
            font-family: 'Roboto', sans-serif;
            font-size: 20px;
        }
        .right-align {
            text-align: right;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="custom-container">
            <div style="display: flex; justify-content: space-between;">
                <div class="custom-div" style="flex: 1;">
                    <h1>Welcome to Peaklytick !</h1>
                    <h4>Helping companies predict their success and providing tailored advice.</h4>
                </div>
                <div style="flex: 1; text-align: right;">
                    <img src="data:image/png;base64,{image_base64}" width="350" alt="Right Image"/>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Try it now"):
        st.session_state.page = "form"
