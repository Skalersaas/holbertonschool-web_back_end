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
        """Normal Testing"""
        return self.assertEqual(access_nested_map(input, map), output)
    
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a","b")) 
    ])
    def test_access_nested_map_exception(self, input, map):
        """Exception Testing"""
        with self.assertRaises(KeyError) as err:
            access_nested_map(input, map)
        self.assertEqual(
            f'KeyError({err.exception})', repr(err.exception)
        )
