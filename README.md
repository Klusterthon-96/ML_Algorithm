# Crop Harvest Season Prediction

This repository contains code for predicting the harvest season of crops based on environmental factors. The prediction model is built using a Random Forest Classifier algorithm.

# Why Random Forest Classifier
Random Forest Classifier algorithm was chosen for this crop harvest season prediction model due to its capability to handle both numerical and categorical features effectively. Random Forest Classifier is an ensemble learning method that combines multiple decision trees to make predictions. It is known for its robustness, ability to handle high-dimensional data, and resistance to overfitting.

In the context of crop harvest season prediction, the dataset includes various environmental factors such as temperature, humidity, pH level, and water availability, along with categorical features like crop label and country. Random Forest Classifier's ability to handle both numerical and categorical features makes it a suitable choice for this prediction task.

By using Random Forest Classifier, the model can capture complex relationships between environmental factors and the harvest season of crops. It can handle non-linear relationships, feature interactions, and provide reliable predictions

# Dataset
The dataset used for training and testing the model is stored in the file `crop_Data.csv`. It contains information about the temperature, humidity, pH level, water availability, crop label, and country.

# Preprocessing
Before training the model, the dataset is preprocessed to transform the numerical and categorical features. The preprocessing steps include:

- Temperature Level: The temperature values are categorized into four levels - Cool, Mild, Warm, and Hot.
- Humidity Level: The humidity values are categorized into five levels - Low, Moderate, Average, High, and Very High.
- pH Level: The pH values are categorized into five levels - Strongly Acidic, Moderately Acidic, Neutral, Moderately Alkaline, and Highly Alkaline.
- Water Availability Level: The water availability values are categorized into three levels - Low, Moderate, and High.

# Model Training
The preprocessed dataset is split into training and testing sets using a test size of 20%. The numerical features are scaled using StandardScaler, and the categorical features are one-hot encoded using OneHotEncoder. The preprocessed features are then used to train a Random Forest Classifier model.

# Model Evaluation
The trained model is evaluated using the testing set. The accuracy score and the classification report are calculated to assess the performance of the model.

# Model Deployment
The trained model is saved as a pickle file named `crop_prediction_pipeline.pkl`. This file can be loaded to make predictions on new data.

A FastAPI application is implemented to provide a RESTful API for predicting the harvest season based on the input environmental factors. The API endpoint `/predict_harvest_season` accepts a POST request with the environmental factors as input and returns the predicted harvest season.

# Prerequisites

Before you begin, ensure you have Python 3.11.6 installed on your system. You can download Python from the official [Python website](https://www.python.org/downloads/).

# Usage
To use the prediction model:
1. Clone the repository:
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Train the model and save it as a pickle file by running the code in the provided script.
4. Run the FastAPI application by executing `python main.py`.This will start the API on `http://0.0.0.0:8000`

## Docker
 To use docker locally, follow these steps:

1.  Make sure that you have Docker installed on your system
2.  Run
```bash
docker compose up
```

# Endpoints

### 1. `/`

- **Method:** GET
- **Description:** Root endpoint to check if the API is running.
- **Example:** 
  ```bash
  curl http://0.0.0.0:8000/
  ```

### 2. `/predict_harvest_season`

- **Method:** POST
- **Description:** Predicts the harvest season based on provided environmental factors.
- **Request Body:**
  - `temperature`: Temperature in Celsius (float)
  - `humidity`: Humidity as a percentage (float)
  - `ph`: Soil pH level (float)
  - `water_availability`: Water availability (float)
  - `label`: Crop label (string)
  - `Country`: Country name (string)
- **Example Request:**
  ```bash
  curl -X POST "http://0.0.0.0:8000/predict_harvest_season" -H "Content-Type: application/json" -d '{"temperature": 25.5, "humidity": 60.0, "ph": 6.5, "water_availability": 0.8, "label": "maize", "Country": "Nigeria"}'
  ```
- **Example Response:**
  ```json
  {"harvest_season": "Spring"}
  ```

### Data Defination
  | Feature               | Possible Values                                                                                          |
|-----------------------|----------------------------------------------------------------------------------------------------------|
| Temperature           | 15 and above (float)                                                                                    |
| Humidity              | 0 and above (float)                                                                                     |
| pH                    | 0 - 14 (float)                                                                                          |
| Water Availability    | 0 and above (float)                                                                                     |
| Label                 | "blackgram", "chickpea", "cotton", "jute", "kidneybeans", "lentil", "maize", "mothbeans", "mungbean", "muskmelon", "pigeonpeas", "rice", "watermelon" (string) |
| Country               | "Kenya", "Nigeria", "South Africa", "Sudan" (string)                                                   |

Feel free to use this table as a reference when preparing your input data for the `/predict_harvest_season` endpoint. Each column represents a feature with its corresponding possible values. Adjust the values accordingly based on your specific use case.


Feel free to explore and integrate this API into your applications for crop prediction based on environmental conditions!
