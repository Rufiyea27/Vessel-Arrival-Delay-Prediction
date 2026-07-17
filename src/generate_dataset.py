# ============================================
# Vessel Arrival Delay Prediction
# Synthetic Dataset Generator
# ============================================

# Import required libraries
import pandas as pd
import numpy as np
import random
from faker import Faker

# --------------------------------------------
# Set random seed for reproducibility
# --------------------------------------------
random.seed(42)
np.random.seed(42)

fake = Faker()
Faker.seed(42)

# --------------------------------------------
# Number of records to generate
# --------------------------------------------
NUM_RECORDS = 15000

# --------------------------------------------
# Define categorical values
# --------------------------------------------
carriers = [
    "Maersk",
    "MSC",
    "CMA CGM",
    "Hapag-Lloyd",
    "ONE",
    "Evergreen",
    "COSCO",
    "Yang Ming"
]

vessel_types = [
    "Container",
    "Bulk Carrier",
    "Oil Tanker",
    "LNG Carrier"
]

ports = [
    "Singapore",
    "Shanghai",
    "Rotterdam",
    "Los Angeles",
    "Hamburg",
    "Dubai",
    "Busan",
    "Antwerp",
    "Mumbai",
    "Colombo"
]

seasons = [
    "Spring",
    "Summer",
    "Autumn",
    "Winter"
]

customs_risk = [
    "Low",
    "Medium",
    "High"
]

# --------------------------------------------
# Create an empty list to store voyage records
# --------------------------------------------
data = []

# --------------------------------------------
# Generate synthetic voyage data
# --------------------------------------------
for i in range(NUM_RECORDS):

    # Generate unique Voyage ID
    voyage_id = f"V{i+1:05d}"

    # Randomly assign carrier
    carrier = random.choice(carriers)

    # Randomly assign vessel type
    vessel_type = random.choice(vessel_types)

    # Generate a fake vessel name
    vessel_name = fake.first_name() + " Voyager"

    # Select origin port
    origin_port = random.choice(ports)

    # Select destination port (must be different)
    destination_port = random.choice(
        [port for port in ports if port != origin_port]
    )

    # Random season
    season = random.choice(seasons)

    # Customs risk level
    customs = random.choice(customs_risk)

        # --------------------------------------------
    # Generate Numerical Features
    # --------------------------------------------

    # Voyage distance in Nautical Miles
    distance_nm = random.randint(500, 12000)

    # Scheduled transit days
    scheduled_transit_days = round(distance_nm / random.uniform(250, 450), 1)

    # Departure delay at origin port
    departure_delay_hours = round(max(0, np.random.normal(6, 5)), 1)

    # Average vessel speed
    average_speed_knots = round(random.uniform(12, 24), 1)

    # Vessel age
    vessel_age = random.randint(1, 30)

    # Cargo utilization %
    cargo_load_percentage = round(random.uniform(40, 100), 1)

    # Port congestion score
    port_congestion_index = round(random.uniform(0, 100), 1)

    # Weather severity (0 = Clear, 10 = Extreme Storm)
    weather_severity = round(random.uniform(0, 10), 1)

    # Fuel price in USD
    fuel_price_usd = round(random.uniform(450, 850), 2)

    # Historical average delay on the route
    historical_route_delay = round(max(0, np.random.normal(8, 6)), 1)
        # --------------------------------------------
    # Business Logic to Calculate Actual Delay
    # --------------------------------------------

    # Higher speed helps reduce delay
    speed_advantage = max(0, average_speed_knots - 18)

    # Random operational factors
    operational_noise = np.random.normal(0, 2)

    # Calculate Actual Delay Hours
    actual_delay_hours = (
        departure_delay_hours * 0.45
        + port_congestion_index * 0.12
        + weather_severity * 1.80
        + historical_route_delay * 0.40
        + vessel_age * 0.05
        - speed_advantage * 0.40
        + operational_noise
    )

    # Delay cannot be negative
    actual_delay_hours = round(max(0, actual_delay_hours), 1)

    # --------------------------------------------
    # Target Variable
    # --------------------------------------------

    late_arrival = 1 if actual_delay_hours >= 12 else 0
    # Create dictionary for one voyage
    row = {
        "Voyage_ID": voyage_id,
        "Carrier": carrier,
        "Vessel_Name": vessel_name,
        "Vessel_Type": vessel_type,
        "Origin_Port": origin_port,
        "Destination_Port": destination_port,

        "Distance_NM": distance_nm,
        "Scheduled_Transit_Days": scheduled_transit_days,
        "Departure_Delay_Hours": departure_delay_hours,
        "Average_Speed_Knots": average_speed_knots,
        "Vessel_Age": vessel_age,
        "Cargo_Load_Percentage": cargo_load_percentage,
        "Port_Congestion_Index": port_congestion_index,
        "Weather_Severity": weather_severity,
        "Fuel_Price_USD": fuel_price_usd,
        "Historical_Route_Delay": historical_route_delay,

        "Season": season,
        "Customs_Clearance_Risk": customs,

        "Actual_Delay_Hours": actual_delay_hours,
        "Late_Arrival": late_arrival
    }
    # Append row to data list
    data.append(row)

