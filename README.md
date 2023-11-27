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

# Usage
To use the prediction model:
1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Train the model and save it as a pickle file by running the code in the provided script.
3. Run the FastAPI application by executing `python main.py`.
4. Make a POST request to `http://localhost:8000/predict_harvest_season` with the input data in the request body to get the predicted harvest season.

Please note that the input data should include the following fields: temperature, humidity, ph, water_availability, label, and Country.
