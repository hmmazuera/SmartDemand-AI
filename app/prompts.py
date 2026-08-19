def build_prompt(features, prediction):
    return f"""
    You are a bike rental demand prediction model. 
    A machine learning model predicted {prediction} bike rentals for the selected hour.

    Condictions:
    - Season: {features['season']}
    - Weather: {features['weather']}
    - Temperature: {features['temp']}°C
    - Humidity: {features['humidity']}%
    - Windspeed: {features['windspeed']}
    - Working Day: {features['workingday']}
    - Holiday: {features['holiday']}
    - Hour: {features['hour']}:00
    
    Write a short and concise summary of the predicted bike rental demand for the selected hour, considering the provided conditions.
    The summary must be 2-3 sentences long discribing why demand is expected to be low, medium or high. Do not mention AI or machine learning.
"""

