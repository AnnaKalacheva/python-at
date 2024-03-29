

"""
Scenario:
    You own an ecommerce marketplace site. Several partners sell their products on your site.
    Like amazon.com. The partners update their list of products and prices daily. They send you the
    product information in one of several ways (API, FTP, Email, ...).

    You have received the products information and created a list as provided below.
    Variable 'products' is the list of products you have received.


Exercise:
    - Print the name of all products that have price greater than 25.

"""

products = [
    {'id': 1, 'name': 't-shirt', 'price': '$12.99', 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 2, 'name': 'shoes', 'price': '$22.45', 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': None},
    {'id': 3, 'name': 'dress-shirt', 'price': '$43.00', 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 4, 'name': 'socks', 'price': '$14.99', 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': 7.99},
    {'id': 5, 'name': 'trousers', 'price': '$32.50', 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': None},
    {'id': 6, 'name': 'jacket', 'price': '$150.00', 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
]
# solution 1
result = []
for product in products:
    price = float(product['price'][1:])
    if price > 25:
        result.append(product['name'])
print(result)
print(" ----- ".join(result))

# solution 2
for product in products:
    tmp_price = product['price'][1:]
    price = float(tmp_price)
    if price > 25:
        print(product['name'])




