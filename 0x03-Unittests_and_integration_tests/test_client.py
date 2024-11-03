#!/usr/bin/env python3
"""Unittests of client module"""

import unittest
from unittest.mock import patch
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
