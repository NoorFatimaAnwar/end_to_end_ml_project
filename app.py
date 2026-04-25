from src.Loggers import get_logger
from src.Exception import CustomException
import sys
import pyodbc
from src.components.data_ingestion import DataIngestion
logger = get_logger(__name__)
if __name__ == "__main__":
    
    try:
       

       print(pyodbc.drivers())
       obj = DataIngestion()
       obj.initiate_data_ingestion()
    except Exception as e:
        error=CustomException(e,sys)
        logger.error(error)