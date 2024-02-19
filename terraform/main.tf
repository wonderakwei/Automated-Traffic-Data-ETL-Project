# main.tf

# Create GCS bucket for backups
resource "google_storage_bucket" "backup_bucket" {
  name          = var.bucket_name
  location      = var.region
  force_destroy = true
}

# Create BigQuery dataset
resource "google_bigquery_dataset" "traffic_dataset" {
  dataset_id = var.dataset_id
  project    = var.project_id
}

# Create BigQuery table with schema
resource "google_bigquery_table" "traffic_table" {
  dataset_id = google_bigquery_dataset.traffic_dataset.dataset_id
  project    = var.project_id
  table_id   = var.table_id

  schema = file("C:\\Users\\DELL\\Documents\\Data Engineering\\DataMasters DE Bootcamp\\Week 3\\Traffic Project\\Traffic-ETL\\data\\schema.json")


}
