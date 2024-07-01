#!/usr/bin/env python3

"""Module for parameterized unitesting"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from typing import Dict, Tuple
from unittest.mock import patch, Mock


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


class TestGetJson(unittest.TestCase):
    """Test cases for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test get_json returns the expected result.

        Parameters:
        test_url (str): The URL to fetch the JSON from.
        test_payload (dict): The expected JSON payload.
        """
        with patch('utils.requests.get') as mock_get:
            # Create a Mock response object with the desired json method
            # return value
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call the function with the test URL
            result = get_json(test_url)

            # Assert that requests.get was called once with the test URL
            mock_get.assert_called_once_with(test_url)

            # Assert that the result is equal to the test payload
            self.assertEqual(result, test_payload)


if __name__ == '__main__':
    # Run the unit tests
    unittest.main()
