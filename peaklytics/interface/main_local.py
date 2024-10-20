import pandas as pd
from peaklytics.ml_logic.preprocessor import clean_data, load_cleaned_data
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler

# Load the raw dataset
df = pd.read_csv('../Peaklytics/raw_data/Peaklytics_intial_data.csv')

# Clean the raw data and organize it
df_cleaned = clean_data(df)
print(f"Rows after cleaning: {df_cleaned.shape[0]}")

# Save the cleaned dataset
df_cleaned.to_csv('cleaned_peaklytics_data.csv', index=False)

# Load the cleaned dataset for further processing
df_cleaned_final = load_cleaned_data('../Peaklytics/cleaned_peaklytics_data.csv')
print(f"Rows after further cleaning and processing: {df_cleaned_final.shape[0]}")

# Number of features after cleaning
num_features = df_cleaned_final.shape[1]
print(f"Number of features: {num_features}")

# Step to apply SMOTE and split data
def apply_smote_and_split(df_cleaned):
    """
    Apply SMOTE to balance the dataset and split into training, validation, and test sets.
    """
    # Separate features (X) and target (y)
    X = df_cleaned.drop(columns=['status'])
    y = df_cleaned['status']

    # Split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Apply SMOTE to balance the training data
    smote = SMOTE(random_state=42)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

    # Further split the resampled data into training and validation sets
    X_train, X_val, y_train, y_val = train_test_split(X_train_resampled, y_train_resampled, test_size=0.2, random_state=42)

    # Initialize the StandardScaler
    scaler = StandardScaler()

    # Get the list of numerical columns
    numerical_columns = X_train.select_dtypes(include=['float64', 'int64']).columns

    # Scale numerical columns for training, validation, and test sets
    X_train[numerical_columns] = scaler.fit_transform(X_train[numerical_columns])
    X_val[numerical_columns] = scaler.transform(X_val[numerical_columns])
    X_test[numerical_columns] = scaler.transform(X_test[numerical_columns])

    return X_train, X_val, X_test, y_train, y_val, y_test

# Apply SMOTE and split the data
X_train, X_val, X_test, y_train, y_val, y_test = apply_smote_and_split(df_cleaned_final)

# Output sizes of training, validation, and test sets
print(f"Training set size: {X_train.shape[0]}")
print(f"Validation set size: {X_val.shape[0]}")
print(f"Test set size: {X_test.shape[0]}")
