import streamlit as st
import plotly.graph_objects as go

def result_page():


    st.markdown("""
        <style>
            html, body {
                height: 100%;
                background: rgb(255,255,255);
                background: -moz-linear-gradient(173deg, rgba(255,255,255,1) 0%, rgba(19,45,70,1) 0%, rgba(25,30,41,1) 0%, rgba(19,45,70,1) 5%, rgba(3,181,135,1) 100%);
                background: -webkit-linear-gradient(173deg, rgba(255,255,255,1) 0%, rgba(19,45,70,1) 0%, rgba(25,30,41,1) 0%, rgba(19,45,70,1) 5%, rgba(3,181,135,1) 100%);
                background: linear-gradient(173deg, rgba(255,255,255,1) 0%, rgba(19,45,70,1) 0%, rgba(25,30,41,1) 0%, rgba(19,45,70,1) 5%, rgba(3,181,135,1) 100%);
                filter: progid:DXImageTransform.Microsoft.gradient(startColorstr="#ffffff",endColorstr="#03b587",GradientType=1);
                color: #191E29;
                font-family: 'Poppins', sans-serif;
                margin: 0;
                padding: 0;
            }
            [data-testid="stApp"] {
                background: transparent;
                display: flex;
                justify-content: center;
                width: 100%;
            }
            .key-input-card {
                background-color: #f9f9f9;
                padding: 15px;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                margin-bottom: 10px;
                color: black;
            }
            .key-input-icon {
                font-size: 1.2em;
                margin-right: 10px;
                color: black;
            }
            .key-input {
                font-weight: bold;
                margin-bottom: 5px;
                color: black;
            }
            .key-input-card:hover {
                box-shadow: 0 6px 12px rgba(0,0,0,0.15);
            }
            .st-expander {
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                padding: 10px;
            }
            .center-text {
                text-align: center;
                color: #FFFFFF;
                font-size: 32px;
                margin-bottom: 20px;
                margin-top: -20px;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
            }
            .metric-card {
                background-color: #f9f9f9;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin-bottom: 15px;
                transition: transform 0.2s ease;
                color: black;
            }
            .metric-card:hover {
                transform: translateY(-3px);
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
            }
            .metric-icon {
                font-size: 1.2em;
                margin-right: 10px;
            }
            .metric-label {
                font-weight: bold;
                color: black;
            }
        </style>
    """, unsafe_allow_html=True)


    # Get the API response stored in session state
    response_body = st.session_state.get('results')

    # App Title
    st.markdown("""
        <style>
        body {
            color: #FFFFFF;
        }
        .peaklytics {
            color: #01C38D;
            text-shadow: 2px 2px 5px #132D46;
            padding: 5px;
        }
        </style>
        <h1 style='text-align: center;'>
            <span class='peaklytics'>Peaklytics</span>
            <span style='color: white;'>Prediction Results</span> 📊
        </h1>

    """, unsafe_allow_html=True)

    # Check if API response is available
    if response_body:
        # Accessing fields from response, with default values if missing
        prediction = response_body.get('prediction', 'Unknown')
        user_inputs = response_body.get('user_inputs', {})
        calculations = response_body.get('calculations', {})

        # Define the styles for success and failure cases
        if prediction.lower() == 'success':
            box_style = f"""
                <style>
                .box {{
                    box-sizing: border-box;
                    padding: 5px;
                    margin: 20px auto;
                    width: 100%;
                    max-width: 600px;
                    text-align: center;
                    background-color: #F0FFF4;
                    border: 2px solid #01C38D;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    color: #191E29;
                }}
                .box h4 {{
                    font-size: 24px;
                    margin: 20px;
                    color: #696E79;
                }}
                .box p {{
                    font-size: 28px;
                    margin-top: 20px;
                    color: #01C38D;
                }}
                </style>
                <div class="box" style="border: 1px solid #ddd; padding: 16px; border-radius: 8px; background-color: #f9f9f9; width: 100%; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);">
                <h4 style="margin-bottom: 8px; font-size: 1.2em; color: #132D46;">Company's Potential Outcome:</h4>
                <span style="display: block; font-size: 1.5em; font-weight: bold; color: #5CB85C;">
                    { response_body['prediction'].capitalize() }
                </span>
            </div>

            """
        else:
            box_style = f"""
                <style>
                .box {{
                    box-sizing: border-box;
                    padding: 5px;
                    margin: 20px auto;
                    width: 100%;
                    max-width: 600px;
                    text-align: center;
                    background-color: #FFF7F7;
                    border: 2px solid #FF4B4B;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    color: #191E29;
                }}
                .box h4 {{
                    font-size: 24px;
                    margin: 20px;
                    color: #696E79;
                }}
                .box p {{
                    font-size: 28px;
                    margin-top: 10px;
                    color: #FF4B4B;
                }}
                </style>
            <div class="box" style="border: 1px solid #ddd; padding: 16px; border-radius: 8px; background-color: #f9f9f9; width: 100%; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);">
                <h4 style="margin-bottom: 8px; font-size: 1.2em; color: #132D46;">Company's Potential Outcome:</h4>
                <span style="display: block; font-size: 1.5em; font-weight: bold; color: #CF3834;">
                    { response_body['prediction'].capitalize() }
                </span>
                <p style="margin-top: 12px; font-size: 0.85em; color: #696E79;">
                    Remember, this is an estimation, and with the right strategies, there are always opportunities for growth and improvement.
                </p>
            </div>

            """
        # Display the styled box
        st.components.v1.html(box_style, height=200)
        st.markdown("---")

        # Display Key User Inputs Section
        st.markdown("<h3 class='center-text'>Company Information</h3>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class='key-input-card'>
                <span class='key-input-icon'>🛍️</span> <span class='key-input'>Market:</span> {user_inputs.get('market', 'N/A')}
            </div>
            <div class='key-input-card'>
                <span class='key-input-icon'>📍</span> <span class='key-input'>Region:</span> {user_inputs.get('region', 'N/A')}
            </div>
            <div class='key-input-card'>
                <span class='key-input-icon'>🏙️</span> <span class='key-input'>City:</span> {user_inputs.get('city', 'N/A')}
            </div>
            <div class='key-input-card'>
                <span class='key-input-icon'>💵</span> <span class='key-input'>Total Funding (USD):</span> ${user_inputs.get('funding_total_usd', 'N/A')}
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class='key-input-card'>
                <span class='key-input-icon'>🔄</span> <span class='key-input'>Funding Rounds:</span> {user_inputs.get('funding_rounds', 'N/A')}
            </div>
            <div class='key-input-card'>
                <span class='key-input-icon'>📆</span> <span class='key-input'>Company Age:</span> {user_inputs.get('company_age', 'N/A')} years
            </div>
            <div class='key-input-card'>
                <span class='key-input-icon'>📊</span> <span class='key-input'>Funding Category:</span> {user_inputs.get('funding_category', 'N/A')}
            </div>
            """, unsafe_allow_html=True)

        # Expandable section for full user input details
        st.markdown("")
        st.markdown("---")

        with st.expander("Click here to view all input details"):
            # Custom CSS for large white font and table background
            st.markdown(
                """
                <style>
                .large-font {
                    font-size:20px !important;
                    color: white !important;
                }
                .custom-table thead tr th {
                    background-color: #333333 !important;
                    color: white !important;
                }
                .custom-table tbody tr td {
                    background-color: #444444 !important;
                    color: white !important;
                }
                .custom-table tbody tr td, .custom-table thead tr th {

                    border: 1px solid white !important; }
                </style>
                """, unsafe_allow_html=True
            )

            # Apply the large font and white color to the container
            st.markdown('<div class="large-font">Details:</div>', unsafe_allow_html=True)

            # Use the custom class for the table
            st.markdown('<div class="custom-table">', unsafe_allow_html=True)
            st.table({
                "Field": list(user_inputs.keys()),
                "Value": list(user_inputs.values())
            })
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("")
        st.markdown("")
        #-------------------------------------------------

        # Funding Breakdown Pie Chart


        # Let user select the chart type
        chart_type = st.selectbox("Choose chart type", ["Pie Chart", "Stacked Bar Chart"])

        funding_data = {
            'Type': ['Seed', 'Venture', 'Equity Crowdfunding', 'Convertible Note', 'Angel', 'Undisclosed', 'Grant', 'Private Equity'],
            'Amount': [
                user_inputs.get('seed', 0),
                user_inputs.get('venture', 0),
                user_inputs.get('equity_crowdfunding', 0),
                user_inputs.get('convertible_note', 0),
                user_inputs.get('angel', 0),
                user_inputs.get('undisclosed', 0),
                user_inputs.get('grant', 0),
                user_inputs.get('private_equity', 0)
            ]
        }

        # Filter out zero values for both chart types
        filtered_funding_data = {k: v for k, v in zip(funding_data['Type'], funding_data['Amount']) if v > 0}

        round_data = {
            'Rounds': ['Round A', 'Round B', 'Round C', 'Round D', 'Round E', 'Round F'],
            'Amounts': [
                user_inputs.get('round_A', 0),
                user_inputs.get('round_B', 0),
                user_inputs.get('round_C', 0),
                user_inputs.get('round_D', 0),
                user_inputs.get('round_E', 0),
                user_inputs.get('round_F', 0)
            ]
        }
        filtered_round_data = {k: v for k, v in zip(round_data['Rounds'], round_data['Amounts']) if v > 0}

        # Display chart based on user selection
        if chart_type == "Pie Chart":
            if filtered_funding_data:
                fig = go.Figure(go.Pie(
                    labels=list(filtered_funding_data.keys()),
                    values=list(filtered_funding_data.values()),
                    textinfo='label+percent',
                    textfont=dict(color='black')
                ))
                fig.update_layout(
                    plot_bgcolor='rgba(0, 0, 0, 0)',
                    paper_bgcolor='rgba(0, 0, 0, 0)'
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.write("No funding data available to display.")

        elif chart_type == "Stacked Bar Chart":
            if filtered_round_data:
                fig = go.Figure(go.Bar(
                    x=list(filtered_round_data.keys()),
                    y=list(filtered_round_data.values()),
                    marker=dict(color='lightblue'),
                    text=list(filtered_round_data.values()),
                    textposition='auto'
                ))
                fig.update_layout(
                    title="Funding per Round",
                    xaxis_title="Rounds",
                    yaxis_title="Funding Amount",
                    plot_bgcolor='rgba(0, 0, 0, 0)',
                    paper_bgcolor='rgba(0, 0, 0, 0)'
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.write("No funding round data available to display.")


#-------------------------------------
        # Financial Calculast.markdown("---"tions
        st.markdown("")
        st.markdown("")
        st.markdown("<h3 class='center-text'>Financial Calculations</h3>", unsafe_allow_html=True)

        col3, col4 = st.columns(2)
        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <span class="metric-icon">💸</span>
                <span class="metric-label">Average Funding Per Round:</span>
                <br> ${calculations.get('average_funding_per_round', 'N/A'):,}
            </div>
            <div class="metric-card">
                <span class="metric-icon">🌱</span>
                <span class="metric-label">Seed Funding %:</span>
                <br> {calculations.get('seed_funding_percentage', 'N/A')}%
            </div>
            """, unsafe_allow_html=True)

        with col4:
            burn_rate = calculations.get('burn_rate', 0)
            runway = calculations.get('runway', 0)

            burn_rate_color = "red" if burn_rate > 100000 else "green"
            runway_color = "green" if runway > 12 else "orange"

            st.markdown(f"""
            <div class="metric-card" style="border-left: 5px solid {burn_rate_color};">
                <span class="metric-icon">🔥</span>
                <span class="metric-label">Burn Rate:</span>
                <br> ${burn_rate:,}/month
            </div>
            <div class="metric-card" style="border-left: 5px solid {runway_color};">
                <span class="metric-icon">🛤️</span>
                <span class="metric-label">Runway:</span>
                <br> {runway} months
            </div>
            """, unsafe_allow_html=True)

        # LLM Insights
        st.markdown("")
        st.markdown("---")
        with st.expander("Click here to view LLM Insights"):
            llm_insights = response_body.get('llm_insights', 'No insights available.')
            st.markdown(f"""
                <div class="insight-box">
                    <div class="insight-title">LLM Insights  ❇️:</div>
                    <div>{llm_insights}</div>
                </div>
            """, unsafe_allow_html=True)

    else:
        st.error("No response from the API. Please try again or check the API.")
