import logging
import os
from datetime import datetime

# Create a log file name with the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")

# Create logs directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Define the full path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,  # Set the logging level to capture INFO and ERROR messages
)

if __name__ == "__main__":
    logging.info("Logging has started")
