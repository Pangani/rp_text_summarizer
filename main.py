from text_summarizer.pipeline.stagee_01_data_ingestion import DataIngestionTrainingPipeline
from text_summarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from text_summarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from text_summarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from text_summarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from text_summarizer.logging import logger

logger.info("Welcome to custom text summarizer package")

STAGE_NAME = "DATA_INGESTION -01"

try:
    logger.info(f">>>>>> Starting {STAGE_NAME}... ")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> {STAGE_NAME} completed successfully.")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "DATA_VALIDATION - 02"
try:
    logger.info(f">>>>>> Starting {STAGE_NAME}... ")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> {STAGE_NAME} completed successfully.")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "DATA_TRANSFORMATION - 03"
try:
    logger.info(f">>>>>> Starting {STAGE_NAME}... ")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> {STAGE_NAME} completed successfully.")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "MODEL_TRAINER - 04"
try:
    logger.info(f"******************************** ")
    logger.info(f">>>>>> Starting {STAGE_NAME}... ")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> {STAGE_NAME} completed successfully.***********")
except Exception as e:
    logger.exception(e)
    raise e

TAGE_NAME = "MODEL_EVALUATION 05"
try:
    logger.info(f"******************************** ")
    logger.info(f">>>>>> Starting {STAGE_NAME}... ")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>>> {STAGE_NAME} completed successfully.***********")
except Exception as e:
    logger.exception(e)
    raise e