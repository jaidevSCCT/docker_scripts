#!/bin/bash
VERSION="$1"
IMAGE="$2"
NAMES="$3"
OUT_PORT=$4
IN_PORT=$5

docker run -d --name "$NAMES" -p "$OUT_PORT:$IN_PORT" -t "$IMAGE:$VERSION"
