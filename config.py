import os
from dotenv import load_dotenv

variables = load_dotenv()

BASE_URL = os.getenv("BASE_URL", "http://selenium1py.pythonanywhere.com/")
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", 5))