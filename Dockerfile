# Use Python 3.10 slim version for a lightweight container
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /prod

# Install system dependencies including libgomp for parallelization libraries
RUN apt-get update && apt-get install -y \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .


# Install the necessary dependencies
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

# Copy the rest of the application code into the container
COPY peaklytics/ peaklytics/

# Copy the model file from the local directory to the container
COPY peaklytics/ml_logic/final_lgbm_model_2 /prod/peaklytics/ml_logic/final_lgbm_model_2

# Set the environment variable for the model path inside the container
ENV MODEL_PATH=/prod/peaklytics/ml_logic/final_lgbm_model_2

# Command to run the FastAPI app using Uvicorn with port 8080
CMD ["sh", "-c", "uvicorn peaklytics.api.fast:app --host 0.0.0.0 --port 8080"]
