import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import pandas as pd

with open("crop_prediction_pipeline.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

class HarvestPredictionRequest(BaseModel):
    temperature: float
    humidity: float
    ph: float
    water_availability: float
    label: str
    Country: str

@app.get('/')
def read_root():
    return {"message": "Welcome to the Crop Prediction API!"}

@app.post("/predict_harvest_season")
def predict_harvest_season(request: HarvestPredictionRequest):
    request_dict = vars(request)
    request_dict['water availability'] = request_dict.pop('water_availability')
    # Create a DataFrame from the request data
    input_data = pd.DataFrame([vars(request)])
    
    # Use the model to make predictions
    prediction = model.predict(input_data)
    
    # Return the predicted harvest season
    return {"harvest_season": prediction[0]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
