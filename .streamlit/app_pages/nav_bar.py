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

    st.markdown("""
        <style>
            .header h1 {
                font-family: 'Arial', sans-serif;
                font-size: 28px; /* Smaller font size */
                color: #01C38D;
                text-transform: uppercase;
                text-align: center;
                letter-spacing: 2px;
                background: linear-gradient(90deg, #132D46, #01C38D);
                -webkit-background-clip: text;
                color: transparent;
            }
            .nav-links {
                text-align: center;
                margin-top: 10px;
            }
            .nav-links a {
                margin: 0 15px;
                text-decoration: none;
                color: #696E79;
                font-size: 18px;
            }
            .nav-links a:hover {
                color: #01C38D;
            }
        </style>
        <div class="header" data-testid="stHeader">
            <h1>Peaklytics</h1>
            <div class="nav-links">
                <a href="?page=/Users/SHAD/code/Parvxi/Peaklytics/app_pages/app.py">Home</a>
                <a href="?page=/Users/SHAD/code/Parvxi/Peaklytics/.streamlit/app_pages/form_page.py">Predict</a>
            </div>
        </div>
        <div class="main-content">
        </div>
    """, unsafe_allow_html=True)


def navigate_to(page):
    st.experimental_set_query_params(page=page)


render_navbar()
