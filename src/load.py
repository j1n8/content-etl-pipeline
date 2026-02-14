import os
import logging
from config import OUTPUT_DIR

logger = logging.getLogger(__name__)

def load(df):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_file = os.path.join(OUTPUT_DIR, "Arpatech.txt")

    logger.info("Writing output to %s", output_file)
    with open(output_file, "w", encoding="utf-8") as f:
        for _, row in df.iterrows():
            f.write(f"{row['base_group']}: {row['description']}\n\n")

    logger.info("ETL output successfully written")
