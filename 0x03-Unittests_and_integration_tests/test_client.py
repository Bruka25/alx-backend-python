#!/usr/bin/env python3

import unittest
from typing import Dict
from unittest.mock import patch, MagicMock, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD

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

    def test_public_repos_url(self) -> None:
        """Tests the `_public_repos_url` property."""
        # Use patch to mock the `org` property of GithubOrgClient
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_org:

            # Set up the mock to return a specific payload when accessed
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            # Instantiate GithubOrgClient with "google"
            # Access `_public_repos_url` and assert its value
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Tests the `public_repos` method."""

        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock,
                ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "episodes.dart",
                    "kratu",
                ],
            )
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

        @parameterized.expand([
            ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
            ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
        ])
        def test_has_license(self, repo: Dict, key: str,
                             expected: bool) -> None:
            """Tests the `has_license` method."""
            gh_org_client = GithubOrgClient("google")
            client_has_licence = gh_org_client.has_license(repo, key)
            self.assertEqual(client_has_licence, expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Performs integration tests for the `GithubOrgClient` class."""

    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()


if __name__ == '__main__':
    unittest.main()
