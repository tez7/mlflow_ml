from mlflow_ml import logger
import pandas as pd
import os
from sklearn.linear_model import ElasticNet
import joblib
from mlflow_ml.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train_model(self, X_train, y_train):
        model = ElasticNet(
            alpha=self.config.alpha,
            l1_ratio=self.config.l1_ratio,
            random_state=self.config.random_state
        )
        model.fit(X_train, y_train)
        return model

    def save_model(self, model):
        model_path = os.path.join(self.config.root_dir, self.config.model_name)
        joblib.dump(model, model_path)
        logger.info(f"Model saved at {model_path}")

    def main(self):
        # Load training and testing data
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        # Separate features and target variable
        X_train = train_data.drop(columns=[self.config.target_column],axis=1)
        y_train = train_data[self.config.target_column]

        X_test = test_data.drop(columns=[self.config.target_column],axis=1)
        y_test = test_data[self.config.target_column]

        # Train the model
        model = self.train_model(X_train, y_train)

        # Save the trained model
        self.save_model(model)