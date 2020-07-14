import unittest
from silasdk.users import User
from testcases.test_config import *
from utilities.util import *


class RequestKyc(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    # Get user data from the excel sheet.
    loc = ("C:\\Users\\sagar\\PycharmProjects\\SilaMoneyAutomationTesting\\testdata\\datasheet.xls")
    getUserHandle, getPrivateKey = utility.getDataFromSheet(loc)

    def test_register_kyc_200(self):

        payload = {
            "user_handle": self.getUserHandle
        }

        response = User.requestKyc(app, payload, self.getPrivateKey)
        self.assertEqual(response["status"], "SUCCESS")
        self.log.info(response)

    def test_register_kyc_custom_403(self):

        payload = {
            "user_handle": self.getUserHandle,
            "kyc_level": "CUSTOM_KYC_FLOW_NAME"
        }

        response = User.requestKyc(app, payload, self.getPrivateKey, True)
        self.assertEqual(response["status"], "FAILURE")
        self.log.info(response)

