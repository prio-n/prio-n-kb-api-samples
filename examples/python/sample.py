import json
import requests
import sys

from typing import Dict


PRIO_N_KB_API_URL = "https://api.prio-n.com"
PRIO_N_AUTH_DOMAIN = "prion-kb.eu.auth0.com"

CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"


def get_access_token() -> Dict:
    headers = {
        'content-type': 'application/x-www-form-urlencoded'
    }

    data = {
        "audience": PRIO_N_KB_API_URL,
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }

    resp = requests.post(
        f"https://{PRIO_N_AUTH_DOMAIN}/oauth/token",
        data=data,
        headers=headers)

    auth = resp.json()

    return auth


def search_kb_api(cve_id: str, access_token: str):
    url = f"{PRIO_N_KB_API_URL}/v1/vulns/{cve_id}"
    headers = {
        'accept': 'application/json',
        'Authorization': f"Bearer {access_token}",
    }

    resp = requests.get(url, headers=headers)

    return resp.json()


auth = get_access_token()
access_token = auth["access_token"]

vuln_data = search_kb_api(sys.argv[1].upper(), access_token)

print(json.dumps(vuln_data, indent=2))
