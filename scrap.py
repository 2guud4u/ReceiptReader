import requests
import json

# set up the request parameters
params = {
'api_key': '2EEB3E19A4EC4B759863FA12FBC71441',
  'type': 'product',
  'dpci': '284111329'
}

# make the http GET request to RedCircle API
api_result = requests.get('https://api.redcircleapi.com/request', params)

# print the JSON response from RedCircle API
print(json.dumps(api_result.json()))

