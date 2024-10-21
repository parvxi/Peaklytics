import streamlit as st
import plotly.graph_objects as go

response_body = {
    "prediction": "fail",
    "user_inputs": {
        "market": "Healthcare",
        "funding_total_usd": 350000,
        "region": "North America",
        "city": "San Francisco",
        "funding_rounds": 2,
        "seed": 150000,
        "venture": 200000,
        "equity_crowdfunding": 0,
        "undisclosed": 0,
        "convertible_note": 0,
        "angel": 0,
        "grant": 0,
        "private_equity": 0,
        "post_ipo_equity": 0,
        "post_ipo_debt": 0,
        "secondary_market": 0,
        "product_crowdfunding": 0,
        "round_A": 0,
        "round_B": 0,
        "round_C": 0,
        "round_D": 0,
        "round_E": 0,
        "round_F": 0,
        "country": "USA",
        "funding_category": "Early Stage Venture",
        "company_age": 3,
        "market_category": "Healthcare Services"
    },
    "calculations": {
        "average_funding_per_round": 175000,
        "seed_funding_percentage": 42.86,
        "venture_funding_percentage": 57.14,
        "burn_rate": 29166.67,
        "runway": 12,
        "break_even_revenue": 35000
    },
    "rule_based_insights": [
        "Funding is below average. Seek additional investment to fuel growth in the Healthcare market.",
        "Explore additional funding rounds to improve financial standing in the Healthcare sector.",
        "Improve funding utilization efficiency. Consider agile methodologies to reduce costs."
    ],
    "llm_insights": "Based on the provided data, I've identified potential strategies to avoid failure:\n\n1. Reduce burn rate by cutting non-essential expenses.\n2. Secure additional funding to increase the company runway.\n3. Focus on product-market fit to attract more investment.\n4. Analyze competitors in the Healthcare market to identify opportunities for differentiation."
}

# App Title
st.title("🌟 Peaklytics Prediction Dashboard 🌟")

# Prediction Section
st.subheader(f"Company's Predicted Outcome: **{response_body['prediction'].capitalize()}**")
st.markdown("---")

# User Inputs Section
st.write("### User Input Details")
st.write("Below are the inputs you provided for the prediction:")

user_inputs = response_body['user_inputs']
st.table({
    "Field": list(user_inputs.keys()),
    "Value": list(user_inputs.values())
})

# Enhanced Pie Chart for Funding Breakdown
st.markdown("---")
st.write("### Funding Breakdown")

funding_data = {
    'Type': ['Seed', 'Venture', 'Equity Crowdfunding', 'Convertible Note', 'Angel'],
    'Amount': [
        user_inputs['seed'],
        user_inputs['venture'],
        user_inputs['equity_crowdfunding'],
        user_inputs['convertible_note'],
        user_inputs['angel']
    ]
}

# Plot Pie chart for funding breakdown
pie_chart = go.Figure(go.Pie(
    labels=funding_data['Type'],
    values=funding_data['Amount'],
    hole=.3,
    title="Funding Distribution"
))
st.plotly_chart(pie_chart)

# KPI Display Section
st.markdown("---")
st.subheader("Key Financial Metrics")

# Slider for interactive burn rate adjustment
burn_rate = st.slider('Adjust Burn Rate (USD/Month)', min_value=10000, max_value=100000, value=int(response_body['calculations']['burn_rate']))
runway = response_body['calculations']['runway']

# Gauge chart for burn rate
burn_rate_gauge = go.Figure(go.Indicator(
    mode="gauge+number",
    value=burn_rate,
    title={'text': "Burn Rate (USD/Month)"},
    gauge={'axis': {'range': [0, max(100000, burn_rate * 2)]}}
))
st.plotly_chart(burn_rate_gauge)

# Display runway based on burn rate
st.write(f"### Updated Runway: {int(response_body['calculations']['funding_total_usd'] / burn_rate)} months")

# Display break-even revenue in a new gauge chart
break_even_gauge = go.Figure(go.Indicator(
    mode="gauge+number",
    value=response_body['calculations']['break_even_revenue'],
    title={'text': "Break-Even Revenue (USD)"},
    gauge={'axis': {'range': [0, max(50000, response_body['calculations']['break_even_revenue'] * 2)]}}
))
st.plotly_chart(break_even_gauge)

# Collapsible Section for Insights
st.markdown("---")
st.subheader("Business Insights")

with st.expander("View Rule-Based Insights"):
    for insight in response_body['rule_based_insights']:
        st.write(f"- {insight}")

with st.expander("View LLM-Generated Insights"):
    st.markdown(response_body['llm_insights'])

st.success("Thank you for using Peaklytics! We hope these insights help you make informed decisions.")
