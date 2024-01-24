variable "credentials" {
  description = "My Credentials"
  default     = "./keys/true-shore-412221-8719f38243a3.json"
}


variable "project" {
  description = "Project"
  default     = "true-shore-412221"
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "true_shore_412221_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "true-shore-412221-data-lake-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}