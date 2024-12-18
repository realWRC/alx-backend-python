#!/usr/bin/env python3
"""Unittests of client module"""

import unittest
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from requests.exceptions import HTTPError
from unittest.mock import patch, PropertyMock, Mock


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests for GithubOrgClient
    """
    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Return value test
        """
        expected_org_data = {'login': org_name}
        mock_get_json.return_value = expected_org_data
        client = GithubOrgClient(org_name)
        org_data = client.org
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}'
        )
        self.assertEqual(org_data, expected_org_data)

    def test_public_repos_url(self):
        """Test _public_repos_url property"""
        test_org_payload = {
            'repos_url': 'https://api.github.com/orgs/test_org/repos'
        }
        expected_url = test_org_payload['repos_url']
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)\
                as mock_org:
            mock_org.return_value = test_org_payload
            client = GithubOrgClient('test_org')
            result = client._public_repos_url
            self.assertEqual(result, expected_url)
            mock_org.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Tests public_repos method
        """
        repos_payload = [
            {'name': 'repo1', 'license': {'key': 'mit'}},
            {'name': 'repo2', 'license': {'key': 'apache-2.0'}},
            {'name': 'repo3', 'license': {'key': 'gpl-3.0'}},
        ]
        mock_get_json.return_value = repos_payload

        with patch.object(
            GithubOrgClient,
            '_public_repos_url',
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = \
                'https://api.github.com/orgs/test_org/repos'
            client = GithubOrgClient('test_org')
            result = client.public_repos()

            expected_repos = ['repo1', 'repo2', 'repo3']
            self.assertEqual(result, expected_repos)
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                'https://api.github.com/orgs/test_org/repos'
            )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Tests for has_license method
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test suite
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up integration tests
        """
        cls.route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            """
            Side effect function
            """
            if url in cls.route_payload:
                return Mock(**{'json.return_value': cls.route_payload[url]})
            raise HTTPError

        cls.get_patcher = patch('requests.get', side_effect=get_payload)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop patching."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Tests the public_repos without license filter
        """
        client = GithubOrgClient('google')
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Tests the public_repos with license filter
        """
        client = GithubOrgClient('google')
        repos = client.public_repos(license='apache-2.0')
        self.assertEqual(repos, self.apache2_repos)
