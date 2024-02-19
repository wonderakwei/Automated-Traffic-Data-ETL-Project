
import pandas as pd
import logging
from datetime import datetime
import os
from google.cloud import storage
from google.cloud import bigquery
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Setting up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def convert_and_reformat_xls_to_csv(file_path, output_path):
    """
    Converts an XLS file to CSV and reformats the time column.

    :param file_path: Path to the XLS file.
    :param output_path: Path where the output CSV file will be saved.
    """
    try:
        # Reading the .xls file
        logging.info(f"Reading {file_path}")
        data = pd.read_excel(file_path)

        # Checking if 'time' column exists and reformatting
        if 'time' in data.columns:
            logging.info("Reformatting 'time' column")
            data['time'] = pd.to_datetime(data['time'], format='%d/%m/%Y %H:%M').dt.strftime('%Y-%m-%d %H:%M')
        else:
            logging.warning("'time' column not found in the data")

        # Saving to .csv
        data.to_csv(output_path, index=False)
        logging.info(f"File saved as {output_path}")

    except Exception as e:
        logging.error(f"Error occurred: {e}")

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

def load_data_from_gcs_to_bigquery():
    """
    Loads data from Google Cloud Storage to BigQuery.
    """
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
            skip_leading_rows=1,  # 1= header row present
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

def main():
    # File paths
    base_path = r'C:\Users\DELL\Documents\Data Engineering\DataMasters DE Bootcamp\Week 3\Traffic Project\Traffic-ETL\data'
    input_file = os.path.join(base_path, 'traffic_spreadsheet.xls')
    output_file = os.path.join(base_path, 'traffic_data.csv')

    # Convert and reformat the XLS file
    convert_and_reformat_xls_to_csv(input_file, output_file)

    # Upload the file to GCS
    upload_to_gcs()

    # Load data from GCS to BigQuery
    load_data_from_gcs_to_bigquery()

if __name__ == "__main__":
    main()
