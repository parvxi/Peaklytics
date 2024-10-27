import streamlit as st
import requests
from streamlit_lottie import st_lottie
from utils import load_lottiefile

def loading_page():
    st.markdown("<h1 style='text-align: center;'>Work in Progress</h1>", unsafe_allow_html=True)

    # Load and display the loading animation
    lottie_animation = load_lottiefile("/Users/SHAD/code/Parvxi/Peaklytics/.streamlit/app_pages/images/Animation - 1729605553725.json")
    st_lottie(lottie_animation, height=400, key="loading")

    # Check if we already have the form data in session state
    if "params" in st.session_state:
        params = st.session_state.params  # Get the form data

        # Debug: Check the form data being sent
        #st.write("Form Data being sent:", params)

        # Send the request to the API
        try:
            api_url = 'http://127.0.0.1:8000/predict'  # Update this to your actual API URL
            response = requests.post(api_url, json=params)

            if response.status_code == 200:
                #st.write("Storing API Response:", response.json())  # Debug: Check if response is 200
                st.session_state.results = response.json() # Store the result in session state
                st.session_state.page = 'results'
                # Force a rerun to trigger navigation to results page
                st.rerun()

        except requests.exceptions.RequestException as e:
            st.error(f"API request failed: {e}")
            st.session_state.page = "form"  # Go back to form page on request error
            st.rerun()  # Force rerun to handle page switch
    else:
        st.error("Form data not found. Please fill the form again.")
        st.session_state.page = "form"  # Navigate back to form if no data is found
        st.rerun()  # Force rerun to handle page switch
