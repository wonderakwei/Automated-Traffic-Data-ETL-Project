
```markdown
# Data Upload Process - Google Cloud Platform

This document provides a step-by-step guide on the process of uploading data to various destinations in Google Cloud Platform (GCP). The process involves setting up Application Default Credentials, configuring the Google Cloud SDK, and running Python scripts for data transformation, uploading to Google Cloud Storage (GCS), and loading into BigQuery.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Google Cloud CLI Configuration](#google-cloud-cli-configuration)
  - [1. Set Up Application Default Credentials](#1-set-up-application-default-credentials)
  - [2. Set a Default Project for Google Cloud SDK](#2-set-a-default-project-for-google-cloud-sdk)
  - [3. Set Quota Project](#3-set-quota-project)
- [Python Scripts](#python-scripts)
  - [1. data_transformation.py](#1-data_transformationpy)
  - [2. upload_data_to_gcs.py](#2-upload_data_to_gcspy)
  - [3. upload_data_from__gcs_to_bigquery.py](#3-upload_data_from__gcs_to_bigquerypy)
- [.env File](#env-file)
- [Instructions](#instructions)

## Prerequisites

- Google Cloud Platform (GCP) account.
- Python installed on your machine.
- Google Cloud SDK installed.
- Service account JSON key file for authentication.
- Data files to be uploaded.

## Google Cloud CLI Configuration

### 1. Set Up Application Default Credentials

Ensure that Application Default Credentials (ADC) are set up. Run the following command:

```bash
gcloud auth application-default login
```

### 2. Set a Default Project for Google Cloud SDK

Set a default project for the Google Cloud SDK:

```bash
gcloud config set project your-gcp-project-id
```

### 3. Set Quota Project

Set the quota project for the active project:

```bash
gcloud auth application-default set-quota-project your-gcp-project-id
```

## Python Scripts

### 1. data_transformation.py

This script performs data transformations on the input data. Adjust the script according to your data transformation requirements.

Usage:

`python scripts/data_transformation.py`

### 2. upload_data_to_gcs.py

This script uploads data from a local file to a Google Cloud Storage (GCS) bucket. Update the .env file with the necessary details:

```env
BUCKET_NAME=your-gcs-bucket-name
BLOB_NAME=your-blob-name
DATASET_ID=your-bigquery-dataset-id
TABLE_ID=your-bigquery-table-id
PROJECT_ID=your-gcp-project-id
SOURCE_FILE_PATH=your-source-file-path
DESTINATION_BLOB_NAME=your-destination-blob-name
```

Usage:

`python scripts/upload_data_to_gcs.py`

### 3. upload_data_from__gcs_to_bigquery.py

This script loads data from GCS to BigQuery. Update the .env file with the necessary details.

## .env File

Create a `.env` file in the root directory with the following content:

```env
BUCKET_NAME=your-gcs-bucket-name
BLOB_NAME=your-blob-name
DATASET_ID=your-bigquery-dataset-id
TABLE_ID=your-bigquery-table-id
PROJECT_ID=your-gcp-project-id
SOURCE_FILE_PATH=your-source-file-path
DESTINATION_BLOB_NAME=your-destination-blob-name
```
Usage:

`python scripts/upload_data_from_gcs_to_bigquery.py`

## Instructions

1. Ensure all prerequisites are met.
2. Configure the Google Cloud CLI as described above.
3. Run the Python scripts with the appropriate parameters.

```