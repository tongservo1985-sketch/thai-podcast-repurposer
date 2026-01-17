# Media Storage for Thai Podcasts
resource "aws_s3_bucket" "media_storage" {
  bucket = "${var.project_name}-media-assets"
}

# Block public access (Security Requirement)
resource "aws_s3_bucket_public_access_block" "media_storage_block" {
  bucket = aws_s3_bucket.media_storage.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# Encryption at rest
resource "aws_s3_bucket_server_side_encryption_configuration" "media_storage_encryption" {
  bucket = aws_s3_bucket.media_storage.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# Lifecycle policy: Move raw audio to Glacier after 30 days to save costs
resource "aws_s3_bucket_lifecycle_configuration" "media_lifecycle" {
  bucket = aws_s3_bucket.media_storage.id

  rule {
    id     = "archive_old_audio"
    status = "Enabled"

    transition {
      days          = 30
      storage_class = "GLACIER"
    }
  }
}