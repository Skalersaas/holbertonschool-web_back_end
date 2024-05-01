#!/usr/bin/env python3
"""Test utils module"""
from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(TestCase):
    """Base class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, input, map, output):
        """Joriki ejji"""
        return self.assertEqual(access_nested_map(input, map), output)
