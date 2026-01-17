variable "aws_region" {
  default = "ap-southeast-1" # Bangkok/Singapore region for low latency
}

variable "project_name" {
  default = "overlord-ai"
}

variable "environment" {
  default = "production"
}

variable "db_password" {
  description = "RDS Root Password"
  type        = string
  sensitive   = true
}