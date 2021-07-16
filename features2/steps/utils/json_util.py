import json
import requests

#Token : eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwcm9maWxlIjoiQURNSU5JU1RSQVRPUiIsImlzcyI6InRlc3Quc2dtZUBnbWFpbC5jb20iLCJleHAiOjE2MjcwNDIyMjcsImlhdCI6MTYyNjQzNzQyNywidXNlciI6MTM5fQ.5zh4GGoJIwq7u1X4xG4hBzat9w9wyZXF2iJz8gETda0
#Link : https://test.jasgme.com/pt/login

def get_url():
    return 'https://test.jasgme.com/sgme/api'

def get_invalid_credentials():
    return {'login': 'test.sgme@gmail.com', 'password': 'abcd12345678'}



