import os
from google.cloud import storage
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def upload_to_gcs():
    # Retrieve configuration from environment variables
    bucket_name = os.getenv("BUCKET_NAME")
    source_file_path = os.getenv("SOURCE_FILE_PATH")
    destination_blob_name = os.getenv("DESTINATION_BLOB_NAME")

    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_path)
        logging.info(f"File {source_file_path} uploaded to {destination_blob_name}.")
    except Exception as e:
        logging.error(f"Error occurred during upload: {e}")

# Upload the file
upload_to_gcs()
