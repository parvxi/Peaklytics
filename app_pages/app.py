import streamlit as st
import base64
from streamlit_lottie import st_lottie
import json

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Func to load Lottie animation from JSON file
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Main Page
def page1():
    image_base64 = get_base64_image("../Peaklytics/app_pages/images/main_page.png")

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

    # button to transition to the next page
    if st.button("Try it now"):
        st.session_state.page = "form"

# Second Page
def page2():
    st.markdown("<h1 style='text-align: center;'>Start Now</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Enter your company info</h3>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        market = st.text_input("Market")
        funding_total = st.number_input("Funding Total (USD)", min_value=0)
        city = st.text_input("City")

    with col2:
        company_age = st.number_input("Company Age", min_value=0)
        funding_rounds = st.number_input("Funding Rounds", min_value=0)
        funding_category = st.text_input("Funding Category")

    advanced = st.checkbox("Advanced", value=False)

    if advanced:
        st.text("Advanced options selected")

    st.subheader("Opt-in")
    optin1 = st.checkbox("All other inputs")
    optin2 = st.checkbox("....")
    optin3 = st.checkbox(".....")

    if st.button("Try it"):
        st.session_state.page = "loading"

# Third Page
def page3():
    st.markdown("<h1 style='text-align: center;'>Work in Progress</h1>", unsafe_allow_html=True)
    lottie_animation = load_lottiefile("/home/smy154/code/parvxi/Peaklytics/app_pages/images/1729425524995.json")
    st_lottie(lottie_animation, height=400, key="loading")

# Switch between pages based on session state
if 'page' not in st.session_state:
    st.session_state.page = 'main'

if st.session_state.page == 'main':
    page1()
elif st.session_state.page == 'form':
    page2()
elif st.session_state.page == 'loading':
    page3()
