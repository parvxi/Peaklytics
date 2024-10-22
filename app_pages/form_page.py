import streamlit as st
import requests
from option import markets,cities, regions, countries,funding_cat # Import the options


# Set custom styles for background color, font size, and font family
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f0f0;  /* Set background color for the entire app */
    }
    h1 {
        font-family: 'Roboto', sans-serif;
        font-size: 35px;  /* Set font size for h1 */
        color: #56c1ca;  /* Set color for h1 */
        text-align: center;
        margin-bottom: 0px;
        margin-top: 10px;
    }
    h3 {
        font-family: 'Roboto', sans-serif;
        font-size: 15px;  /* Set font size for h3 */
        color: #1e1e49;  /* Set color for h3 */
        text-align: center;
        margin-bottom: 40px;
    }

    .styled-title {
        font-family: 'Roboto', sans-serif;
        font-size: 20px;  /* Adjust the font size */
        color: #1e1e49;  /* Set the text color */
        font-weight: bold;  /* Make the text bold */
        margin-bottom: 19px;
    }

    label {
        font-family: 'Roboto', sans-serif !important;
        color: #1e1e49 !important;
        font-weight: bold !important;
    }

    /* Flexbox container for checkbox and label on the same line */
    .checkbox-container {
        display: flex;
        align-items: center;
    }

    .checkbox-container input[type="checkbox"] {
        margin-top : 10px !important;
        margin-right: -2px;  /* Space between checkbox and label */
        transform: scale(1.2);  /* Optional: Make the checkbox slightly bigger */
    }

    .checkbox-label {
        font-family: 'Roboto', sans-serif;
        margin-top : 10px !important;
        font-size: 14px;
        color: #1e1e49;  /* Set text color to black */
        font-weight: bold;
    }

    /* Style for button */
    .stButton > button {
        background-color: #56c1ca;  /* Background color */
        color: white;  /* Text color */
        font-size: 18px;  /* Font size */
        padding: 10px 35px;  /* Padding around the button */
        border-radius: 10px;  /* Rounded corners */
        border: none;  /* Remove border */
        cursor: pointer;  /* Pointer cursor on hover */
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-top: 20px
    }
    .stButton > button:hover {
        background-color: #1e1e49;  /* Darker background on hover */
        color: white;  /* Text color on hover */
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Function definition
def form_page():
    st.markdown("<h1 style='text-align: center;'>🚀 Ready to Get Started?</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Tell us more about your company to unlock personalized advice and predict  <br> your future success!</h3>", unsafe_allow_html=True)

    # Title for basic information with emoji
    st.markdown('<p class="styled-title">📝 Basic information to get started:</p>', unsafe_allow_html=True)

    # Add space between columns by creating an additional spacer column
    col1, spacer, col2 = st.columns([1, 0.1, 1])  # Adjust the middle number (0.2) for more or less space

    with col1:
        market = st.selectbox("Market", markets)
        funding_total = st.number_input("Funding Total (USD)", min_value=0)
        funding_category = st.selectbox("Funding Category", funding_cat)
        country = st.selectbox("Country", countries)

    with col2:
        company_age = st.number_input("Company Age", min_value=0)
        funding_rounds = st.number_input("Funding Rounds", min_value=0)
        city = st.selectbox("City", cities)
        region = st.selectbox("Region", regions)

    # --------------------------------------------------------------------

        # Track the state of the checkbox
    # Track the state of the checkbox
    if "show_details" not in st.session_state:
        st.session_state.show_details = False

    # Use columns to ensure checkbox and label are on the same line
    col1, col2 = st.columns([0.05, 1])  # Adjust the widths as needed

    with col1:
        # Provide a non-empty label and hide it using `label_visibility="hidden"`
        show_details = st.checkbox(" ", label_visibility="hidden")

    with col2:
        st.markdown('<label class="checkbox-label">🔍 Show additional details</label>', unsafe_allow_html=True)

#------------------------------------------------------------------------------------------------
    st.session_state.show_details = show_details
#------------------------------------------------------------------------------------------------

    # Conditional content
    if st.session_state.show_details:
        # Title for additional details with custom style and emoji
        st.markdown('<p class="styled-title">⚙️ Additional details for a more personalized experience:</p>', unsafe_allow_html=True)

        # Add space between columns by creating an additional spacer column
        col3, spacer, col4 = st.columns([1, 0.1, 1])  # Adjust the middle number for more or less space

        with col3:
            seed = st.number_input("Seed (USD)", min_value=0)
            venture = st.number_input("Venture (USD)", min_value=0)
            equity_crowdfunding = st.number_input("Equity Crowdfunding (USD)", min_value=0)
            undisclosed = st.number_input("Undisclosed (USD)", min_value=0)
            convertible_note = st.number_input("Convertible Note (USD)", min_value=0)
            angel = st.number_input("Angel (USD)", min_value=0)

        with col4:
            grant = st.number_input("Grant (USD)", min_value=0)
            private_equity = st.number_input("Private Equity (USD)", min_value=0)
            post_ipo_equity = st.number_input("Post IPO Equity (USD)", min_value=0)
            post_ipo_debt = st.number_input("Post IPO Debt (USD)", min_value=0)
            secondary_market = st.number_input("Secondary Market (USD)", min_value=0)
            product_crowdfunding = st.number_input("Product Crowdfunding (USD)", min_value=0)

        # Add a second row of columns for funding rounds and market category
        col5, spacer, col6 = st.columns([1, 0.1, 1])

        with col5:
            round_A = st.number_input("Round A (USD)", min_value=0)
            round_B = st.number_input("Round B (USD)", min_value=0)
            round_C = st.number_input("Round C (USD)", min_value=0)

        with col6:
            round_D = st.number_input("Round D (USD)", min_value=0)
            round_E = st.number_input("Round E (USD)", min_value=0)
            round_F = st.number_input("Round F (USD)", min_value=0)




    st.markdown('<div class="button-container">', unsafe_allow_html=True)


    if st.button("Click for the Insight"):
        # Collect form data into a dictionary
        params = {
            "market": market,
            "funding_total_usd": funding_total,
            "funding_category": funding_category,
            "country": country,
            "company_age": company_age,
            "funding_rounds": funding_rounds,
            "city": city,
            "region": region,
            "seed": seed if st.session_state.show_details else 0,
            "venture": venture if st.session_state.show_details else 0,
            "equity_crowdfunding": equity_crowdfunding if st.session_state.show_details else 0,
            "undisclosed": undisclosed if st.session_state.show_details else 0,
            "convertible_note": convertible_note if st.session_state.show_details else 0,
            "angel": angel if st.session_state.show_details else 0,
            "grant": grant if st.session_state.show_details else 0,
            "private_equity": private_equity if st.session_state.show_details else 0,
            "post_ipo_equity": post_ipo_equity if st.session_state.show_details else 0,
            "post_ipo_debt": post_ipo_debt if st.session_state.show_details else 0,
            "secondary_market": secondary_market if st.session_state.show_details else 0,
            "product_crowdfunding": product_crowdfunding if st.session_state.show_details else 0,
            "round_A": round_A if st.session_state.show_details else 0,
            "round_B": round_B if st.session_state.show_details else 0,
            "round_C": round_C if st.session_state.show_details else 0,
            "round_D": round_D if st.session_state.show_details else 0,
            "round_E": round_E if st.session_state.show_details else 0,
            "round_F": round_F if st.session_state.show_details else 0,
        }

        # Store form data in session state to use in the loading page
        st.session_state.params = params

        # Move to loading page
        st.session_state.page = "loading"
