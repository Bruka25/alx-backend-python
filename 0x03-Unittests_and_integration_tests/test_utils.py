#!/usr/bin/env python3

"""Module for parameterized unitesting"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map returns correct value for given path.

        Parameters:
        nested_map (dict): The dictionary to access.
        path (tuple): The sequence of keys to access in the nested dictionary.
        expected: The expected value to be returned by the function.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    # Run the unit tests
    unittest.main()
