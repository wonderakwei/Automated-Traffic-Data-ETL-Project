# Automated Traffic Data ETL Project

![Data Engineer](images/data_engineer.jpg)

## Overview

The Automated Traffic Data ETL Project streamlines the extraction, transformation, and loading of traffic data. It utilizes Python scripts to convert a spreadsheet (traffic_spreadsheet.xls) into .csv format, reformat the time column, and seamlessly upload the data to BigQuery through Google Cloud Storage (GCS). This project integrates Terraform for Infrastructure as Code (IaC), facilitating the provisioning of GCS and BigQuery resources. Furthermore, it employs APScheduler, a Python library, to schedule daily cron jobs, ensuring the automation of the entire process. The project also includes the creation of a Data Studio dashboard, offering a visual representation of traffic trends over time.

## Interview Questions

**Evaluation Criteria:** The code will be assessed based on results, cleanliness, and explanatory comments. Justifiable assumptions are allowed where necessary.

### Task

The objective is to upload the `traffic_spreadsheet.xls` to BigQuery for analysis. The provided script should cover both Python and Bash.

- Define appropriate bucket names and tables.
- Convert the file to .csv as BigQuery does not support .xls.
- Reformat the time column to YY-mm-dd HH:MM.
- Create a backup of the file in an S3 storage bucket in GCS.
- Automate the data upload to BigQuery from GCS.
- Optionally, generate a dashboard on Data (Looker) Studio displaying a traffic graph over time.
- The entire process should be automated to run daily via a cronjob.

## Project Structure

```plaintext
project_root/
│
├── data/
│   └── schema.json
│   └── traffic_spreadsheet.xls
│
├── docs/
│   └── apscheduler.md
│   └── datastudio.md
│   └── gcp.md
│   └── processing_and_upload.md
│   └── requirements.md
│   └── terraform.md
│   
├── images/
│   └── project_image.jpg
│
├── scripts/
│   ├── .env
│   ├── automated_pipeline.py
│   ├── data_transformation.py
│   ├── scheduler.py
│   └── upload_data_from__gcs_to_bigquery.py
│   └── upload_data_to_gcs.py
│
├── terraform/
│   ├── credentials.json
│   ├── main.tf
│   ├── provider.tf
│   ├── terraform.tfvars
│   └── variables.tf
│
├── README.md
│
└── requirements.txt
