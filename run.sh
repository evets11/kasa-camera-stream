#!/usr/bin/env bash

# Start nginx
echo "Starting Nginx"
nginx
echo "Nginx Started"

echo "Starting controller"
python3 -u /Controller/Controller.py
