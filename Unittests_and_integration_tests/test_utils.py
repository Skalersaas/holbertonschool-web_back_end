#!/usr/bin/env python3
"""Test utils module"""
from unittest import TestCase
from parameterized import parameterized


class TestAccessNestedMap(TestCase):
    """Base class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, input, map, output):
        """Joriki ejji"""
        return self.assertEqual(input, map, output)
