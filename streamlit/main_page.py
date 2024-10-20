import streamlit as st

# Set the page background color to white and add padding
st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
        font-family: 'Roboto', sans-serif;  /* Applying custom font */
        padding: 0px;  /* Remove padding from the entire app */
        justify-content: center;  /* Center the main container */

    }

    .main-container {
        padding: 50px 50px 50px 50px;  /* Add padding to the main container */
        background-color: white;
        border-radius: 10px;  /* Optional: Rounded corners */
    }

    h1 {
        color: #1e1e49;
        font-family: 'Roboto', sans-serif;
        font-size: 40px;
    }

    h2 {
        color: #1e1e49;
        font-family: 'Roboto', sans-serif;
        font-size: 20px;
    }

    /* Styling the button */
    .stButton > button {
        background-color: #1e1e49;
        color: white;
        padding: 10px 40px;
        font-size: 20px;
        border-radius: 10px;
        border: none;
        cursor: pointer;
    }

    /* Button hover effect */
    .stButton > button:hover {
        background-color: #56c1ca;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add a container with padding and optional border
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Divide the container into two columns
left, spacer, right = st.columns([4, 0.2, 1])  # Adjust the spacer width as needed

# Left container: Title, Subtitle, and Button
with left:
    st.markdown("<h1>Welcome to Peaklytick !</h1>", unsafe_allow_html=True)
    st.markdown("<h2>Helping companies predict their success and providing tailored advice.</h2>", unsafe_allow_html=True)
    st.button("Click Me!")

# Right container: Image (using st.image without Image.open)
with right:
    st.image("images/main_page.png", width=350)  # Replace with your image path

st.markdown('</div>', unsafe_allow_html=True)
