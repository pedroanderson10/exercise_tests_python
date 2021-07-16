from behave import*
import os
import sys
import json
import unittest
from nose.tools import *

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, "utils")
sys.path.append(path_dir)

from utils.json_util import *

@given("a user is in the SGME login page")
def given(context):
    context.url = get_url()
    # response = requests.get(f"{context.url}")
    # assert_equal(response.status_code, 200)

@when("the user insert his invalid credentials")
def when(context):
    credentials_body = get_invalid_credentials()
    context.response = requests.post(f"{context.url}/authenticate/login", json=credentials_body)
    assert_equal(401, context.response.status_code)

@then("system returns that the credentials are not valid")
def then(context):
    context.json_data = json.loads(context.response.text)
    assert_in('error', context.json_data)
    assert_equal('Usuário ou Senha não conferem!', context.json_data['error'])
