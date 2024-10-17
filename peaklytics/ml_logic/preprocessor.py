import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from datetime import datetime
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
def print_columns(df, step):
    """
    Function to print the columns after each step.
    """
    print(f"\nColumns after {step}:")
    print(df.columns)
    print(f"Number of features: {df.shape[1]}")
def calculate_company_age(df):
    """
    Function to calculate the age of the company.
    """
    current_year = datetime.now().year
    df['company_age'] = current_year - df['founded_year']
    return df
def clean_data(df):
    """
    Clean the initial dataset by performing feature engineering and handling missing values.
    """
    # Check for missing values
    missing_values = df.isnull().sum()
    print("\nMissing values before Cleaning:")
    print(missing_values)
    # Print initial columns
    print_columns(df, "initial dataset")
    # Convert date columns to datetime
    df['first_funding_at'] = pd.to_datetime(df['first_funding_at'], errors='coerce')
    df['last_funding_at'] = pd.to_datetime(df['last_funding_at'], errors='coerce')
    df['founded_at'] = pd.to_datetime(df['founded_at'], errors='coerce')
    print_columns(df, "datetime conversion")
    # Feature Engineering: Create 'funding_category' column
    df['funding_category'] = df.apply(
        lambda x: 'Single Round - Traditional' if x['funding_rounds'] == 1 and x[['seed', 'venture']].sum() == 0
        else 'Single Round - Non-traditional' if x['funding_rounds'] == 1 and x[['seed', 'venture']].sum() > 0
        else 'Multiple Rounds', axis=1)
    print_columns(df, "feature engineering")
    # Calculate 'company_age'
    df = calculate_company_age(df)
    print_columns(df, "calculating company age")
    # Drop unnecessary columns
    columns_to_drop = [
        'Unnamed: 0', 'round_G', 'round_H', 'founded_quarter', 'quater',
        'founded_month', 'name', 'founded_year', 'founded_at',
        'debt_financing', 'first_funding_at', 'last_funding_at'
    ]
    df.drop(columns=columns_to_drop, inplace=True)
    print_columns(df, "dropping unnecessary columns")
    # Apply transformation on 'status' column
    df['status'] = df['status'].apply(lambda x: 'operating' if x == 'acquired' else x)
    print_columns(df, "transforming status column")
    return df
def load_cleaned_data(file_path):
    """
    Load the cleaned dataset from a CSV file and handle missing values, encoding, etc.
    """
    df_cleaned = pd.read_csv(file_path)
    print_columns(df_cleaned, "loaded cleaned data")
    # Remove outliers from 'funding_total_usd'
    Q1 = df_cleaned['funding_total_usd'].quantile(0.25)
    Q3 = df_cleaned['funding_total_usd'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df_cleaned = df_cleaned[(df_cleaned['funding_total_usd'] >= lower_bound) & (df_cleaned['funding_total_usd'] <= upper_bound)]
    print_columns(df_cleaned, "removing outliers")
    # Dropping duplicates
    duplicates_before = df_cleaned.duplicated().sum()
    print(f"\nDuplicates before: {duplicates_before}")
    df_cleaned.drop_duplicates(inplace=True)
    duplicates_after = df_cleaned.duplicated().sum()
    print(f"Duplicates after: {duplicates_after}")
    print_columns(df_cleaned, "dropping duplicates")
    # One-hot encoding categorical columns
    df_cleaned = pd.get_dummies(df_cleaned, columns=['funding_category', 'country'], drop_first=True)
    print_columns(df_cleaned, "one-hot encoding")
    # Encode the 'status' column
    le = LabelEncoder()
    df_cleaned['status'] = le.fit_transform(df_cleaned['status'])
    print_columns(df_cleaned, "encoding status column")
    # Fill missing values in 'funding_total_usd' with the median
    df_cleaned['funding_total_usd'] = df_cleaned['funding_total_usd'].fillna(df_cleaned['funding_total_usd'].median())
    print_columns(df_cleaned, "filling missing values")
    # Dropping rows with any remaining missing values
    df_cleaned.dropna(inplace=True)
    print_columns(df_cleaned, "dropping rows with missing values")
    market_freq = df_cleaned['market'].value_counts(normalize=True)
    df_cleaned['market_freq'] = df_cleaned['market'].map(market_freq)
    city_freq = df_cleaned['city'].value_counts(normalize=True)
    df_cleaned['city_freq'] = df_cleaned['city'].map(city_freq)
    region_freq = df_cleaned['region'].value_counts(normalize=True)
    df_cleaned['region_freq'] = df_cleaned['region'].map(region_freq)
    df_cleaned = df_cleaned.drop(columns=['market', 'city', 'region'])
    print_columns(df_cleaned, "after frequency mapping and column drop")
    return df_cleaned
def apply_smote_and_split(df_cleaned):
    """
    Apply SMOTE to balance the dataset and split into training, validation, and test sets.
    """
    # Separate features (X) and target (y)
    X = df_cleaned.drop(columns=['status'])  # Assuming 'status' is the target column
    y = df_cleaned['status']
    # Identify any non-numerical columns that may cause issues
    non_numeric_cols = X.select_dtypes(exclude=[float, int]).columns
    print(f"Non-numeric columns: {non_numeric_cols}")
    # Remove non-numeric columns
    X = X.select_dtypes(include=[float, int])  # Keep only numerical columns
    # Split into training and test sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Apply SMOTE to balance the training data
    smote = SMOTE(random_state=42)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
    X_train, X_val, y_train, y_val = train_test_split(X_train_resampled, y_train_resampled, test_size=0.2, random_state=42)
    # Initialize the StandardScaler
    scaler = StandardScaler()
    # Get the list of numerical columns for scaling
    numerical_columns = X_train.select_dtypes(include=['float64', 'int64']).columns
    # Scale numerical columns for training, validation, and test sets
    X_train[numerical_columns] = scaler.fit_transform(X_train[numerical_columns])
    X_val[numerical_columns] = scaler.transform(X_val[numerical_columns])
    X_test[numerical_columns] = scaler.transform(X_test[numerical_columns])
    return X_train, X_val, X_test, y_train, y_val, y_test
