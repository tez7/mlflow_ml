from mlflow_ml.config.configuration import ConfigurationManager
from mlflow_ml import logger
from mlflow_ml.components.model_evaluation import ModelEvaluation

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config_manager = ConfigurationManager()
            model_evaluation_config = config_manager.get_model_evaluation_config()

            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.evaluate_metrics()

        except Exception as e:
            logger.exception(e)
            raise e

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = ModelEvaluationPipeline()
        pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise e