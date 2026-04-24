from src.Loggers import get_logger
from src.Exception import CustomException
import sys

logger = get_logger(__name__)
if __name__ == "__main__":
    logger.info("The logging function is working ")
    try:
        a = 10/0
    except Exception as e:
        error=CustomException(e,sys)
        logger.error(error)