
```markdown
# Google Cloud Platform Configuration - Data Engineering Project

This document provides a step-by-step guide on setting up the Google Cloud Platform (GCP) environment for the Data Engineering Project, which involves uploading data to Google Cloud Storage (GCS) and loading it into BigQuery.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Configuration Steps](#configuration-steps)
  - [1. Create a GCP Project](#1-create-a-gcp-project)
  - [2. Enable APIs](#2-enable-apis)
  - [3. Create a GCS Bucket](#3-create-a-gcs-bucket)
  - [4. Set Up BigQuery](#4-set-up-bigquery)
  - [5. Create Service Account and Generate Credentials](#5-create-service-account-and-generate-credentials)
  - [6. Grant Permissions](#6-grant-permissions)
  - [7. Use Service Account in Terraform](#7-use-service-account-in-terraform)
- [Notes](#notes)
- [References](#references)

## Prerequisites

- Google Cloud Platform (GCP) account.
- `gcloud` CLI installed locally.
- [Terraform](https://www.terraform.io/downloads.html) installed on your machine.

## Configuration Steps

### 1. Create a GCP Project

Create a new project in the [Google Cloud Console](https://console.cloud.google.com/). Note the Project ID.

### 2. Enable APIs

Enable the following APIs in your project:

- Google Cloud Storage
- BigQuery

### 3. Create a GCS Bucket

Terraform will be used to create a GCS bucket in your project to store data.

### 4. Set Up BigQuery

Terraform will be used to create a dataset and table in BigQuery for storing the data.

### 5. Create Service Account and Generate Credentials

- Create a service account in the GCP Console.
- Download the JSON key file for the service account.

### 6. Grant Permissions

Grant necessary IAM roles to the service account:

- Storage Admin (for GCS)
- BigQuery Admin (for BigQuery)

### 7. Use Service Account in Terraform

Update `provider.tf` and `terraform.tfvars` in the Terraform script with the credentials JSON path:

```hcl
provider "google" {
  credentials = file("path/to/credentials.json")
  project     = "your-gcp-project-id"
  region      = "your-gcp-region"
}
```

## Notes

- Ensure that the service account used by Terraform has the required permissions.
- Verify API quotas to prevent unexpected issues.

## References

- [Google Cloud Console](https://console.cloud.google.com/)
- [Terraform Documentation](https://www.terraform.io/docs/index.html)
- [Google Cloud Storage API](https://cloud.google.com/storage/docs/json_api)
- [Google BigQuery API](https://cloud.google.com/bigquery/docs/reference/rest)
```