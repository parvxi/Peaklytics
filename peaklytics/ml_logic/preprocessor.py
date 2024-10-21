import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from datetime import datetime
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import numpy as np

# Utility Function: Print columns after each step
def print_columns(df, step):
    """
    Function to print the columns after each step.
    """
    print(f"\nColumns after {step}:")
    print(df.columns)
    print(f"Number of features: {df.shape[1]}")

# Function: Calculate company age
def calculate_company_age(df):
    """
    Function to calculate the age of the company based on founded_year.
    """
    current_year = datetime.now().year
    df['company_age'] = current_year - df['founded_year']
    return df

# Function: Clean the data
def clean_data(df):
    """
    Clean the initial dataset by handling missing values, feature engineering, and dropping unnecessary columns.
    """
    # Feature Engineering: Create 'funding_category' column
    df['funding_category'] = df.apply(
        lambda x: 'Single Round - Traditional' if x['funding_rounds'] == 1 and x[['seed', 'venture']].sum() == 0
        else 'Single Round - Non-traditional' if x['funding_rounds'] == 1 and x[['seed', 'venture']].sum() > 0
        else 'Multiple Rounds', axis=1)

    # Calculate 'company_age' if 'founded_year' exists
    if 'founded_year' in df.columns:
        current_year = datetime.now().year
        df['company_age'] = current_year - df['founded_year']

    # Drop unnecessary columns (remove any reference to 'first_funding_at' or 'last_funding_at')
    columns_to_drop = [
        'Unnamed: 0', 'round_G', 'round_H', 'founded_quarter', 'quater',
        'founded_month', 'name', 'founded_year',  # Keep 'founded_at' if needed for another feature
        'debt_financing', 'first_funding_at', 'last_funding_at'
    ]
    df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

    # Apply transformation to 'status' column
    if 'status' in df.columns:
        df['status'] = df['status'].apply(lambda x: 'operating' if x == 'acquired' else x)

    return df


# Function: One-hot encode categorical features and encode 'status'
def encode_categorical_features(df, training_columns=None):
    """
    Apply one-hot encoding to categorical features during prediction. Ensure the columns match the model's feature set.

    Args:
        df (pd.DataFrame): The input data.
        training_columns (list): The list of columns the model was trained on.

    Returns:
        pd.DataFrame: The encoded dataframe, matching the training feature set.
    """
    # One-hot encoding for categorical variables
    df_encoded = pd.get_dummies(df, columns=['funding_category', 'country'], drop_first=True)

    # If training_columns is provided (e.g., during prediction), ensure the same columns are present
    if training_columns is not None:
        # Identify missing columns that were in the training set but are not in the encoded data
        missing_cols = set(training_columns) - set(df_encoded.columns)

        # Convert the set to a list
        missing_cols = list(missing_cols)

        # Create a DataFrame with those missing columns, filled with zeros
        missing_df = pd.DataFrame(0, index=df_encoded.index, columns=missing_cols)

        # Concatenate the original encoded data with the missing columns DataFrame
        df_encoded = pd.concat([df_encoded, missing_df], axis=1)

        # Ensure the columns are in the same order as during training
        df_encoded = df_encoded[training_columns]

    return df_encoded



# Function: Apply SMOTE and split the data
def apply_smote_and_split(df):
    """
    Apply SMOTE to balance the dataset and split into training, validation, and test sets.
    """
    X = df.drop(columns=['status'])
    y = df['status']

    # Remove non-numeric columns
    X = X.select_dtypes(include=[np.number])

    # Split the data into training and test sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Apply SMOTE to balance the training data
    smote = SMOTE(random_state=42)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

    # Further split the training data into training and validation sets (80% train, 20% validation)
    X_train, X_val, y_train, y_val = train_test_split(X_train_resampled, y_train_resampled, test_size=0.2, random_state=42)

    # Initialize the StandardScaler
    scaler = StandardScaler()

    # Scale numerical columns for training, validation, and test sets
    X_train = scaler.fit_transform(X_train)
    X_val = scaler.transform(X_val)
    X_test = scaler.transform(X_test)

    return X_train, X_val, X_test, y_train, y_val, y_test
