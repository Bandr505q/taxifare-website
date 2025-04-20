import streamlit as st
import requests
from datetime import datetime

st.title("🚕 TaxiFareModel front")

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions.
''')

st.header("📍 Enter ride details:")

# 1. User inputs
pickup_date = st.date_input("Pickup date", value=datetime.today())
pickup_time = st.time_input("Pickup time", value=datetime.now().time())
pickup_datetime = datetime.combine(pickup_date, pickup_time)

pickup_long = st.number_input("Pickup longitude", value=-73.985428)
pickup_lat = st.number_input("Pickup latitude", value=40.748817)
dropoff_long = st.number_input("Dropoff longitude", value=-73.985428)
dropoff_lat = st.number_input("Dropoff latitude", value=40.748817)
passenger_count = st.number_input("Passenger count", min_value=1, max_value=8, value=1)

# 2. Build parameters dictionary
params = {
    "pickup_datetime": pickup_datetime.strftime("%Y-%m-%d %H:%M:%S"),
    "pickup_longitude": pickup_long,
    "pickup_latitude": pickup_lat,
    "dropoff_longitude": dropoff_long,
    "dropoff_latitude": dropoff_lat,
    "passenger_count": passenger_count
}

# 3. Call API
if st.button("Predict fare"):
    url = 'https://taxifare.lewagon.ai/predict'
    response = requests.get(url, params=params)

    if response.status_code == 200:
        prediction = response.json().get("fare", "No prediction returned")
        st.success(f"💰 Estimated fare: ${prediction:.2f}")
    else:
        st.error("❌ Failed to get prediction from API.")
