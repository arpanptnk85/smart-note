#!/bin/sh

# Exit immediately if any command fails
set -e

# Log the startup process
echo "Starting the User Service..."

echo $MONGO_URI

# Start the server (development)
exec flask --app user_service/app run --host 0.0.0.0 --port 8001