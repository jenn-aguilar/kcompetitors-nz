import requests
from bs4 import BeautifulSoup

# URL of the website
# for page_index in range(1,10):
#     print(page_index)
url = f'https://hikoco.co.nz/collections/hairbody?page=1&sort_by=best-selling'

# Send a GET request to fetch the webpage content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all product containers (adjust the selector based on the website structure)
products = soup.find_all('div', class_='grid-item__content')

for product in products:
    # Find the product name and price (adjust the selectors accordingly)
    brand = product.find('div', class_='grid-product__vendor').text.strip()
    name = product.find('div', class_='grid-product__title').text.strip()
    price = product.find('span', class_='visually-hidden').text.strip()

    print(f'{brand}, {name}, {price}')

