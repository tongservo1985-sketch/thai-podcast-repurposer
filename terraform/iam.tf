# IAM Role for AI Processing Workers (ECS/EC2)
resource "aws_iam_role" "worker_role" {
  name = "${var.project_name}-worker-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        }
      },
    ]
  })
}

# Specific policy for S3 access (Least Privilege)
resource "aws_iam_role_policy" "worker_s3_policy" {
  name = "overlord-s3-access"
  role = aws_iam_role.worker_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "s3:GetObject",
          "s3:PutObject",
          "s3:ListBucket"
        ]
        Resource = [
          aws_s3_bucket.media_storage.arn,
          "${aws_s3_bucket.media_storage.arn}/*"
        ]
      }
    ]
  })
}