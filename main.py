import sys
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException

from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact
if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(training_pipeline_config=trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Starting data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info(f"Data ingestion artifact: {dataingestionartifact}")
        print(dataingestionartifact)
    except Exception as e:
        raise NetworkSecurityException(e, sys)