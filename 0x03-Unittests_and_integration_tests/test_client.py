#!/usr/bin/env python3
"""Unittests of client module"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


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
