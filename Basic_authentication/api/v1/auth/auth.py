#!/usr/bin/env python3
""" Module for auth
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Demo now
        """
        return False, path

    def authorization_header(self, request=None) -> str:
        """ Demo again
        """
        return None, request

    def current_user(self, request=None) -> TypeVar('User'):
        """ Eh
        """
        return None, request
