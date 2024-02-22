from text_summarizer.pipeline.stagee_01_data_ingestion import DataIngestionTrainingPipeline
from text_summarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from text_summarizer.logging import logger

logger.info("Welcome to custom text summarizer package")

STAGE_NAME = "STAGE_01_DATA_INGESTION"

try:
    logger.info(f">>>>>> Starting {STAGE_NAME}... ")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> {STAGE_NAME} completed successfully.")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "STAGE_02_DATA_VALIDATION"
try:
    logger.info(f">>>>>> Starting {STAGE_NAME}... ")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> {STAGE_NAME} completed successfully.")
except Exception as e:
    logger.exception(e)
    raise e