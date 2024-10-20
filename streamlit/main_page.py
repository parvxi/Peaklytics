import streamlit as st
import base64

# Helper function to convert a local image to a base64 string
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Convert your local image to base64
image_base64 = get_base64_image("images/main_page.png")  # Replace with your local image path

# Set custom styles for the container
st.markdown(
    """
    <style>
        .stApp {
        background-color: white;
        font-family: 'Roboto', sans-serif;  /* Applying custom font */
        }
    .custom-container {
        padding-top: 50px;  /* Padding above the container */
        padding-left: 20px;
        padding-right: 20px;
        padding-bottom: 20px;
        border-radius: 10px;  /* Optional: Add some rounded corners */
        width: 143%;  /* Make the container 200% of the viewport width */
        max-width: none;  /* Disable max-width */
        margin-left: 50%;  /* Move it halfway from the left */
        transform: translateX(-50%);  /* Center it by translating half its width back */
        }
    .custom-div {
        padding-top: 100px;  /* Add padding to the div */
        border-radius: 10px;  /* Optional: Rounded corners */
    }
    h1 {
        color: #1e1e49;  /* Set text color to white for better contrast */
        font-family: 'Roboto', sans-serif;
        font-size: 40px;
    }
    h4 {
        color: #1e1e49;  /* Set text color to white for better contrast */
        font-family: 'Roboto', sans-serif;
        font-size: 20px;
    }
    .right-align {
        text-align: right;
    }
        /* Styling the button */
    .button {
        font-family: 'Roboto', sans-serif;  /* Applying custom font */
        background-color: #1e1e49;
        color: white;
        padding: 10px 40px;
        font-size: 20px;
        border-radius: 10px;
        border: none;
        cursor: pointer;
    }

    /* Button hover effect */
    .button:hover {
        background-color: #56c1ca;
        color: white;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Create the main container with red background and padding
st.markdown(
    f"""
    <div class="custom-container">
        <div style="display: flex; justify-content: space-between;">
            <div class="custom-div" style="flex: 1;">
                <h1>Welcome to Peaklytick !</h1>
                <h4>Helping companies predict their success and providing tailored advice.</h4>
                <button class="button">Try it now </button>  <!-- HTML Button inside the div -->
            </div>
            <div style="flex: 1; text-align: right;">
                <img src="data:image/png;base64,{image_base64}" width="350" alt="Right Image"/>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
