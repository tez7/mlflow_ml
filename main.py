from mlflow_ml import logger # i can do from scr.mlflow_ml import logger but didn't do bcoz i mentioned logger inside constructor so need to give folder
from mlflow_ml.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlflow_ml.pipeline.stage_02_data_validation import DataValidationPipeline
from mlflow_ml.pipeline.satge_03_data_transformation import DataTransformationPipeline
from mlflow_ml.pipeline.stage_04_model_train_save import ModelTrainerPipeline
from mlflow_ml.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

from dotenv import load_dotenv
load_dotenv() 

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise e

STAGE_NAME = "Model Train and Save Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    traininig = ModelTrainerPipeline()
    traininig.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise e

STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    evaluation = ModelEvaluationPipeline()
    evaluation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise e