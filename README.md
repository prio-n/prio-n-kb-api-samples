# Using PRIOn KB API

## Authentication

PRIOn KB API uses the client credentials flow. In order to use it you must register an account on [https://kb.prio-n.com](https://kb.prio-n.com). Registration is free. Sign-in to your account, click on your username and select `API Keys` to manage your keys. One API Key pair is allowed per registered user.

## Limits
PRIOn API requests are limited up to `100 req/day`.


## Authentication
PRIOn KB API uses the client credentials flow to obtain a valid `access token` and access the API.

For example:

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

Then you can use the `access_token` to access the API:

```sh
curl -X 'GET' \
  'http://api.prio-n.com/v1/vulns/CVE-1999-0001' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'

```

## Samples
Checkout the [examples]('examples/) directory for samples. 