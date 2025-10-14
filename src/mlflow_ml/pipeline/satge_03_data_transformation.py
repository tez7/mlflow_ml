from mlflow_ml.config.configuration import ConfigurationManager
from mlflow_ml import logger
from mlflow_ml.components.data_transformation import DataTransformation



STAGE_NAME = "Data Transformation Stage"


class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            # check status first from artifacts/data_validation/STATUS_FILE.txt
            # if status is ok/True then only proceed for data transformation
            with open("artifacts/data_validation/status.txt", "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                # 1. Get configuration
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                
                # 2. Execute component
                data_transformation = DataTransformation(config=data_transformation_config)
                
                # Perform split and save raw data
                data_transformation.train_test_spliting()
                
                # Perform scaling and save scaled data
                data_transformation.scale_and_save()
            else:
                logger.info("Data Validation status is not ok. Data Transformation will not proceed.")
                raise Exception("Data Validation status is not ok. Data Transformation will not proceed.")
            
        except Exception as e:
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = DataTransformationPipeline()
        pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise e