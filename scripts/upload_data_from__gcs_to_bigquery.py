from google.cloud import bigquery
import logging
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_data_from_gcs_to_bigquery():
    # Retrieve configuration from environment variables
    bucket_name = os.getenv("BUCKET_NAME")
    blob_name = os.getenv("BLOB_NAME")
    dataset_id = os.getenv("DATASET_ID")
    table_id = os.getenv("TABLE_ID")
    project_id = os.getenv("PROJECT_ID")

    try:
        # Create a BigQuery client object with the specified project
        client = bigquery.Client(project=project_id)

        # Configure the load job
        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,  # Assumes header row present
            autodetect=False,      # Auto-detect schema
        )

        # Construct the URI for the GCS location
        uri = f"gs://{bucket_name}/{blob_name}"

        # Load job
        load_job = client.load_table_from_uri(
            uri,
            f"{dataset_id}.{table_id}",
            job_config=job_config
        )

        # Wait for the job to complete
        load_job.result()
        logging.info(f"Job finished. Loaded data from {uri} into {dataset_id}.{table_id}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Load the data
load_data_from_gcs_to_bigquery()
