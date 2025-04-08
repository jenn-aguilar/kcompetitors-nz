import requests
from bs4 import BeautifulSoup

# URL of the website
for page_index in range(1,10):
    print(page_index)
    url = f'https://www.stylevana.com/en_NZ/hair-body.html?p={page_index}&product_list_dir=desc&product_list_order=popularity'

    # Send a GET request to fetch the webpage content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)

    # Find all product containers (adjust the selector based on the website structure)
    products = soup.find_all('li', class_='item product product-item')

    for product in products:
        # Find the product name and price (adjust the selectors accordingly)
        name = product.find('a', class_='product-item-link').text.strip()
        price = product.find('div', class_='price-box price-final_price').text.replace('\n', ' ').strip()

        print(f'{name}, {price}')

