import requests
import json

URL = 'http://127.0.0.1:8000/api/v1'
URL = 'http://18.219.31.213:80/api/v1'

def getProduct():
    response = requests.get(URL + '/products')
    products: dict = response.json()
    return products[0]

def getMarketplace():
    response = requests.get(URL + '/marketplaces')
    marketplace: dict = response.json()
    return marketplace[0]

def test_post_price():
    product = getProduct()
    marketplace: dict = getMarketplace()

    body = {"id_product": product['_id'],
            "marketplace": marketplace,
	        "price" : 56.76,
	        "moment": "2023-05-31 21:35:00"
            }
    response = requests.post(URL + '/prices', data=json.dumps(body))
    assert response.status_code == 200
