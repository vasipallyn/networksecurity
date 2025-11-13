import logging
import os
from datetime import datetime

## log file format
LOG_FILE=f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log" 

## log file path
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
 ##creating the above logs folder,if file already exists, not created again
os.makedirs(logs_path,exist_ok=True)

## total path
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

## logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)