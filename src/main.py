import os
import logging
from data import DataFetcher


# Setup logging
stream_handler = logging.StreamHandler()

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s:%(asctime)s:%(message)s',
    handlers=[stream_handler,]
)


def main() -> None:
    bucket_name = os.getenv('BUCKET_NAME')
    blob_name = os.getenv('BLOB_NAME')
    target_path = "src/artifacts/data/ndc/dataset.json"
    DataFetcher()(bucket_name, blob_name, target_path)


if __name__ == "__main__":
    main()
