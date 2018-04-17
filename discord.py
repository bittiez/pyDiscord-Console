import sys
import json
import requests

webhook_url = 'full webhook url'
discord_data = {'content': " ".join(sys.argv[2:]), 'username': sys.argv[1]}
response = requests.post(
    webhook_url, data=json.dumps(discord_data),
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 204:
    raise ValueError(
        'Request to discord returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
)
