#!/usr/bin/env python3
"""
Unittests for python code implimemnted in directory
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Tests the access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests return values"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),

    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Tests for KeyError"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """
    Defines tests for the get_json method of utils.py
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Tests for get_json"""
        mock_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Tests for memorize method of utils"""

    def test_memoize(self):
        """
        Tests memorize
        """
        class TestClass:
            """
            As described
            """
            def a_method(self):
                """
                Method to be memoized/stored
                """
                return 42

            @memoize
            def a_property(self):
                """
                Using memoize property
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42)\
                as mock_method:
            test_obj = TestClass()
            result_first_call = test_obj.a_property
            result_second_call = test_obj.a_property

            mock_method.assert_called_once()

            self.assertEqual(result_first_call, 42)
            self.assertEqual(result_second_call, 42)
