""" Unit tests for the Higher Lower game """

import unittest
from unittest.mock import patch, call
import main

# Sample data for testing
test_data = {
    'A': 100,
    'B': 200,
    'C': 300
}

class TestMain(unittest.TestCase):
    """Unit tests for main.py functions."""
    def setUp(self):
        """Patch main.data with test_data before each test."""
        self.data_patcher = patch('main.data', test_data)
        self.data_patcher.start()

    def tearDown(self):
        """Stop patching main.data after each test."""
        self.data_patcher.stop()

    def test_get_random_entry_returns_tuple(self):
        """Test get_random_entry returns a valid (name, value) tuple from data."""
        name, value = main.get_random_entry()
        self.assertIn(name, test_data)
        self.assertEqual(value, test_data[name])

    def test_get_random_entry_excludes(self):
        """Test get_random_entry does not return the excluded entry."""
        excluded = 'A'
        for _ in range(20):
            name, _ = main.get_random_entry(exclude=excluded)
            self.assertNotEqual(name, excluded)

    def test_format_entry(self):
        """Test format_entry returns the correct formatted string."""
        result = main.format_entry('Test', 123)
        self.assertEqual(result, 'Test (searched 123 times)')

    def test_get_random_entry_returns_different_entries(self):
        """Test get_random_entry can return all possible entries over multiple calls."""
        found = set()
        for _ in range(100):
            name, _ = main.get_random_entry()
            found.add(name)
        self.assertTrue(set(test_data.keys()).issubset(found))

    def test_get_random_entry_with_all_but_one_excluded(self):
        """Test get_random_entry returns the only available entry when all others are excluded."""
        keys = list(test_data.keys())
        for key in keys:
            with patch('main.data', {key: test_data[key]}):
                name, value = main.get_random_entry()
                self.assertEqual(name, key)
                self.assertEqual(value, test_data[key])

    def test_play_game_correct_and_incorrect_guess(self):
        """Test play_game logic for correct and incorrect guesses using mocks."""
        # Patch input to simulate user guesses: first correct, then incorrect
        with patch('builtins.input', side_effect=['a', 'b']), \
             patch('main.get_random_entry', side_effect=[('A', 200), ('B', 100), ('C', 50)]), \
             patch('main.LOGO', "LOGO"), \
             patch('builtins.print') as mock_print:
            main.play_game()
            # Check that print was called with correct and final score
            printed = [call.args[0] for call in mock_print.call_args_list]
            self.assertTrue(any("Correct! Current score: 1." in s for s in printed))
            self.assertTrue(any("Sorry, that's wrong. Final score: 1." in s for s in printed))

if __name__ == '__main__':
    unittest.main()