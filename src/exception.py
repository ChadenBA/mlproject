import logging
import sys
#import logger  # Import the logger configuration
from src import logger
from src.logger import logging

def error_message_details(error, error_detail: sys):
    # Capture traceback information
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the filename where the error occurred
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message  # Return the formatted error message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Call the parent class's __init__
        # Get the detailed error message using the error and traceback info
        self.error_message = error_message_details(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message  # Return the custom error message when printing the exception


if __name__ == "__main__":
    try:
        # Deliberately cause a divide-by-zero error to trigger exception handling
        a = 1 / 0
    except Exception as e:
        # Log the error as an ERROR level message
        logging.error("An error occurred: %s", str(e))
        # Raise the custom exception to add more detailed error information
        raise CustomException(e, sys)
