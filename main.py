import sys
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataValidationConfig, TrainingPipelineConfig, DataIngestionConfig,DataValidationConfig,DataTransformationConfig
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
        data_validation_config = DataValidationConfig(training_pipeline_config=trainingpipelineconfig)
        data_validation = DataValidation(data_ingestion_artifact=dataingestionartifact,
                                         data_validation_config=data_validation_config)
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info(f"Data validation artifact Complete: {data_validation_artifact}")
        print(data_validation_artifact)
        data_transformation_config = DataTransformationConfig(training_pipeline_config=trainingpipelineconfig)
        logging.info("Data Transformation started")
        data_transformation = DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact = data_transformation.initialize_data_transformation()
        print(data_transformation_artifact)
    except Exception as e:
        raise NetworkSecurityException(e, sys)