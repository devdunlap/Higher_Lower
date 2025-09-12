""" Unit tests for the Higher Lower game """

from random import random
import unittest
from unittest.mock import patch
import main

# Sample data for testing
test_data = {
    'A': 100,
    'B': 200,
    'C': 300
}

class TestMain(unittest.TestCase):
    def setUp(self):
        # Patch main.data with test_data
        self.data_patcher = patch('main.data', test_data)
        self.data_patcher.start()

    def tearDown(self):
        self.data_patcher.stop()

    def test_get_random_entry_returns_tuple(self):
        name, value = main.get_random_entry()
        self.assertIn(name, test_data)
        self.assertEqual(value, test_data[name])

    def test_get_random_entry_excludes(self):
        excluded = 'A'
        for _ in range(20):
            name, _ = main.get_random_entry(exclude=excluded)
            self.assertNotEqual(name, excluded)

    def test_format_entry(self):
        result = main.format_entry('Test', 123)
        self.assertEqual(result, 'Test (searched 123 times)')

    def test_get_random_entry_returns_different_entries(self):
        # Ensure that with enough calls, we get all possible entries (except excluded)
        found = set()
        for _ in range(100):
            name, _ = main.get_random_entry()
            found.add(name)
        self.assertTrue(set(test_data.keys()).issubset(found))

    def test_get_random_entry_with_all_but_one_excluded(self):
        # Exclude all but one entry, should always return the remaining one
        keys = list(test_data.keys())
        for i in range(len(keys)):
            with patch('main.data', {keys[i]: test_data[keys[i]]}):
                name, value = main.get_random_entry()
                self.assertEqual(name, keys[i])
                self.assertEqual(value, test_data[keys[i]])

if __name__ == '__main__':
    unittest.main()