#!/usr/bin/env bash
set -euo pipefail

curl -sS \
  -H "X-SM-API-TOKEN: ${SEPPMAIL_API_TOKEN}" \
  -H "X-SM-API-SECRET: ${SEPPMAIL_API_SECRET}" \
  "https://mail.example.com:8445/v1/version"
