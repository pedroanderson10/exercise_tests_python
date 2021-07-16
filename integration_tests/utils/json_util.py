import json
import requests

#Token : eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwcm9maWxlIjoiQURNSU5JU1RSQVRPUiIsImlzcyI6InRlc3Quc2dtZUBnbWFpbC5jb20iLCJleHAiOjE2MjcwNDIyMjcsImlhdCI6MTYyNjQzNzQyNywidXNlciI6MTM5fQ.5zh4GGoJIwq7u1X4xG4hBzat9w9wyZXF2iJz8gETda0
#Link : https://test.jasgme.com/pt/login

def get_url():
    return 'https://test.jasgme.com/sgme/api'

def get_valid_credentials():
    return {'login': 'test.sgme@gmail.com', 'password': 'abcd1234'}

def get_invalid_credentials():
    return {'login': 'test.sgme@gmaill.com', 'password': 'abcd12345'}

def get_token():
    url = get_url()
    credentials_body = get_valid_credentials()

    response = requests.post(f"{url}/authenticate/login", json=credentials_body)
    assert response.status_code == 200

    json_data = json.loads(response.text)
    token = json_data['token']

    auth = f'Bearer {token}'

    return auth

