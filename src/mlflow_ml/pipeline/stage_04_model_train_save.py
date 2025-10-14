from mlflow_ml.config.configuration import ConfigurationManager
from mlflow_ml import logger
from mlflow_ml.components.model_train_save import ModelTrainer

STAGE_NAME = "Model Train and Save Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()

            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.main()
        except Exception as e:
            logger.exception(e)
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = ModelTrainerPipeline()
        pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise e