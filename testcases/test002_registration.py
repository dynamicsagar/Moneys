import unittest
from silasdk import User
from testcases.test_config import *
from utilities.util import *


class Registration(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    def test_register_200(self):
        payload = {
            "country": "US",
            "user_handle": user_handle,
            "first_name": name,
            "last_name": name,
            "entity_name": 'Example User',
            "identity_value": "123452222",
            "phone": 1234567890,
            "email": "fake@email.com",
            "street_address_1": '123 Main Street',
            "city": 'New City',
            "state": 'OR',
            "postal_code": 97204,
            "crypto_address": eth_address,
            "crypto_alias": "python_wallet_1",
            "birthdate": "1990-05-19"
        }

        response = User.register(app, payload)
        self.assertEqual(response["status"], "SUCCESS")
        utility.insertData(inserthandle=user_handle, insertethkey=eth_private_key)
        self.log.info(response)
