import joblib
import pandas as pd
from constanst import MODEL_PATH

def load_model():
    model = joblib.load(MODEL_PATH)
    print(type(model))
    return model

def predict_demand(model, input_data):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]
    return round(prediction)