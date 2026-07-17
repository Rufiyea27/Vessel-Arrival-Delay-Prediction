from pydantic import BaseModel, Field


class VoyageInput(BaseModel):
    """
    Input schema for Vessel Arrival Delay Prediction
    """

    Carrier: str = Field(..., example="Maersk")
    Vessel_Type: str = Field(..., example="Container")

    Origin_Port: str = Field(..., example="Singapore")
    Destination_Port: str = Field(..., example="Rotterdam")

    Distance_NM: float = Field(..., example=8200)

    Scheduled_Transit_Days: float = Field(..., example=22)

    Departure_Delay_Hours: float = Field(..., example=8)

    Average_Speed_Knots: float = Field(..., example=18)

    Vessel_Age: int = Field(..., example=10)

    Cargo_Load_Percentage: float = Field(..., example=85)

    Port_Congestion_Index: float = Field(..., example=70)

    Weather_Severity: float = Field(..., example=6)

    Fuel_Price_USD: float = Field(..., example=650)

    Historical_Route_Delay: float = Field(..., example=12)

    Season: str = Field(..., example="Summer")

    Customs_Clearance_Risk: str = Field(..., example="Medium")

    Route: str = Field(..., example="Singapore → Rotterdam")

    Congestion_Level: str = Field(..., example="High")

    Weather_Category: str = Field(..., example="Moderate")

    Vessel_Age_Group: str = Field(..., example="Mid Age")

    Load_Category: str = Field(..., example="High")

    Speed_Category: str = Field(..., example="Normal")

    Delay_Risk_Score: float = Field(..., example=26.6)


class PredictionResponse(BaseModel):
    """
    Prediction response schema
    """

    Prediction: str
    Late_Arrival: int
    Delay_Probability: float
    Confidence: float
    Risk_Level: str