import streamlit as st
from main_page import main_page
from form_page import form_page
from loading_page import loading_page
from nav_bar import render_navbar

# Switch between pages based on session state
if 'page' not in st.session_state:
    st.session_state.page = 'main'

# Call navbar for all pages
render_navbar()

# Handle page navigation
if st.session_state.page == 'main':
    main_page()
elif st.session_state.page == 'form':
    form_page()
elif st.session_state.page == 'loading':
    loading_page()
