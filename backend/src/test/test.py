import requests
import json

url = 'http://192.168.0.106:8000/api/v1'

def test_post_product():
    obj = {
        "description": "7896079846747",
        "gtin": "123"
    }
    response = requests.post(url+'/product', data=json.dumps(obj))
    assert response.status_code == 200

def test_get_product_by_gtin():
    response = requests.get(url+'/product'+'/123')
    products = response.json()
    assert len(products) > 0


def test_get_product_all():
    response = requests.get(url+'/product')
    products = response.json()
    assert len(products) > 0

def test_post_user():
    obj = {
           "name":"Lucas Garcia Batista",
           "email":"lucasgb2@gmail.com",
           "password":"123"}
    response = requests.post(url+'/user', data=json.dumps(obj))
    assert response.status_code == 200

def test_get_user_by_email():
    response = requests.get(url + '/user/lucasgb2@gmail.com')
    user = response.json()
    assert len(user) > 0