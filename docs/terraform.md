

```markdown
# Data Engineering Project - Infrastructure as Code with Terraform

## Overview

This project focuses on automating the infrastructure setup for a data engineering pipeline using Terraform. The pipeline involves uploading data to Google Cloud Storage (GCS) and loading it into BigQuery.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Instructions](#instructions)
- [Notes](#notes)
- [References](#references)

## Prerequisites

- [Terraform](https://www.terraform.io/downloads.html) installed on your machine.
- Google Cloud Platform (GCP) account with appropriate credentials.
- Enabled APIs: Google Cloud Storage, BigQuery.

## Project Structure

- `main.tf`: Main Terraform script for setting up GCS bucket and BigQuery dataset and table.
- `provider.tf`: Defines the GCP provider configuration.
- `variables.tf`: Defines input variables used in the Terraform script.
- `terraform.tfvars`: File to store specific variable values.
- `data/`: Contains the data files to be uploaded.

## Configuration

Update the variables in `variables.tf` and `terraform.tfvars` with your specific configurations:

```hcl
# variables.tf
variable "bucket_name" {
  description = "Name of the GCS bucket"
}

variable "dataset_id" {
  description = "BigQuery dataset ID"
}

variable "table_id" {
  description = "BigQuery table ID"
}

variable "project_id" {
  description = "Google Cloud project ID"
}

variable "region" {
  description = "GCP region for the storage bucket"
}

# terraform.tfvars

create a `terraform.tfvars` file within the terraform folder and update the following configurations:
bucket_name = "your-gcs-bucket-name"
dataset_id = "your-bigquery-dataset-id"
table_id = "your-bigquery-table-id"
project_id = "your-gcp-project-id"
region = "your-gcp-region"
```

## Instructions

1. Clone this repository:

2. Update the configuration variables in `variables.tf` and `terraform.tfvars`.

3. Run Terraform commands ( make sure you are in the terraform directory):

   ```bash
   terraform init
   terraform apply
   ```

4. Follow the on-screen prompts to apply changes.

## Notes

- Ensure that the necessary Google Cloud APIs are enabled for the project.
- Permissions: Make sure the service account used by Terraform has the required permissions.

## References

- [Terraform Documentation](https://www.terraform.io/docs/index.html)
- [Google Cloud Storage API](https://cloud.google.com/storage/docs/json_api)
- [Google BigQuery API](https://cloud.google.com/bigquery/docs/reference/rest)
```
