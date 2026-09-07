import os
import joblib
import pandas as pd
import requests
from constanst import MODEL_PATH
from dotenv import load_dotenv
from prompts import build_prompt
import json

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def load_model():
    model = joblib.load(MODEL_PATH)
    print(type(model))
    return model

def predict_demand(model, input_data):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]
    return round(prediction)

def generate_explanation(features, prediction):

    prompt = build_prompt(features, prediction)

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "openrouter/free",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        })
    )

    response = response.json()

    if "choices" not in response:
        return f"OpenRouter Error: {response}"

    return response["choices"][0]["message"]["content"]