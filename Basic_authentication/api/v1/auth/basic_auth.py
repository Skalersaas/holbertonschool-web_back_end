#!/usr/bin/env python3
""" Module for auth
"""
from api.v1.auth.auth import Auth
import base64

class BasicAuth(Auth):
    """ Child"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ Extracting
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startsWith("Basic "):
            return None
        return authorization_header[6:]
