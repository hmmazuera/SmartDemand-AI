import os
import joblib
import pandas as pd
import requests
from constanst import MODEL_PATH
from dotenv import load_dotenv
from prompts import build_prompt

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

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
    responde = requests.post(
        'https://openrouter.ai/api/v1/chat/completions',
        headers={
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json',
        },
        json={
            'model': 'minstralai/mistral-7b-instruct',
            'messages': [
                {'role': 'user', 'content': prompt}
            ]
        }
    )
    return responde.json()['choices'][0]['message']['content']