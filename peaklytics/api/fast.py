
import sys
sys.path.append('/home/joud/code/parvxi/Peaklytics')

from fastapi import FastAPI, HTTPException
print(sys.path)
#from api import fast
from pydantic import BaseModel
import pandas as pd
from peaklytics.ml_logic.preprocessor import clean_data, encode_categorical_features
from peaklytics.ml_logic.registry import load_model
from langchain_ollama import OllamaLLM
import logging
import os
import uvicorn
# Initialize FastAPI app and load the model
app = FastAPI()
llm = OllamaLLM(model="llama3.1")
app.state.model = load_model()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define input schema
class CompanyData(BaseModel):
    market: str
    funding_total_usd: int
    region: str
    city: str
    funding_rounds: int
    seed: int
    venture: int
    equity_crowdfunding: int
    undisclosed: int
    convertible_note: int
    angel: int
    grant: int
    private_equity: int
    post_ipo_equity: int
    post_ipo_debt: int
    secondary_market: int
    product_crowdfunding: int
    round_A: int
    round_B: int
    round_C: int
    round_D: int
    round_E: int
    round_F: int
    country: str
    funding_category: str
    company_age: int
    market_category: str

@app.get("/")
def read_root():
    return {"message": "Hello, Welcome to Peaklytics!"}

#------------------------------------------------------------------------------------------------

@app.post("/predict")
async def predict(data: CompanyData):
    try:
        model = app.state.model
        if model is None:
            raise HTTPException(status_code=500, detail="Model not loaded")

        # Convert the incoming data to a DataFrame
        df_input = pd.DataFrame([data.dict()])

        # Step 1: Clean the data
        df_cleaned = clean_data(df_input)

        # Step 2: Get the training columns from the model
        training_columns = model.feature_names_in_

        # Step 3: Encode categorical features
        df_encoded = encode_categorical_features(df_cleaned, training_columns=training_columns)

        # Prepare the data for prediction
        X_processed = df_encoded

        # Handle edge cases for very low values and young companies
        predicted_status = handle_edge_cases(data, X_processed, model)

        # Perform useful calculations
        calculations = perform_calculations(data)

        # Apply rule-based system for additional insights
        rule_based_insights = apply_rule_based_insights(data)

        # Generate prompt for LLM based on the predicted status and calculations
        prompt = generate_prompt(predicted_status, data, calculations)
        response = llm.invoke(prompt)

        # Display inputs, calculations, and insights in the response
        return {
            "prediction": predicted_status,
            "user_inputs": data.dict(),
            "calculations": calculations,
            "rule_based_insights": rule_based_insights,
            "llm_insights": response
        }

    except HTTPException as e:
        logging.error(f"HTTP Exception during prediction: {str(e)}")
        raise e

    except Exception as e:
        logging.error(f"Error during prediction: {str(e)}")
        raise HTTPException(status_code=500, detail="Prediction failed")

#------------------------------------------------------------------------------------------------

def handle_edge_cases(data: CompanyData, X_processed, model) -> str:


   # if data.company_age <= 1:
        #return "early_growth"
    if (
        data.company_age > 2 and data.company_age <= 5 and  # Company is 2-5 years old
        data.funding_rounds >= 1 and data.funding_rounds <= 3 and  # The company has gone through 1 to 3 funding rounds
        (data.venture > 0 or data.round_A > 0)  # Early growth is typically characterized by venture capital or Series A funding
    ):
        return "early_growth"

    if data.funding_total_usd == 0 or data.funding_rounds <= 1:
        return "fail"

    # Make predictions
    y_pred_proba = model.predict_proba(X_processed)
    threshold = 0.7  # threshold for success/fail classification
    return "success" if y_pred_proba[0][1] > threshold else "fail"

#------------------------------------------------------------------------------------------------

