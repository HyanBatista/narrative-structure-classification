import os
import json
import logging
from pandas import DataFrame
from pathlib import Path
from torch.utils.data import DataLoader

from google.cloud import storage


logger = logging.getLogger(__name__)


class DataFetcher:
    def __call__(self, bucket_name: str, blob_name: str, target_path: Path) -> None:
        # Create a Path object from a string
        target_path = Path(target_path)

        if not os.path.exists(target_path):
            # Instantiate a client
            client = storage.Client()

            # Get a reference to the blob
            bucket = client.bucket(bucket_name)
            blob = bucket.blob(blob_name)

            # Download the blob to a file
            blob.download_to_filename(target_path)

            logger.info(f"File {target_path.name} downloaded successfully.")
        else:
            logger.info(
                f"File {target_path.name} already exists in {target_path.parent.name}."
            )
