from mlflow_ml import logger
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
from sklearn.model_selection import train_test_split
import pandas as pd
from mlflow_ml.entity.config_entity import DataTransformationConfig
import os


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config


    def train_test_spliting(self):
        """Loads data and splits it into training and test sets."""
        data = pd.read_csv(self.config.data_path)

        # Ensure target_column is extracted here from the config object
        self.target_column = self.config.target_column

        # Split the data into training and test sets. (0.75, 0.25) split.
        # This splits the *entire* dataset first
        train_df, test_df = train_test_split(data, test_size=0.25, random_state=42)

        # Save the RAW (unscaled) split data
        train_df.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test_df.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        # Store for the next step (scaling)
        self.train_data = train_df
        self.test_data = test_df

        logger.info("Split data into initial training and test sets.")
        logger.info(f"Train shape: {train_df.shape}")
        logger.info(f"Test shape: {test_df.shape}")
    
    def scale_and_save(self):
        """
        Applies feature scaling (StandardScaler) to the data and saves 
        the processed (scaled) train and test sets.
        """
        # Ensure splitting has been done
        if not hasattr(self, 'train_data') or not hasattr(self, 'test_data'):
            self.train_test_spliting()

        train = self.train_data.copy()
        test = self.test_data.copy()

        # 1. Separate Features (X) and Target (y)
        X_train = train.drop(columns=[self.target_column])
        y_train = train[self.target_column]

        X_test = test.drop(columns=[self.target_column])
        y_test = test[self.target_column]
        
        # Identify Columns for Scaling (all features except the target)
        feature_columns = X_train.columns

        # 2. Initialize and Fit Scaler on TRAIN Data ONLY
        scaler = StandardScaler()
        
        # Fit on X_train and transform X_train
        X_train_scaled = scaler.fit_transform(X_train[feature_columns])
        
        # 3. Transform TEST Data (using the scaler fitted on X_train)
        X_test_scaled = scaler.transform(X_test[feature_columns])

        # 4. Reconstruct DataFrames
        # Convert the scaled arrays back to DataFrames, preserving index
        X_train_scaled_df = pd.DataFrame(X_train_scaled, columns=feature_columns, index=X_train.index)
        X_test_scaled_df = pd.DataFrame(X_test_scaled, columns=feature_columns, index=X_test.index)
        
        # Recombine features with the target column
        train_processed = pd.concat([X_train_scaled_df, y_train], axis=1)
        test_processed = pd.concat([X_test_scaled_df, y_test], axis=1)

        # 5. Save Processed Data (Scaled)
        # Save the SCALED data to new CSV files
        train_processed.to_csv(os.path.join(self.config.root_dir, "train_scaled.csv"), index=False)
        test_processed.to_csv(os.path.join(self.config.root_dir, "test_scaled.csv"), index=False)

        # logger.info(f"Scaled and saved processed train data.")
        # logger.info(f"Scaled and saved processed test data.")
        
        print(f"Scaled Train shape: {train_processed.shape}")
        print(f"Scaled Test shape: {test_processed.shape}")
