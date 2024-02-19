# variables.tf

variable "credentials_path" {
  description = "Path to the GCP credentials file"
}

variable "project_id" {
  description = "GCP Project ID"
}

variable "region" {
  description = "GCP region for resources"
}

variable "bucket_name" {
  description = "GCS bucket name"
}

variable "dataset_id" {
  description = "BigQuery dataset ID"
}

variable "table_id" {
  description = "BigQuery table ID"
}
