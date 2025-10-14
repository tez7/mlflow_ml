from mlflow_ml.components.data_validation import DataValiadtion
from mlflow_ml.config.configuration import ConfigurationManager
from mlflow_ml import logger


STAGE_NAME = "Data Validation Stage"

# pipeline

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValiadtion(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = DataValidationPipeline()
        pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise e