#!/bin/bash

# Script to sync US Options OPRA or US Stocks SIP data from S3
# Fetches trades, minute aggregates, and day aggregates

# Load AWS CLI module
module load awscli/2.11.7

# S3 endpoint URL
ENDPOINT_URL="https://files.massive.com"

# Get data type (options or stocks) and other arguments
DATA_TYPE=${1:-options}
YEAR=${2:-2025}
MONTH=${3:-11}

# Set S3 bucket and local directory based on data type
if [ "$DATA_TYPE" == "stocks" ] || [ "$DATA_TYPE" == "stock" ]; then
    S3_BUCKET="s3://flatfiles/us_stocks_sip"
    LOCAL_DIR=${4:-/blue/yixuanli/wyanbin/ResearchData/Algo/us_stocks_sip}
    DATA_LABEL="US Stocks SIP"
else
    S3_BUCKET="s3://flatfiles/us_options_opra"
    LOCAL_DIR=${4:-/blue/yixuanli/wyanbin/ResearchData/Algo/us_options_opra}
    DATA_LABEL="US Options OPRA"
fi

echo "Syncing ${DATA_LABEL} data for ${YEAR}/${MONTH}..."
echo "Local directory: ${LOCAL_DIR}"
echo "========================================"

# Sync trades data
echo "Syncing trades_v1..."
aws s3 sync ${S3_BUCKET}/trades_v1/${YEAR}/${MONTH} ${LOCAL_DIR}/trades_v1/${YEAR}/${MONTH} \
    --endpoint-url ${ENDPOINT_URL}

if [ $? -eq 0 ]; then
    echo "✓ trades_v1 sync completed"
else
    echo "✗ trades_v1 sync failed"
fi

echo ""

# Sync minute aggregates data
echo "Syncing minute_aggs_v1..."
aws s3 sync ${S3_BUCKET}/minute_aggs_v1/${YEAR}/${MONTH} ${LOCAL_DIR}/minute_aggs_v1/${YEAR}/${MONTH} \
    --endpoint-url ${ENDPOINT_URL}

if [ $? -eq 0 ]; then
    echo "✓ minute_aggs_v1 sync completed"
else
    echo "✗ minute_aggs_v1 sync failed"
fi

echo ""

# Sync day aggregates data
echo "Syncing day_aggs_v1..."
aws s3 sync ${S3_BUCKET}/day_aggs_v1/${YEAR}/${MONTH} ${LOCAL_DIR}/day_aggs_v1/${YEAR}/${MONTH} \
    --endpoint-url ${ENDPOINT_URL}

if [ $? -eq 0 ]; then
    echo "✓ day_aggs_v1 sync completed"
else
    echo "✗ day_aggs_v1 sync failed"
fi

echo ""
echo "========================================"
echo "All syncs completed!"
echo ""
echo "Usage: $0 [DATA_TYPE] [YEAR] [MONTH] [LOCAL_DIR]"
echo "DATA_TYPE: 'options' or 'stocks' (default: options)"
echo ""
echo "Examples:"
echo "  $0                                    # Options: 2025/11 (default)"
echo "  $0 options 2025 10                    # Options: 2025/10"
echo "  $0 stocks 2025 11                     # Stocks: 2025/11"
echo "  $0 stocks 2025 11 /custom/path        # Stocks: custom location"
echo ""
echo "Default directories:"
echo "  Options: /blue/yixuanli/wyanbin/ResearchData/Algo/us_options_opra"
echo "  Stocks:  /blue/yixuanli/wyanbin/ResearchData/Algo/us_stocks_sip"
