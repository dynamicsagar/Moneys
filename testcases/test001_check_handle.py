import unittest
from silasdk import User
from testcases.test_config import *
from utilities.util import *


class CheckHandle(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    def test_check_handle_200(self):
        payload = {
            "user_handle": user_handle
        }

        response = User.checkHandle(app, payload)
        self.log.info(response)
        self.assertEqual(response["status"], "SUCCESS")

    def test_check_handle_401(self):
        payload = {
            "user_handle": check_handle_status_401
        }

        response = User.checkHandle(app, payload)
        self.log.info(response)
        self.assertEqual(response["status"], "FAILURE")