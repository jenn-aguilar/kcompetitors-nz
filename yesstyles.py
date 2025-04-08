import requests

url = "https://www.yesstyle.com/en/beauty-skin-care/list.html"
params = {
    "pn": 1,        # page number
    "s": 10,        # items per page
    "bcc": 15544,   # beauty > skin care
    "bpt": 46,
    "oc": 12,
    "sb": 136,
    "l": 1,
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.yesstyle.com/",
    # Include any necessary cookies or headers from browser session if blocked
}

response = requests.get(url, params=params, headers=headers)

print(response.text)
if response.ok:
    data = response.json()
    for product in data.get('items', []):
        print(product['brand'], product['productName'], product['price']['usd'])