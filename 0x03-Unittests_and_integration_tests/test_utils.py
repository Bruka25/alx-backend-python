#!/usr/bin/env python3

"""Module for parameterized unitesting"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Dict, Tuple

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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """Function for assesing nested exception raising."""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    # Run the unit tests
    unittest.main()