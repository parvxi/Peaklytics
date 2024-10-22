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
                padding: 1.5rem;
                color: white;
                background-color: #191E29;
                border-bottom: 1px solid #01C38D;
                width: 100%; /* Full width */
                position: fixed;
                top: 0;
                left: 0;
                z-index: 1000;
                box-sizing: border-box;
            }}
            .header h1 {{
                margin: 0;
                font-size: 1.5rem;
                color: #ffffff;
                padding-left: 1rem;
                padding-top: 3rem;

            }}
            .nav-links {{
                display: flex;
                gap: 2rem;
                padding-right: 1rem;
            }}
            .nav-links a {{
                padding-top: 3rem;
                text-decoration: none;
                color: #01C38D;
                font-weight: bold;
                font-size: 1.2rem;
            }}
            .nav-links a:hover {{
                text-decoration: underline;
            }}

            /* Ensure the content below the navbar is not hidden */
            .main-content {{
                margin-top: 80px;
            }}
            /* Ensure the content below the navbar is not hidden */
            .main-content {{
                margin-top: 80px; /* Reduce the space below navbar */
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
        <div class="main-content">
        </div>
    """, unsafe_allow_html=True)

def navigate_to(page):
    st.experimental_set_query_params(page=page)


render_navbar()
