import requests
import time

# URL of the website
# for page_index in range(1,5):
#     print(page_index)
url = f'https://thecosmeticstore.co.nz/collections/all-personal-care/products.json?page=2'

# Send a GET request to fetch the webpage content
response = requests.get(url)
data = response.json()
products = data.get("products", [])
# print(products)

# Find all product containers (adjust the selector based on the website structure)
for product in products:
    tags = product.get("tags", [])
    if "Best Seller" in tags:
        title = product["title"]
        vendor = product["vendor"]
        price = product["variants"][0]["price"]
        print(f"{vendor}, {title}, ${price}")

# time.sleep(20)
