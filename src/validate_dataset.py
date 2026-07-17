# ============================================
# Dataset Validation Script
# ============================================

import pandas as pd

# --------------------------------------------
# Load Dataset
# --------------------------------------------

file_path = "data/raw/vessel_arrival_delay.csv"

df = pd.read_csv(file_path)

print("=" * 60)
print("VESSEL ARRIVAL DELAY DATASET VALIDATION")
print("=" * 60)

# --------------------------------------------
# Dataset Shape
# --------------------------------------------

print("\n1. Dataset Shape")
print("-" * 30)

print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

# --------------------------------------------
# Dataset Info
# --------------------------------------------

print("\n2. Dataset Information")
print("-" * 30)

print(df.info())

# --------------------------------------------
# Missing Values
# --------------------------------------------

print("\n3. Missing Values")
print("-" * 30)

print(df.isnull().sum())

# --------------------------------------------
# Duplicate Rows
# --------------------------------------------

print("\n4. Duplicate Rows")
print("-" * 30)

print(df.duplicated().sum())

# --------------------------------------------
# Summary Statistics
# --------------------------------------------

print("\n5. Numerical Summary")
print("-" * 30)

print(df.describe())

# --------------------------------------------
# Target Distribution
# --------------------------------------------

print("\n6. Late Arrival Distribution")
print("-" * 30)

print(df["Late_Arrival"].value_counts())

print("\nPercentage")

print(df["Late_Arrival"].value_counts(normalize=True) * 100)

# --------------------------------------------
# Unique Carriers
# --------------------------------------------

print("\n7. Carrier Values")
print("-" * 30)

print(df["Carrier"].value_counts())

# --------------------------------------------
# Customs Risk
# --------------------------------------------

print("\n8. Customs Risk")
print("-" * 30)

print(df["Customs_Clearance_Risk"].value_counts())

# --------------------------------------------
# Ports
# --------------------------------------------

print("\n9. Origin Ports")
print("-" * 30)

print(df["Origin_Port"].value_counts())

print("\nDestination Ports")

print(df["Destination_Port"].value_counts())

# --------------------------------------------
# Delay Statistics
# --------------------------------------------

print("\n10. Delay Statistics")
print("-" * 30)

print(df["Actual_Delay_Hours"].describe())

# --------------------------------------------
# Dataset Validation Completed
# --------------------------------------------

print("\nValidation Completed Successfully!")