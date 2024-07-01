#!/usr/bin/env python3

import unittest
from typing import Dict
from unittest.mock import patch, MagicMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class

class TestGithubOrgClient(unittest.TestCase):
    """Tests the `GithubOrgClient` class."""

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(
            self, org: str, resp: Dict, mocked_get_json: MagicMock) -> None:
        """
        Tests the `org` method of GithubOrgClient.

        Parameters:
        org (str): The name of the GitHub organization.
        resp (Dict): The mocked response expected from get_json.
        mocked_get_json (MagicMock): Mock object for get_json.
        """
        # Configure the mocked get_json to return the specified response
        mocked_get_json.return_value = MagicMock(return_value=resp)

        # Instantiate GithubOrgClient with the organization name
        gh_org_client = GithubOrgClient(org)

        # Call the org method and assert the result matches
        # the expected response
        self.assertEqual(gh_org_client.org(), resp)

        # Assert that get_json was called once with the expected URL
        mocked_get_json.assert_called_once_with(
                "https://api.github.com/orgs/{}".format(org))


if __name__ == '__main__':
    unittest.main()
