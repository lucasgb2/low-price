import requests
import json
import pytest

URL = 'http://127.0.0.1:8000/api/v1'
URL = 'http://18.219.31.213:80/api/v1'
CREATED = 201
OK = 200


def test_post_gtin():
    obj = {"gtin": "7896079846747"}
    response = requests.post(URL+'/products', data=json.dumps(obj))
    assert response.status_code == OK
    assert 'napolitano' in response.json()['description'].lower()


def test_get_product_by_gtin():
    response = requests.get(URL+'/products'+'/7896079846747')
    assert response.status_code == OK
    products = response.json()


def test_get_product_all():
    response = requests.get(URL+'/products')
    assert response.status_code == OK
    products = response.json()

@pytest.mark.skip("Not implemented")
def test_get_prices_by_gtin():
    response = requests.get(URL+'/products/7896079846747/prices')
    assert response.status_code == OK
    products = response.json()

@pytest.mark.skip("Not implemented")
def test_get_prices_maxmin_by_gtin():
    response = requests.get(URL+'/products/7896079846747/maxmin')
    assert response.status_code == OK
    products = response.json()