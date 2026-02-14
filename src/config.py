import os

DB_CONFIG = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "database": os.getenv("DB_NAME")
}

OUTPUT_DIR = os.getenv("OUTPUT_DIR", "/app/output")
MIN_SPACES = int(os.getenv("MIN_SPACES", 5))
