import unittest
import requests
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, "utils")
sys.path.append(path_dir)

from utils.json_util import *

class Language(unittest.TestCase):

    def setUp(self):
        self.url = get_url()

    def test_1_get_language(self):
        auth = get_token()
        header = {'authorization' : auth}

        response = requests.get(f"{self.url}/languages", headers=header)
        assert response.status_code == 200

        json_data = json.loads(response.text)

        for item in json_data:
            self.assertIn('id', item)
            self.assertEqual(type(item['id']), int)

            self.assertIn('name', item)
            self.assertEqual(type(item['name']), str)

            self.assertIn('code', item)
            self.assertEqual(type(item['code']), str)

        print()


