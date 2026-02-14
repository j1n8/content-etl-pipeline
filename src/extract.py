import mysql.connector
import pandas as pd
import logging
from config import DB_CONFIG, MIN_SPACES

logger = logging.getLogger(__name__)

QUERY = f"""
SELECT DISTINCT meta_key, meta_value
FROM wp_postmeta
WHERE meta_key NOT LIKE '\\_%'
  AND meta_value IS NOT NULL
  AND CHAR_LENGTH(meta_value) > 5
  AND (LENGTH(TRIM(meta_value)) - LENGTH(REPLACE(TRIM(meta_value), ' ', ''))) >= {MIN_SPACES}
"""

def extract():
    logger.info("Connecting to source database")
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    logger.info("Executing extraction query")
    cursor.execute(QUERY)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    df = pd.DataFrame(rows, columns=["topic", "description"])
    logger.info("Extracted %d rows", len(df))
    return df
