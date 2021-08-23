import unittest
import requests
import json

class ApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000"

    def test_add(self):
        URL = "{}/addition".format(ApiTest.API_URL)
        r = requests.post(URL, json={'num1': 10, 'num2': 15})
        result = r.json()

        self.assertEqual(r.status_code, 200)
        self.assertEqual(result, 25)

    def test_sub(self):
        URL = "{}/subtraction".format(ApiTest.API_URL)
        r = requests.post(URL, json={'num1': 15, 'num2': 10})
        result = r.json()

        self.assertEqual(r.status_code, 200)
        self.assertEqual(result, 5)

    def test_multi(self):
        URL = "{}/multiplication".format(ApiTest.API_URL)
        r = requests.post(URL, json={'num1': 10, 'num2': 15})
        result = r.json()

        self.assertEqual(r.status_code, 200)
        self.assertEqual(result, 150)
    def test_add(self):
        URL = "{}/division".format(ApiTest.API_URL)
        r = requests.post(URL, json={'num1': 10, 'num2': 5})
        result = r.json()

        self.assertEqual(r.status_code, 200)
        self.assertEqual(result, 2)
