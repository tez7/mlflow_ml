import joblib
import pandas as pd
import os
import numpy as np
from pathlib import Path

#================ Prediction Pipeline use this to run direcly in terminal=================
# class PredictionPipeline:
#     def __init__(self, model_path: Path):
#         self.model_path = model_path
#         self.model = joblib.load(self.model_path)
#         print(f"Model loaded from {self.model_path}")

#     def predict(self, input_data: pd.DataFrame) -> np.ndarray:
#         predictions = self.model.predict(input_data)
#         return predictions
    
# TEST_DATA_PATH = r"C:\Users\raxx7\Documents\Python_Scripts\ml\mlflow\mlflow_ml\artifacts\data_transformation\test_scaled.csv"

# if __name__ == "__main__":
#     try:
#         pipeline = PredictionPipeline(model_path = r"C:\Users\raxx7\Documents\Python_Scripts\ml\mlflow\mlflow_ml\artifacts\model_trainer\model.joblib")

#         input_data = pd.read_csv(TEST_DATA_PATH)

#         input_features = input_data.drop('quality', axis=1, errors='ignore') 
        
#         # 3. Call predict with the input data
#         predictions = pipeline.predict(input_features)

#         print("\nPrediction successful.")
#         print(f"Shape of predictions: {predictions.shape}")
#         print(f"Predictions: {predictions}")

#     except Exception as e:
#         raise e
    
#================================================================

#================ Prediction Pipeline use this in Flask app=================
class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

    
    def predict(self, data):
        prediction = self.model.predict(data)

        return prediction