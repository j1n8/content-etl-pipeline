import logging
from extract import extract
from transform import transform
from load import load

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def main():
    logging.info("Starting ETL pipeline")
    df = extract()
    df_final = transform(df)
    load(df_final)
    logging.info("ETL pipeline completed successfully")

if __name__ == "__main__":
    main()
