"""
@package utilities
Util class implementation
All most commonly used utilities should be implemented in this class
Example:
    name = self.util.getUniqueName()
"""

import time
import traceback
import random, string
import utilities.custom_logger as cl
import logging
from xlwt import Workbook
import xlrd
import requests
from requests.exceptions import HTTPError


class Util(object):
    log = cl.customLogger(logging.INFO)

    def sleep(self, sec, info=""):
        """
        Put the program to wait for the specified amount of time
        """
        if info is not None:
            self.log.info("Wait :: '" + str(sec) + "' seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def getAlphaNumeric(self, length, type='letters'):
        """
        Get random string of characters
        Parameters:
            length: Length of string, number of characters string should have
            type: Type of characters string should have. Default is letters
            Provide lower/upper/digits for different types
        """
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def getUniqueName(self, charCount=10):
        """
        Get a unique name
        """
        return self.getAlphaNumeric(charCount, 'lower')

    def insertData(self, inserthandle, insertethkey):
        """
        Insert user_handle and eth_private_key to the xls sheet.
        Parameters:
                inserthandle: user_handle
                insertethkey: eth_private_key
        """
        try:
            wb = Workbook()
            sheet1 = wb.add_sheet('Sheet 1')
            sheet1.write(1, 0, inserthandle)
            sheet1.write(2, 0, insertethkey)
            wb.save("C:\\Users\\sagar\\PycharmProjects\\SilaMoneyAutomationTesting\\testdata\\datasheet.xls")
            self.log.info("Successfully inserted both the values in the sheet")
        except:
            self.log.info("Unable to insert values into xls")

    def getDataFromSheet(self, loc):
        """
        Get user_handle and eth_private_key from the xls sheet.
        Parameters:
                getUserHandle: user_handle
                getPrivateKey: eth_private_key
        """
        try:
            loc = ("C:\\Users\\sagar\\PycharmProjects\\SilaMoneyAutomationTesting\\testdata\\datasheet.xls")
            wb = xlrd.open_workbook(loc)
            sheet = wb.sheet_by_index(0)
            getUserHandle = (sheet.cell_value(1, 0))
            getPrivateKey = (sheet.cell_value(2, 0))
            self.log.info("Getting data from the xls sheet")
            return getUserHandle, getPrivateKey
        except:
            self.log.info("Unable to get data from the xls")

    def verifyResponseStatusCode(self, url):
        try:
            response = requests.get(url)

            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            self.log.info(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.log.info(f'Other error occurred: {err}')
        else:
            self.log.info('Success!')

    def verifyResponseStatus(self, url):
        try:
            response = requests.get(url)
            assert(response["status"], "SUCCESS")
            self.log.info('Check_handle verification passed!!')
            return True
        except AssertionError as error:
            self.log.info(error)
        except Exception as exception:
            self.log.info(exception)











