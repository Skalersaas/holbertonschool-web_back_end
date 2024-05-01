#!/usr/bin/env python3
"""TEsting client.py"""
from unittest import TestCase, mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """Testing github client"""

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @mock.patch('client.get_json')
    def test_org(self, org, expected, got):
        """ Testing org"""
        got.return_value = expected
        x = GithubOrgClient(org)
        self.assertEqual(x.org, expected)
        got.assert_called_once("https://api.github.com/orgs/"+org)
