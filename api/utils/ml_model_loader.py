import joblib
from constants import BASE_DIR
from sklearn.linear_model import LogisticRegression

_model = None

def load_model() -> LogisticRegression:
    """
    Load the Logistic Regression model globally
    """
    global _model
    
    if _model is not None:
        return _model
    
    model_path = BASE_DIR / "storage" / "logistic_regression_model.pkl"
    
    model: LogisticRegression = joblib.load(model_path)
    
    _model = model
    
    return model