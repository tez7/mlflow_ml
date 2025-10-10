import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" # log format

log_dir = "logs" # directory to store log files
log_filepath = os.path.join(log_dir,"running_logs.log") # log file name
os.makedirs(log_dir, exist_ok=True) # create log directory if not exists


logging.basicConfig(
    level= logging.INFO, # log level
    format= logging_str, # log format

    handlers=[
        logging.FileHandler(log_filepath), # write log to file
        logging.StreamHandler(sys.stdout) # print log at terminal as well
    ]
)

logger = logging.getLogger("mlflowProjectLogger") # custom logger for this project