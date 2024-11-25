import yaml
from data_importer.api_client import APIClient
from data_importer.db import Database
from data_importer.logger import get_logger

logger = get_logger(__name__)

def load_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

def main():
    config = load_config()
    api_client = APIClient(config["api"]["url"])
    db = Database(config["database"])

    data = api_client.fetch_data()
    if not data:
        logger.error("No data fetched from the API.")
        return

    for item in data:
        phone_id = item["id"]
        phone_name = item.get("name")
        phone_data = item.get("data", {})
        db.insert_phone_data(phone_id, phone_name, phone_data)

    logger.info("Data import completed successfully.")

if __name__ == "__main__":
    main()
