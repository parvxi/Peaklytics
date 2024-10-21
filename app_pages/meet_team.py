import streamlit as st
from PIL import Image
import base64
from nav_bar import render_navbar


st.set_page_config(page_title="Meet Our Team", page_icon=":wave:", layout="wide")


render_navbar()

st.markdown(f"""
    <style>
        html, body {{
            height: 100%;
            background: rgb(25,30,41);
            background: linear-gradient(205deg, rgba(25,30,41,1) 17%, rgba(19,45,70,1) 48%, rgba(1,195,141,1) 100%, rgba(1,195,141,1) 100%);
            color: #191E29;
            font-family: 'Poppins', sans-serif;
            margin: 0;
            padding: 0;
        }}
        [data-testid="stApp"] {{
            background: transparent;
            display: flex;
            justify-content: center;
            width: 100%;
        }}
        .card-container {{
            display: flex;
            justify-content: center;  /* Centers the cards horizontally */
            flex-wrap: wrap;  /* Allows wrapping of cards if the screen is too small */
            gap: 10px;  /* Adds space between the cards */
            margin-top: 30px;
        }}
        .card {{
            width: 250px;
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
        .card:hover {{
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
        .card:hover .card__content {{
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
        img {{
            width: 100px;
            height: 100px;
            object-fit: cover;
            border-radius: 50%;
            border: 3px solid #01C38D;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }}
    </style>
""", unsafe_allow_html=True)

# Function to convert image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")


team_members = [
    {
        "name": "Sabah Baothman",
        "role": "Computer scientist",
        "image": f"data:image/svg+xml;base64,{image_to_base64('/Users/SHAD/code/Parvxi/Peaklytics/app_pages/images/1.svg')}",
        "linkedin": "https://linkedin.com/in/Sabah",
        "description": "Sabah leads the creative efforts at the Peaklytics, overseeing model development and branding."
    },
    {
        "name": "Shahad Hatim",
        "role": "Team leader",
        "image": f"data:image/svg+xml;base64,{image_to_base64('/Users/SHAD/code/Parvxi/Peaklytics/app_pages/images/2.svg')}",
        "linkedin": "https://linkedin.com/in/shahadhatim",
        "description": "Shahad ensures the smooth running of day-to-day operations and manages our key projects."
    },
    {
        "name": "Joud Alharbi",
        "role": "Community Manager",
        "image": f"data:image/svg+xml;base64,{image_to_base64('/Users/SHAD/code/Parvxi/Peaklytics/app_pages/images/3.svg')}",
        "linkedin": "https://linkedin.com/in/joudalharbi",
        "description": "Joud is the voice of our community, ensuring that users are heard and engaged."
    },
    {
        "name": "Somayah",
        "role": "Statician",
        "image": f"data:image/svg+xml;base64,{image_to_base64('/Users/SHAD/code/Parvxi/Peaklytics/app_pages/images/4.svg')}",
        "linkedin": "https://linkedin.com/in/somayah",
        "description": "Somayah drives our technological strategy, ensuring we remain at the forefront of innovation."
    }
]


st.markdown(f'<div class="card-container">', unsafe_allow_html=True)


for member in team_members:
    st.markdown(f"""
    <div class="card">
        <img src="{member['image']}" alt="{member['name']}">
        <div class="card__content">
            <p class="card__title">{member['name']}</p>
            <p class="card__description">{member['description']}</p>
            <a href="{member['linkedin']}" class="linkedin-button" target="_blank">LinkedIn Profile</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown(f'</div>', unsafe_allow_html=True)
