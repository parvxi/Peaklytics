import streamlit as st
from PIL import Image
import base64

# st.set_page_config(page_title="Meet Our Team", page_icon=":wave:", layout="wide")

# Function to convert image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# Function to render the "Meet Our Team" section
def meet_team():
    st.markdown(f"""
        <style>
             .team-container {{
                 padding : 30px;
                 display: flex;
                justify-content: center;

                 }}
            .card-container {{
                background: rgb(25,30,41);
                background: linear-gradient(205deg, rgba(25,30,41,1) 17%, rgba(19,45,70,1) 48%, rgba(1,195,141,1) 100%, rgba(1,195,141,1) 100%);
                border: 1px solid rgb(25,30,41);
                border-radius: 10px;
                width: 80rem;
                padding : 40px;

            }}
            .card1, .card2, .card3, .card4 {{
                width: 350px;
                height: 250px;
                background-color: #f2f2f2;
                border-radius: 10px;
                display: flex;
                align-items: center;
                justify-content: center;
                overflow: hidden;
                perspective: 1000px;
                transition: all 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
                margin: 20px;
            }}
            .card1:hover, .card2:hover, .card3:hover, .card4:hover {{
                transform: scale(1.05);
                box-shadow: 0 8px 16px #000000;
                background-color: #f2f2f2;
                color: #ffffff;
            }}
            .card__content {{
                color: #000000;
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                padding: 20px;
                box-sizing: border-box;
                background-color: #f2f2f2;
                transform: rotateX(-90deg);
                transform-origin: bottom;
                transition: all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            }}
            .card1:hover .card__content,
            .card2:hover .card__content,
            .card3:hover .card__content,
            .card4:hover .card__content{{
                transform: rotateX(0deg);
            }}
            .card__title {{
                margin: 0;
                font-size: 24px;
                color: #000000;
                font-weight: 700;
            }}
            .card__description {{
                margin: 10px 0 0;
                font-size: 14px;
                color: #000000;
                line-height: 1.4;
            }}
            .profile-image {{
                width: 100px;
                height: 100px;
                object-fit: cover;
                border-radius: 50%;
                border: 3px solid #01C38D;
                box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            }}
            .team-heading {{
                text-align: center;
                font-family: 'Roboto', sans-serif;
                font-size: 25px;
                padding-bottom: 20px;
                color: #f0f0f0;
            }}
        </style>
    """, unsafe_allow_html=True)

    # Team member cards
    st.markdown(
        f"""
        <div class="team-container">
        <div class="card-container">
        <h4 class="team-heading">👩‍💻 Meet Our Amazing Team 👩‍💻</h4>
        <div style="display: flex; justify-content: space-between;">
            <div class="card1">
                <img class="profile-image" src="data:image/svg+xml;base64,{image_to_base64('/Users/SHAD/code/Parvxi/Peaklytics/app_pages/images/1.svg')}" alt="Sabah Baothman">
                <div class="card__content">
                    <p class="card__title">Sabah Baothman</p>
                    <p class="card__description">Sabah leads the creative efforts at Peaklytics, overseeing model development and branding.</p>
                    <a href="https://linkedin.com/in/Sabah" class="linkedin-button" target="_blank">LinkedIn Profile</a>
                </div>
            </div>
            <div class="card2">
                <img class="profile-image" src="data:image/svg+xml;base64,{image_to_base64('/Users/SHAD/code/Parvxi/Peaklytics/app_pages/images/2.svg')}" alt="Shahad Hatim">
                <div class="card__content">
                    <p class="card__title">Shahad Hatim</p>
                    <p class="card__description">Shahad ensures the smooth running of day-to-day operations and manages our key projects.</p>
                    <a href="https://linkedin.com/in/shahadhatim" class="linkedin-button" target="_blank">LinkedIn Profile</a>
                </div>
            </div>
            <div class="card3">
                <img class="profile-image" src="data:image/svg+xml;base64,{image_to_base64('/Users/SHAD/code/Parvxi/Peaklytics/app_pages/images/3.svg')}" alt="Joud Alharbi">
                <div class="card__content">
                    <p class="card__title">Joud Alharbi</p>
                    <p class="card__description">Joud is the voice of our community, ensuring that users are heard and engaged.</p>
                    <a href="https://linkedin.com/in/joudalharbi" class="linkedin-button" target="_blank">LinkedIn Profile</a>
                </div>
            </div>
            <div class="card4">
                <img class="profile-image" src="data:image/svg+xml;base64,{image_to_base64('/Users/SHAD/code/Parvxi/Peaklytics/app_pages/images/4.svg')}" alt="Somayah">
                <div class="card__content">
                    <p class="card__title">Somayah</p>
                    <p class="card__description">Somayah drives our technological strategy, ensuring we remain at the forefront of innovation.</p>
                    <a href="https://linkedin.com/in/somayah" class="linkedin-button" target="_blank">LinkedIn Profile</a>
                </div>
            </div>
        </div>
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )
