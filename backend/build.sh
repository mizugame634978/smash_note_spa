#!/usr/bin/env bash

echo "===== build.sh START ====="
# exit on error
set -o errexit
# 最低限
pip install -r requirements.txt
