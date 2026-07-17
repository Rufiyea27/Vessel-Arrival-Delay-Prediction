from contextlib import asynccontextmanager

import joblib
import pandas as pd

from fastapi import FastAPI, HTTPException

from api.schemas import VoyageInput, PredictionResponse

# =====================================================
# Global Model Variable
# =====================================================

model = None


# =====================================================
# Load Model on Startup
# =====================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    global model

    try:
        model = joblib.load("models/final_model.pkl")
        print("✅ Model loaded successfully!")

    except Exception as e:
        print(f"❌ Error loading model: {e}")

    yield

    print("Application shutting down...")


# =====================================================
# FastAPI App
# =====================================================

app = FastAPI(
    title="Vessel Arrival Delay Prediction API",
    description="Predict whether a vessel will arrive late.",
    version="1.0.0",
    lifespan=lifespan
)


# =====================================================
# Home Endpoint
# =====================================================

@app.get("/")
def home():

    return {
        "message": "🚢 Vessel Arrival Delay Prediction API",
        "status": "Running",
        "version": "1.0.0"
    }


# =====================================================
# Health Check
# =====================================================

@app.get("/health")
def health():

    if model is None:

        raise HTTPException(
            status_code=500,
            detail="Model not loaded."
        )

    return {
        "status": "Healthy",
        "model_loaded": True
    }


# =====================================================
# Prediction Endpoint
# =====================================================

@app.post("/predict", response_model=PredictionResponse)
def predict(data: VoyageInput):

    try:

        # Convert request to DataFrame
        input_df = pd.DataFrame([data.model_dump()])

        # Prediction
        prediction = model.predict(input_df)[0]

        # Probability
        probability = model.predict_proba(input_df)[0]

        confidence = float(max(probability))

        delay_probability = float(probability[1])

        # Business-friendly response
        result = {
            "Prediction":
                "Delayed"
                if prediction == 1
                else "On Time",

            "Late_Arrival":
                int(prediction),

            "Delay_Probability":
                round(delay_probability, 4),

            "Confidence":
                round(confidence, 4),

            "Risk_Level":
                (
                    "High"
                    if delay_probability >= 0.80
                    else "Medium"
                    if delay_probability >= 0.50
                    else "Low"
                )
        }

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )