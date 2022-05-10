import unittest
from countries_solution import CountriesDataFrame
import json 
import hashlib

class TestCountriesDataFrame(unittest.TestCase):
    def test_get_countries(self):
        dt = CountriesDataFrame()
        dt.get_countries()
        self.assertTrue(len(dt.json_str) > 1)


    def test_get_records(self):
        dt = CountriesDataFrame()
        dt.get_countries()
        data = dt.get_records()
        self.assertTrue(type(data) == list and len(data) > 1)


    def test_json_file(self):
        dt = CountriesDataFrame()
        dt.get_countries()
        dt.to_dt()
        dt.to_json()

        with open('data.json') as f:
            data = json.load(f)

        self.assertTrue(type(data) == dict and len(data) > 1)


    def test_hash_sha1(self):
        dt = CountriesDataFrame()
        hash_test = 'Countries'
        result = True if (dt.hash_sha1(hash_test) == hashlib.sha1(hash_test.encode()).hexdigest()) else False
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
