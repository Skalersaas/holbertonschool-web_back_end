#!/usr/bin/env python3
""" Module for auth
"""
from flask import request
from typing import List, TypeVar
import re


class Auth:
    """ Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require
        """
        if not path or not excluded_paths:
            return True

        path = path if path[-1] == '/' else f"{path}/"

        for ex in excluded_paths:
            if not ex:
                continue
            if ex[-1] == "*":
                    if ex[:-1] == path[:len(ex)-1]:
                        return False
            elif ex == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Header
        """
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Eh
        """
        return None
