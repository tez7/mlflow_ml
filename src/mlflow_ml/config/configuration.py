
from mlflow_ml.constants import *
from mlflow_ml.utils.common import read_yaml, create_directories
from mlflow_ml.entity.config_entity import DataIngestionConfig

# Configuration Manager
# This class will read the config.yaml and params.yaml file and provide the necessary configuration for different components of the project
# It will also create the necessary directories for the project
# It will also validate the config.yaml and params.yaml file against the schema.yaml file
class ConfigurationManager:
    def __init__(
        self,
        config_filepath: Path = CONFIG_FILE_PATH,
        params_filepath: Path = PARAMS_FILE_PATH,
        schema_filepath: Path = SCHEMA_FILE_PATH,
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        create_directories([Path(self.config.artifacts_root)])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([Path(config.root_dir)])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir),
        )

        return data_ingestion_config
    
    # def get_data_validation_config(self):
    #     config = self.config.data_validation

    #     create_directories([Path(config.root_dir)])
    #     data_validation_config = {
    #         "root_dir": Path(config.root_dir),
    #         "unzip_data_dir": Path(config.unzip_data_dir),
    #         "STATUS_FILE": Path(config.STATUS_FILE)
    #     }
    #     return data_validation_config