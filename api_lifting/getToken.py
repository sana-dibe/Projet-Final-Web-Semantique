import requests
import json


client_id='zzLBiUlVw2eBKHV15rbLIk6GGdmT84x3'
client_secret='cfuVIA0mjx24kwpb'


url = "https://test.api.amadeus.com/v1/security/oauth2/token"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
data = {"grant_type": "client_credentials", "client_id":client_id, "client_secret": client_secret}

response = requests.post(url, headers=headers, data=data)


print(response.json()['access_token'])
