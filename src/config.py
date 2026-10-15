import os
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Example of loading an optional environment variable
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
