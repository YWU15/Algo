# Configure your S3 Access and Secret keys
aws configure set aws_access_key_id 4387ddc1-fcd7-4b60-a259-5f11fff32908
aws configure set aws_secret_access_key L4kYmUmYV_IJQua8j38b6OrJDw0pH7zL

# List
aws s3 ls s3://flatfiles/ --endpoint-url https://files.massive.com

# Copy
aws s3 cp s3://flatfiles/us_stocks_sip/trades_v1/2025/11/2025-11-05.csv.gz . --endpoint-url https://files.massive.com
