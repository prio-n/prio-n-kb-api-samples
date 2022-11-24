# PRIO<sup>n</sup> Knowledge Base

[PRIO<sup>n</sup> Knowledge Base](https://kb.prio-n.com) aggregates publicly disclosed vulnerabilities and provides additional context for faster vulnerability triage. PRIO<sup>n</sup>'s scoring algorithm crunches the data and produces a priority score.

Using Natural Language Processing (NLP) and 3rd party lookups, KB is able to:

- Detect the vulnerability type.
- Map vulnerabilities against the following security frameworks:
  - OWASP
  - MITRE ATT&CK
  - MITRE CAPEC
  - DISA STIG
- Identify existence of public exploit code and exploitation activity.

Visit [https://www.prio-n.com](https://www.prio-n.com) to learn more.
## Using PRIO<sup>n</sup> KB API

## Limits
PRIO<sup>n</sup> API requests are limited up to `100 req/day`. Check out the `X-KB-API-QUOTA-LEFT` response header to see if you are within the daily limit before making subsequent requests.


## Authentication

PRIO<sup>n</sup> KB API uses the client credentials flow. In order to use it you must register at [https://kb.prio-n.com](https://kb.prio-n.com). Registration is free. Sign-in to your account, click on your username and select `API Keys` to manage your keys. One API Key pair is allowed per registered user.

To obtain a valid `access token` and access the API use you `client_id` and `client_secret` pair:


```bash
curl --request POST \
  --url 'https://prion-kb.eu.auth0.com/oauth/token' \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data '
    audience=https://api.prio-n.com&
    grant_type=client_credentials&
    client_id=YOUR_CLIENT_ID&
    client_secret=YOUR_SECRET'

```

The response will be similar to the one below:

```json
{"access_token":"<YOUR ACCESS TOKEN>","expires_in":86400,"token_type":"Bearer"}
```

Use the `access_token` to access the API:

```sh
curl -X 'GET' \
  'http://api.prio-n.com/v1/vulns/CVE-1999-0001' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'

```

## Samples
Checkout the [examples]('examples/) directory for samples. 