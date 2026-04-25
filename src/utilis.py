import pandas as pd
import pyodbc
import os
import sys
from dotenv import load_dotenv
from src.Exception import CustomException
from src.Loggers import get_logger

logger = get_logger(__name__)

load_dotenv()


def read_sql_data(table: str):
    """
    Read data using Windows Authentication (SQL Server)
    """

    try:
        server = os.getenv("DB_SERVER")
        database = os.getenv("DB_NAME")
        driver = os.getenv("DB_DRIVER")

        logger.info("Establishing connection using Windows Authentication")

        connection_string = f"""
            DRIVER={{{driver}}};
            SERVER={server};
            DATABASE={database};
            Trusted_Connection=yes;
            TrustServerCertificate=yes;
        """

        conn = pyodbc.connect(connection_string)

        query = f"SELECT * FROM {table}"

        df = pd.read_sql(query, conn)

        conn.close()

        logger.info("Data fetched successfully")

        return df

    except Exception as e:
        logger.error("Database connection failed")
        raise CustomException(e, sys)