from PIL import Image
import re
import pytesseract
import requests
import json

def getProduct(dpci):
    params = {
        'api_key': '2EEB3E19A4EC4B759863FA12FBC71441',
        'type': 'product',
        'dpci': dpci
    }

    # make the http GET request to RedCircle API
    api_result = requests.get('https://api.redcircleapi.com/request', params)

    # print title if item works
    if(api_result.json().get("request_info").get("success") == True):
        print(api_result.json().get('product').get('title'))


text = pytesseract.image_to_string(Image.open('shop.png'))
pattern = r'\d{9}'
item_dpci = []
for i, line in enumerate(text.split('\n')):
    
        
        matchh = re.search(pattern, str(line))
        if matchh:
            item_dpci.append(matchh.group(0))

for item in item_dpci:
    print("loooking for ", item)
    getProduct(item)


# set up the request parameters


