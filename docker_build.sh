#!/bin/bash
VERSION="$1"
IMAGE="$2"
FILE="$3"
PATH_TO_DIR="$4"
echo $FILE
docker build -f "$FILE" -t "$IMAGE:$VERSION" "$PATH_TO_DIR"
