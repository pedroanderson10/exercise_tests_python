import unittest
import requests
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, "utils")
sys.path.append(path_dir)

from utils.json_util import *

class Profile(unittest.TestCase):

    def setUp(self):
        self.url = get_url()

    def test_1_get_profile(self):
        auth = get_token()
        header = {'authorization' : auth}

        response = requests.get(f"{self.url}/profiles", headers=header)
        assert response.status_code == 200

        json_data = json.loads(response.text)


        for item in json_data:

            id = item['id']
            self.assertIn('id', item)
            self.assertEqual(type(item['id']), int)
            self.assertEqual(item['id'], id)
            print('ID = ', id)

            name = item['name']
            self.assertIn('name', item)
            self.assertEqual(type(item['name']), str)
            self.assertEqual(item['name'], name)
            print('Name =', name)

            typee = item['type']
            self.assertIn('type', item)
            self.assertEqual(type(item['type']), str)
            self.assertEqual(item['type'], typee)
            print('Type =', typee)
            print('\n')

        print()