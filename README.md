# 🚢 Vessel Arrival Delay Prediction using Machine Learning

An end-to-end Machine Learning project that predicts whether a vessel will arrive late based on operational, environmental, and voyage-related factors.

The project demonstrates the complete Data Science lifecycle—from synthetic data generation and exploratory analysis to model deployment using FastAPI and Docker.

---

## 📌 Project Overview

Late vessel arrivals can disrupt global supply chains, increase operational costs, and impact customer satisfaction.

This project uses Machine Learning to predict vessel arrival delays before the voyage is completed, enabling logistics teams to proactively manage risks.

The project includes:

- Synthetic dataset generation
- Exploratory Data Analysis (EDA)
- Data Cleaning
- Feature Engineering
- Machine Learning Model Training
- Hyperparameter Optimization
- Model Explainability using SHAP
- REST API with FastAPI
- Docker Containerization
- Streamlit Dashboard (Optional)

---

# 🚀 Business Problem

Shipping companies face delays due to multiple operational factors such as:

- Port congestion
- Bad weather
- Departure delays
- Historical route performance
- Cargo load
- Vessel characteristics

Accurately predicting delays allows operators to:

- Improve ETA estimation
- Optimize scheduling
- Reduce operational costs
- Improve customer communication
- Support proactive decision-making

---

# 🛠 Tech Stack

### Programming

- Python 3.11+

### Data Processing

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-learn

Models evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

### Model Explainability

- SHAP

### API

- FastAPI
- Pydantic

### Deployment

- Docker
- Docker Compose

### Frontend (Optional)

- Streamlit

---

# 📂 Project Structure

```text
Vessel-Arrival-Delay-Prediction/

│
├── api/
│   ├── app.py
│   ├── schemas.py
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── final_model.pkl
│   └── preprocessor.pkl
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   ├── 04_Preprocessing.ipynb
│   ├── 05_Model_Building.ipynb
│   ├── 06_Model_Optimization.ipynb
│   └── 07_Model_Explainability.ipynb
│
├── reports/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# 📊 Dataset

This project uses a **synthetically generated maritime logistics dataset** containing realistic vessel operations.

### Features include:

| Feature | Description |
|----------|-------------|
| Carrier | Shipping company |
| Vessel Type | Container, Bulk, Tanker |
| Origin Port | Departure port |
| Destination Port | Arrival port |
| Distance_NM | Distance in nautical miles |
| Scheduled Transit Days | Planned voyage duration |
| Departure Delay Hours | Delay before departure |
| Average Speed | Vessel cruising speed |
| Vessel Age | Age of vessel |
| Cargo Load Percentage | Vessel utilization |
| Port Congestion Index | Congestion score |
| Weather Severity | Weather score |
| Fuel Price | Fuel cost |
| Historical Route Delay | Historical average delay |
| Season | Voyage season |
| Customs Clearance Risk | Customs risk level |

---

# 🎯 Target Variable

```
Late_Arrival
```

Binary Classification

- 0 → On Time
- 1 → Delayed

---

# 🔍 Exploratory Data Analysis

Performed:

- Missing value analysis
- Duplicate detection
- Distribution analysis
- Correlation heatmap
- Boxplots
- Histograms
- Countplots
- Outlier detection

---

# 🧹 Data Cleaning

Performed:

- Missing value treatment
- Duplicate removal
- Outlier treatment
- Data type validation

---

# ⚙ Feature Engineering

Created new business-oriented features:

- Route
- Congestion Level
- Weather Category
- Vessel Age Group
- Load Category
- Speed Category
- Delay Risk Score

These engineered features improve model performance by incorporating domain knowledge.

---

# 🤖 Machine Learning Workflow

The following models were trained and evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

Evaluation metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

The best-performing model was selected and optimized using RandomizedSearchCV.

---

# 📈 Model Explainability

Model explanations were generated using SHAP.

Included:

- SHAP Summary Plot
- SHAP Waterfall Plot
- SHAP Feature Importance
- Individual Prediction Explanation

This helps explain why a voyage is predicted as delayed.

---

# 🌐 FastAPI REST API

### Endpoints

### GET /

Returns API status.

---

### GET /health

Checks model health.

---

### POST /predict

Predict vessel arrival delay.

Example Request:

```json
{
  "Carrier": "Maersk",
  "Vessel_Type": "Container",
  "Origin_Port": "Singapore",
  "Destination_Port": "Rotterdam",
  "Distance_NM": 8200,
  "Scheduled_Transit_Days": 22,
  "Departure_Delay_Hours": 8,
  "Average_Speed_Knots": 18,
  "Vessel_Age": 10,
  "Cargo_Load_Percentage": 85,
  "Port_Congestion_Index": 70,
  "Weather_Severity": 6,
  "Fuel_Price_USD": 650,
  "Historical_Route_Delay": 12,
  "Season": "Summer",
  "Customs_Clearance_Risk": "Medium",
  "Route": "Singapore → Rotterdam",
  "Congestion_Level": "High",
  "Weather_Category": "Moderate",
  "Vessel_Age_Group": "Mid Age",
  "Load_Category": "High",
  "Speed_Category": "Normal",
  "Delay_Risk_Score": 26.6
}
```

Example Response:

```json
{
  "Prediction": "Delayed",
  "Late_Arrival": 1,
  "Delay_Probability": 0.94,
  "Confidence": 0.96,
  "Risk_Level": "High"
}
```

---

# 🐳 Docker

Build Docker image

```bash
docker build -t vessel-delay-api .
```

Run container

```bash
docker run -p 8000:8000 vessel-delay-api
```

---

# ▶ Running the Project

Clone the repository

```bash
git clone https://github.com/<your-username>/Vessel-Arrival-Delay-Prediction.git
```

Move into project

```bash
cd Vessel-Arrival-Delay-Prediction
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
uvicorn api.app:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

# 📈 Future Improvements

- Deploy on Render / Azure / AWS
- CI/CD using GitHub Actions
- MLflow Experiment Tracking
- Automated Retraining Pipeline
- Monitoring Dashboard
- Real-world AIS vessel data integration

---

# 👨‍💻 Author

**Rufiyea**

Data Scientist | Machine Learning Enthusiast

GitHub: https://github.com/Rufiyea27

LinkedIn: https://www.linkedin.com/in/rufiyeacarassco/

---

# ⭐ Acknowledgements

This project was developed as an end-to-end Machine Learning portfolio project to demonstrate:

- Data Analysis
- Feature Engineering
- Machine Learning
- Explainable AI
- API Development
- Docker
- MLOps fundamentals

---

## 📜 License

This project is licensed under the MIT License.
