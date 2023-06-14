import requests
import json

rooturl = 'http://127.0.0.1:8000/api/v1'
CREATED = 201
OK = 200


def test_post_user():
    body = {
           "name": "Máquina testadora",
           "email": "alguem@gmail.com",
           "password": "123"}
    response = requests.post(rooturl + '/users', data=json.dumps(body))
    assert response.status_code == CREATED



def test_get_user_by_email():
    response = requests.get(rooturl + '/users/alguem@gmail.com')
    user = response.json()
    assert response.status_code == OK
    assert len(user) > 0
    assert user['email'] == 'alguem@gmail.com'