import streamlit as st
from constanst import APP_TITLE, APP_SUBTITLE
from utils import load_model, predict_demand

model = load_model()

st.set_page_config(page_title=APP_TITLE, page_icon="🚲")

st.title(APP_TITLE)
st.subheader(APP_SUBTITLE)
st.divider()

st.markdown(""" Date and Time """)

col1, col2 = st.columns(2)

with col1:
    year = st.selectbox('Year', [2011,2012])
    mont = st.selectbox('Month', list(range(1,13)))
    day = st.slider('Day', 1,31,15)

with col2:
    hour = st.slider('Hour', 0,23,12)
    season = st.selectbox('Season', options=[1,2,3,4], format_func=lambda x: {
        1: 'Spring',
        2: 'Summer',
        3: 'Fall',
        4: 'Winter'
    }[x]
    )

st.divider()
st.markdown(""" Weather Conditions """)

col3, col4 = st.columns(2)
with col3:
    weather = st.selectbox('Weather', options=[1,2,3,4], format_func=lambda x: {
        1: 'Clear',
        2: 'Mist',
        3: 'Light Rain/Snow',
        4: 'Heavy Rain/Snow'
    }[x] )

    temp = st.slider('Temperature (°C)', 0.0, 40.0, 20.0)
    humidity = st.slider('Humidity (%)', 0, 100, 50)

with col4:
    atemp = st.slider('Feels like (°C)', 0.0, 40.0, 20.0)
    windspeed = st.slider('Windspeed', 0.0, 50.0, 10.0)
    holiday = st.selectbox('Holiday', [0,1], format_func=lambda x: 'Yes' if x else 'No')
    workingday = st.selectbox('Working Day', [0,1], format_func=lambda x: 'Yes' if x else 'No')

st.divider()

if st.button('Predict Demand', use_container_width=True):
    input_data = {
        'season': season,
        'holiday': holiday,
        'workingday': workingday,
        'weather': weather,
        'temp': temp,
        'atemp': atemp,
        'humidity': humidity,
        'windspeed': windspeed,
        'year': year,
        'month': mont,
        'day': day,
        'hour': hour
    }
    prediction = predict_demand(model, input_data)

    st.divider()
    st.metric(
        label="Predicted Bike Rental Demand",
        value=f"{prediction} rentals",
    )

    if prediction < 150:
        st.info("Low demand expected. Consider reducing bike availability.")
    elif prediction < 300:
        st.warning("Moderate demand expected. Ensure sufficient bike availability.")
    else:
        st.success("High demand expected! Ensure maximum bike availability.")