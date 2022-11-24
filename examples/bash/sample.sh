#!/usr/bin/env bash

# Sample PRIO-N KB API Usage
# Requires curl and jq to be installed

# Set the placeholder values accordingly
PRIO_N_KB_API_URL="https://api.prio-n.com"
PRIO_N_AUTH_DOMAIN="prion-kb.eu.auth0.com"
CLIENT_ID=YOUR_CLIENT_ID
CLIENT_SECRET=YOUR_CLIENT_SECRET

ACCESS_TOKEN=$(curl --request POST \
  --url "https://$PRIO_N_AUTH_DOMAIN/oauth/token" \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data "audience=https://api.prio-n.com&grant_type=client_credentials&client_id=$CLIENT_ID&client_secret=$CLIENT_SECRET" |\
  jq -r '.access_token')


curl -XGET -H "Authorization: Bearer $ACCESS_TOKEN" "$PRIO_N_KB_API_URL/v1/vulns/$1" | jq .
