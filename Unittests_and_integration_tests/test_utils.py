#!/usr/bin/env python3
"""Test utils module"""
from unittest import TestCase, mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize

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


class TestGetJson(TestCase):
    """Testing json output class"""
    
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """Testing json"""
        with mock.patch('requests.get') as patch:
            patch.return_value.json.return_value = payload
            self.assertEqual(get_json(url=url), payload)

class TestMemoize(TestCase):
    """Testing Memoize"""
    
    def test_memoize(self):
        """testing"""

        class TestClass:
            """Test classs"""

            def a_method(self):
                """A method"""
                return 42

            @memoize
            def a_property(self):
                """A property"""
                return self.a_method()

        with mock.patch("TestClass.a_method") as patch:
            t_class = TestClass()
            t_class.a_property()
            t_class.a_property()
            patch.assert_called_once()
