import logging
import os
from datetime import datetime


if not os.path.exists("logs"):
    os.mkdir("logs")


logger = logging.getLogger("test_logger")
logger.setLevel(logging.INFO)


run_time = datetime.now().strftime("%Y%m%d_%H%M%S")
file_handler = logging.FileHandler(
    f"logs/test_{run_time}.log",
    mode="w",
    encoding="utf-8"
)


formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(message)s"
)

file_handler.setFormatter(formatter)


logger.addHandler(file_handler)