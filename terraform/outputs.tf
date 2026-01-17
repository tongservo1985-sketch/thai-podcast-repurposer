output "s3_bucket_name" {
  value = aws_s3_bucket.media_storage.id
}

output "rds_endpoint" {
  value = aws_db_instance.postgres.endpoint
}

output "redis_endpoint" {
  value = aws_elasticache_cluster.celery_broker.cache_nodes[0].address
}

output "vpc_id" {
  value = module.vpc.vpc_id
}