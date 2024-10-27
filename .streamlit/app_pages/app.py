import streamlit as st
from main_page import main_page
from form_page import form_page
from loading_page import loading_page
from results import result_page
from nav_bar import render_navbar

# Initialize session state for the page if not already set
if 'page' not in st.session_state:
    # Retrieve the query parameter to handle navigation
    params = st.query_params
    if params.get("page", [""])[0] == "results":
        st.session_state.page = 'results'
    else:
        st.session_state.page = 'main'


render_navbar()

# Control navigation based on the current page in session state
if st.session_state.page == 'main':
    main_page()
elif st.session_state.page == 'form':
    form_page()
elif st.session_state.page == 'loading':
    loading_page()
elif st.session_state.page == 'results':
    result_page()  # Navigate to the result page
