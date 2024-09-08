#!/bin/sh

# Exit immediately if any command fails
set -e

# Log the startup process
echo "Starting the Main Service..."

exec flask --app api_gateway/app run --host 0.0.0.0 --port 8000