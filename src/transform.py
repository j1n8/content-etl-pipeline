import re
import logging
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

DUMMY_KEYWORDS = [
    "lorem ipsum",
    "dummy text",
    "unknown printer",
    "type specimen book"
]

def clean_description(text):
    if not text:
        return None

    text = BeautifulSoup(text, "html.parser").get_text()

    if any(word in text.lower() for word in DUMMY_KEYWORDS):
        return None

    return re.sub(r"\s+", " ", text).strip()

def transform(df):
    logger.info("Cleaning descriptions")
    df["description"] = df["description"].apply(clean_description)
    df = df.dropna(subset=["description"])

    logger.info("Grouping data")
    df["group_name"] = df["topic"].apply(lambda x: " ".join(x.split("_")[:2]))
    grouped = df.groupby("group_name")["description"].apply(" ".join).reset_index()

    grouped["base_group"] = grouped["group_name"].apply(lambda x: x.split()[0])
    final = grouped.groupby("base_group")["description"].apply(" ".join).reset_index()

    final = final[~final["base_group"].isin(["awsm", "w3tc"])]

    logger.info("Final grouped records: %d", len(final))
    return final
