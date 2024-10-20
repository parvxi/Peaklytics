import pandas as pd
from datetime import datetime
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

def clean_data(df):
    """
    Cleans the dataset by removing unnecessary columns and creating new features.
    """
    # Convert date columns to datetime
    df['first_funding_at'] = pd.to_datetime(df['first_funding_at'], errors='coerce')
    df['last_funding_at'] = pd.to_datetime(df['last_funding_at'], errors='coerce')
    df['founded_at'] = pd.to_datetime(df['founded_at'], errors='coerce')

    # Create a new column 'funding_category' based on funding rounds
    df['funding_category'] = df.apply(
        lambda x: 'Single Round - Traditional' if x['funding_rounds'] == 1 and x[['seed', 'venture']].sum() == 0
        else 'Single Round - Non-traditional' if x['funding_rounds'] == 1 and x[['seed', 'venture']].sum() > 0
        else 'Multiple Rounds', axis=1)

    # Calculate the company age
    current_year = datetime.now().year
    df['company_age'] = current_year - df['founded_at'].dt.year

    # Remove unnecessary columns
    df.drop(columns=['Unnamed: 0', 'round_G', 'round_H', 'founded_quarter', 'quater',
                     'founded_month', 'name', 'founded_year', 'founded_at', 'debt_financing',
                     'first_funding_at', 'last_funding_at'], inplace=True)

    return df

def impute_missing_values(df):
    """
    Imputes missing values using the median strategy.
    """
    imputer = SimpleImputer(strategy='median')
    df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    return df_imputed

def scale_data(X_train, X_test, columns_to_scale):
    """
    Scales the numerical data using StandardScaler.
    """
    scaler = StandardScaler()
    X_train[columns_to_scale] = scaler.fit_transform(X_train[columns_to_scale])
    X_test[columns_to_scale] = scaler.transform(X_test[columns_to_scale])
    return X_train, X_test, scaler
