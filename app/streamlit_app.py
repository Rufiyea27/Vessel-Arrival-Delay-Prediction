import streamlit as st
import requests

API_URL = "https://vessel-delay-prediction.onrender.com/predict"

st.set_page_config(
    page_title="Vessel Delay Predictor",
    page_icon="🚢",
    layout="wide"
)

st.title("🚢 Vessel Arrival Delay Prediction")

st.markdown(
"""
Predict whether a vessel is likely to arrive late.
"""
)


carrier = st.selectbox(
    "Carrier",
    ["Maersk","MSC","COSCO","CMA CGM","Hapag-Lloyd"]
)

vessel_type = st.selectbox(
    "Vessel Type",
    ["Container","Bulk Carrier","Oil Tanker"]
)

origin = st.selectbox(
    "Origin Port",
    ["Singapore","Shanghai","Dubai"]
)

destination = st.selectbox(
    "Destination Port",
    ["Rotterdam","Hamburg","Los Angeles"]
)

distance = st.number_input(
    "Distance (NM)",
    value=8200
)

transit_days = st.number_input(
    "Scheduled Transit Days",
    value=22
)

departure_delay = st.slider(
    "Departure Delay (Hours)",
    0,
    48,
    6
)

speed = st.slider(
    "Average Speed (Knots)",
    10,
    30,
    18
)

vessel_age = st.slider(
    "Vessel Age",
    1,
    30,
    10
)

cargo = st.slider(
    "Cargo Load %",
    40,
    100,
    85
)

congestion = st.slider(
    "Port Congestion",
    0,
    100,
    70
)

weather = st.slider(
    "Weather Severity",
    1,
    10,
    5
)

fuel = st.number_input(
    "Fuel Price",
    value=650
)

historical = st.slider(
    "Historical Route Delay",
    0,
    48,
    10
)

season = st.selectbox(
    "Season",
    ["Spring","Summer","Autumn","Winter"]
)

customs = st.selectbox(
    "Customs Risk",
    ["Low","Medium","High"]
)

route = f"{origin} → {destination}"

if congestion < 30:
    congestion_level = "Low"
elif congestion < 70:
    congestion_level = "Medium"
else:
    congestion_level = "High"

if weather <= 3:
    weather_category = "Clear"
elif weather <= 6:
    weather_category = "Moderate"
else:
    weather_category = "Severe"

if vessel_age <= 5:
    age_group = "New"
elif vessel_age <= 15:
    age_group = "Mid Age"
else:
    age_group = "Old"

if cargo < 60:
    load_category = "Low"
elif cargo < 85:
    load_category = "Medium"
else:
    load_category = "High"

if speed < 15:
    speed_category = "Slow"
elif speed < 20:
    speed_category = "Normal"
else:
    speed_category = "Fast"

delay_risk = (
    departure_delay * 0.4
    + weather * 0.3
    + congestion * 0.3
)
if st.button("Predict"):

    payload = {

        "Carrier": carrier,
        "Vessel_Type": vessel_type,
        "Origin_Port": origin,
        "Destination_Port": destination,

        "Distance_NM": distance,
        "Scheduled_Transit_Days": transit_days,
        "Departure_Delay_Hours": departure_delay,
        "Average_Speed_Knots": speed,
        "Vessel_Age": vessel_age,
        "Cargo_Load_Percentage": cargo,
        "Port_Congestion_Index": congestion,
        "Weather_Severity": weather,
        "Fuel_Price_USD": fuel,
        "Historical_Route_Delay": historical,

        "Season": season,
        "Customs_Clearance_Risk": customs,

        "Route": route,
        "Congestion_Level": congestion_level,
        "Weather_Category": weather_category,
        "Vessel_Age_Group": age_group,
        "Load_Category": load_category,
        "Speed_Category": speed_category,

        "Delay_Risk_Score": delay_risk
    }

    response = requests.post(API_URL, json=payload)

if response.status_code == 200:

    result = response.json()

    st.success("Prediction Complete!")

    st.metric(
        "Prediction",
        result["Prediction"]
    )

    st.metric(
        "Delay Probability",
        f"{result['Delay_Probability']:.2%}"
    )

    st.metric(
        "Risk Level",
        result["Risk_Level"]
    )

    if result["Risk_Level"] == "High":
        st.error("⚠ High Risk Voyage")

    elif result["Risk_Level"] == "Medium":
        st.warning("⚠ Medium Risk Voyage")

    else:
        st.success("✅ Low Risk Voyage")

else:

    st.error("API request failed.")

    st.write(response.text)