def perform_calculations(data: CompanyData) -> dict:
    avg_funding_per_round = data.funding_total_usd / data.funding_rounds if data.funding_rounds > 0 else 0
    seed_percentage = (data.seed / data.funding_total_usd) * 100 if data.funding_total_usd > 0 else 0
    venture_percentage = (data.venture / data.funding_total_usd) * 100 if data.funding_total_usd > 0 else 0

    burn_rate = data.funding_total_usd / 12
    runway = data.funding_total_usd / burn_rate if burn_rate > 0 else 0
    break_even_revenue = data.funding_total_usd / 12

    return {
        "average_funding_per_round": avg_funding_per_round,
        "seed_funding_percentage": seed_percentage,
        "venture_funding_percentage": venture_percentage,
        "burn_rate": burn_rate,
        "runway": runway,
        "break_even_revenue": break_even_revenue
    }

#------------------------------------------------------------------------------------------------

def apply_rule_based_insights(data: CompanyData) -> list:
    insights = []

    if data.funding_total_usd < 500000:
        insights.append(f"Funding is below average. Seek additional investment to fuel growth in the {data.market} market.")

    if data.funding_rounds < 2:
        insights.append(f"Explore additional funding rounds to improve financial standing in the {data.market} sector.")

    funding_efficiency = data.funding_total_usd / data.company_age if data.company_age > 0 else 0
    if funding_efficiency < 100000:
        insights.append("Improve funding utilization efficiency. Consider agile methodologies to reduce costs.")

    return insights if insights else ["No specific issues detected."]

#------------------------------------------------------------------------------------------------

def generate_prompt(predicted_status: str, data: CompanyData, calculations: dict) -> str:
    base_info = f'''
        - Market: {data.market}
        - Total Funding: ${data.funding_total_usd}
        - Average Funding Per Round: ${calculations['average_funding_per_round']}
        - Seed Funding: {calculations['seed_funding_percentage']}% of total funding
        - Venture Capital: {calculations['venture_funding_percentage']}% of total funding
        - Burn Rate: ${calculations['burn_rate']} per month
        - Runway: {calculations['runway']} months
        - Location: {data.city}, {data.region}, {data.country}
        - Company Age: {data.company_age} years
    '''

    if predicted_status == "success":
        return f'''
        The company is predicted to succeed based on the following data:
        {base_info}

        To maintain and grow its success in the {data.market} market, suggest strategies for:

        1. Expanding market share.
        2. Optimizing operations to improve funding efficiency.
        3. Identifying potential risks and creating mitigation strategies.
        4. Benchmarking against key competitors in the {data.market_category} industry.
        5. Leveraging the company's funding runway and identifying when to seek the next round of investments.

        Additionally, provide case studies from companies that have maintained long-term growth in similar industries.
        '''

    elif predicted_status == "fail":
        return f'''
        The company is predicted to fail based on the following data:
        {base_info}

        Suggest strategies to avoid failure, focusing on the following areas:

        1. Identifying cost-cutting measures to extend the runway.
        2. Improving funding utilization efficiency and reallocating resources.
        3. Exploring alternative funding sources, such as private equity or convertible notes, to secure financial stability.
        4. Pivoting or adjusting the business model to align with market demands and improve competitiveness in the {data.market} sector.
        5. Evaluating case studies of companies that successfully turned around similar challenges in {data.market_category}.

        Provide industry-specific tactics that could boost the company’s chances of success.
        '''

    elif predicted_status == "early_growth":
        return f'''
        The company is in its early growth stage based on the following data:
        {base_info}

        Suggest next steps for securing funding, building an MVP, and growing the business, including:

        1. Securing additional funding (venture or equity crowdfunding) to support growth in the {data.market} market.
        2. Building an MVP and validating product-market fit.
        3. Developing partnerships and expanding customer acquisition channels.
        4. Exploring early revenue opportunities and strategies for achieving breakeven.
        5. Offering insights on competitors in similar growth stages who have successfully scaled their operations in {data.market_category}.

        Provide examples of companies that have navigated this early growth phase and achieved success.
        '''

    return "Unknown prediction status"
