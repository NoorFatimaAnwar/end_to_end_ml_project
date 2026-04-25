import pandas as pd
from src.Exception import CustomException
from src.Loggers import get_logger
import os
import sys
from sklearn.model_selection import train_test_split
from src.utilis import read_sql_data

logger = get_logger(__name__)

class DataIngestionConfig:
    artifact_dir = "artifacts"
    raw_data_path = os.path.join(artifact_dir, "raw.csv")
    train_data_path = os.path.join(artifact_dir, "train.csv")
    test_data_path = os.path.join(artifact_dir, "test.csv")


class DataIngestion:

    def __init__(self):
        self.config = DataIngestionConfig()

    def initiate_data_ingestion(self):

        try:
            # Create artifact folder
            os.makedirs(self.config.artifact_dir, exist_ok=True)

            logger.info("Reading data from SQL Server...")

            df = read_sql_data("customer_features")

            logger.info("Data read successfully")

            # Save raw data
            df.to_csv(self.config.raw_data_path, index=False)
            logger.info("Raw data saved")

            # Train Test Split
            train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

            # Save splits
            train_data.to_csv(self.config.train_data_path, index=False)
            test_data.to_csv(self.config.test_data_path, index=False)

            logger.info("Train-test split done and saved")

            return (
                self.config.train_data_path,
                self.config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)


