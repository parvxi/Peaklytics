import optuna
from lightgbm import LGBMClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score
from lightgbm import early_stopping, log_evaluation
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
import pandas as pd

# Function to clean column names


# Function to train and optimize the model
def train_and_optimize_model(X_train, y_train, X_val, y_val):
    # Clean the column names
    X_train = clean_column_names(X_train)
    X_val = clean_column_names(X_val)  # Ensure consistency with validation set

    # Objective function for Optuna
    def objective(trial):
        param = {
            'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.1),
            'n_estimators': trial.suggest_int('n_estimators', 100, 500),
            'max_depth': trial.suggest_int('max_depth', 6, 10),
            'num_leaves': trial.suggest_int('num_leaves', 20, 50),
            'min_child_samples': trial.suggest_int('min_child_samples', 20, 100),
            'subsample': trial.suggest_float('subsample', 0.6, 0.9),
            'colsample_bytree': trial.suggest_float('colsample_bytree', 0.6, 0.9),
            'reg_alpha': trial.suggest_float('reg_alpha', 1, 10.0),
            'reg_lambda': trial.suggest_float('reg_lambda', 1, 10.0),
            'random_state': 45
        }

        # Initialize the model
        lgbm_model = LGBMClassifier(**param)
        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        f1 = cross_val_score(lgbm_model, X_train, y_train, cv=cv, scoring='f1', n_jobs=-1).mean()
        return f1

    # Optimize hyperparameters using Optuna
    study = optuna.create_study(direction='maximize')
    study.optimize(objective, n_trials=50)

    # Train the best model
    best_params = study.best_params
    lgbm_model = LGBMClassifier(**best_params)

    # Fit the model with early stopping and log evaluation
    lgbm_model.fit(X_train, y_train,
                   eval_set=[(X_val, y_val)],
                   eval_metric='f1',
                   callbacks=[early_stopping(stopping_rounds=100), log_evaluation(50)])

    return lgbm_model, best_params

# Function to predict using the trained model
def predict_model(model: LGBMClassifier, X_test) -> pd.DataFrame:
    X_test = clean_column_names(X_test)  # Ensure test set has cleaned column names
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    return y_pred, y_pred_proba

# Function to evaluate the model
def evaluate_model(y_true, y_pred, y_pred_proba) -> dict:
    accuracy = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    roc_auc = roc_auc_score(y_true, y_pred_proba)
    return {
        'accuracy': accuracy,
        'f1_score': f1,
        'roc_auc_score': roc_auc
    }