# --------------------------------------------
# Convert list to DataFrame
# --------------------------------------------
df = pd.DataFrame(data)

# --------------------------------------------
# Display first few rows
# --------------------------------------------
print("\nFirst 5 Records:\n")
print(df.head())

# --------------------------------------------
# Display dataset information
# --------------------------------------------
print("\nDataset Information:\n")
print(df.info())

# --------------------------------------------
# Display dataset shape
# --------------------------------------------
print("\nDataset Shape:")
print(df.shape)


print(df.head(10))

# Save dataset
df.to_csv("data/raw/vessel_arrival_delay_dataset.csv", index=False)

print("\nDataset saved successfully!")

df = pd.DataFrame(data)

# ============================================
# Introduce Missing Values
# ============================================

missing_columns = [
    "Departure_Delay_Hours",
    "Weather_Severity",
    "Port_Congestion_Index",
    "Fuel_Price_USD",
    "Historical_Route_Delay"
]

for column in missing_columns:
    missing_index = df.sample(frac=0.03, random_state=42).index
    df.loc[missing_index, column] = np.nan


    # ============================================
# Introduce Duplicate Records
# ============================================

duplicates = df.sample(n=100, random_state=42)

df = pd.concat([df, duplicates], ignore_index=True)


# ============================================
# Introduce Outliers
# ============================================

outlier_index = df.sample(n=50, random_state=10).index

df.loc[outlier_index, "Actual_Delay_Hours"] *= 3

# ============================================
# Introduce Outliers
# ============================================

outlier_index = df.sample(n=50, random_state=10).index

df.loc[outlier_index, "Actual_Delay_Hours"] *= 3


# ============================================
# Introduce Inconsistent Categories
# ============================================

replace_index = df.sample(n=40, random_state=15).index

df.loc[replace_index, "Carrier"] = "maersk"

replace_index = df.sample(n=30, random_state=20).index

df.loc[replace_index, "Carrier"] = "MSC "

replace_index = df.sample(n=20, random_state=25).index

df.loc[replace_index, "Carrier"] = "CMA-CGM"


# ============================================
# Shuffle Dataset
# ============================================

df = df.sample(frac=1, random_state=42).reset_index(drop=True)



# ============================================
# Save Dataset
# ============================================

output_path = "data/raw/vessel_arrival_delay.csv"

df.to_csv(output_path, index=False)

print(f"\nDataset saved successfully to:\n{output_path}")


# ============================================
# Dataset Summary
# ============================================

print("\nDataset Created Successfully!")
print("-" * 50)

print(f"Rows : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

print("\nMissing Values")

print(df.isnull().sum())

print("\nDuplicate Rows")

print(df.duplicated().sum())

print("\nTarget Distribution")

print(df["Late_Arrival"].value_counts())

print("\nFirst Five Rows")

print(df.head())