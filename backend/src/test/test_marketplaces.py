import requests
import json

URL = 'http://127.0.0.1:8000/api/v1'
URL = 'http://18.219.31.213:80/api/v1'
CREATED = 201
OK = 200

def test_post_marketplace():
    body = {"longitude": "-23.3058711","latitude": "-50.0926748"}
    response = requests.post(URL + '/marketplaces', data=json.dumps(body))
    r = response.json()
    assert response.status_code == OK

