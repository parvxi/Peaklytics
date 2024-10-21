import streamlit as st

def render_navbar():
    # Add Custom CSS for header styling
    st.markdown(f"""
        <style>
            /* Custom header styling */
            .header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 1rem;
                color: white;
                border-bottom: 1px solid #01C38D;
            }}
            .header h1 {{
                margin: -50px;
                font-size: 1rem;
                color: #ffffff;
            }}
            .nav-links {{
                display: flex;
                gap: 1rem;
            }}
            .nav-links a {{
                text-decoration: none;
                color: #01C38D;
                font-weight: bold;
                font-size: 1.2rem;
            }}
            .nav-links a:hover {{
                text-decoration: underline;
            }}
        </style>
    """, unsafe_allow_html=True)

    # Create header
    st.markdown("""
        <div class="header" data-testid="stHeader">
            <h1>My App</h1>
            <div class="nav-links">
                <a href="?page=/Users/SHAD/code/Parvxi/Peaklytics/app_pages/app.py">Home</a>
                <a href="?page=predict">Predict</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

def navigate_to(page):
    st.experimental_set_query_params(page=page)
