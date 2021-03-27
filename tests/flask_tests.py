import unittest
import requests


class Tests(unittest.TestCase):
    
    def test_app_is_up(self):
        r = requests.get('http://localhost:5000/')
        self.assertEqual(r.status_code, 200)
