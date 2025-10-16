from mlflow_ml import logger
import pandas as pd
import os
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
import mlflow.sklearn
from urllib.parse import urlparse
import joblib
from mlflow_ml.entity.config_entity import ModelEvaluationConfig
from mlflow_ml.utils.common import save_json
import mlflow
from pathlib import Path

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        mlflow.set_tracking_uri(self.config.mlflow_uri)
        logger.info(f"MLflow Tracking URI set to: {self.config.mlflow_uri}")

    def evaluate_metrics(self):
        # Load test data
        test_data = pd.read_csv(self.config.test_data_path)
        X_test = test_data.drop(columns=[self.config.target_column], axis=1)
        y_test = test_data[self.config.target_column]

        # Load the trained model
        model = joblib.load(self.config.model_path)

        # Make predictions
        y_pred = model.predict(X_test)

        # Calculate metrics
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        metrics = {
            "MSE": mse,
            "RMSE": rmse,
            "MAE": mae,
            "R2": r2
        }

        # Save metrics to a file (outside the MLflow block, cleaner)
        save_json(path=Path(self.config.metric_file_name), data=metrics)

        # MLFLOW LOGGING BLOCK
        # Set registry URI (often the same as tracking URI)
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type = urlparse(mlflow.get_tracking_uri()).scheme

        # Log metrics to MLflow
        with mlflow.start_run():
            # Log all calculated metrics at once
            mlflow.log_metrics(metrics) 
            
            # Log parameters from the config
            mlflow.log_params(self.config.all_parameters)
            
            # Log the model
            mlflow.sklearn.log_model(model, "model")

            # FIX: Variable name must be correct
            # Model registry only works if the URI is not a local file store
            if tracking_url_type != "file":
                # Register the model
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")