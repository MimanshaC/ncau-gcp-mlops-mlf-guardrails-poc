project = "ncau-gcp-mlops-nprod-mlf-poc"

location = "australia-southeast1"

enable_apis = true

apis = [
    "artifactregistry.googleapis.com",
    "aiplatform.googleapis.com",
  ]

env = "nprod"

monitoring_project = "sincere-venture-162304"
