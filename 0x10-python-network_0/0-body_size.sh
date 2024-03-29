#!/bin/bash

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Send an HTTP request using curl and store the response in a temporary file
response_file=$(mktemp)
curl -s "$url" > "$response_file"

# Get the size of the response body in bytes
response_size=$(wc -c < "$response_file")

# Display the size
echo "Response size for $url: $response_size bytes"

# Clean up the temporary file
rm "$response_file"
