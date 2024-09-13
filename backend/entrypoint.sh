#!/bin/bash

echo "Starting App"

exec flask --app app run --host 0.0.0.0 --port 5000