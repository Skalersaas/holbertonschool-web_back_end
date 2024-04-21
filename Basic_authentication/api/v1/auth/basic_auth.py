#!/usr/bin/env python3
""" Module for auth
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """ Child"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Extracting
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ Decoding
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            return b64decode(base64_authorization_header).decode()
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """ Extracting
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if not decoded_base64_authorization_header.__contains__(":"):
            return None, None
        headers = decoded_base64_authorization_header.split(":")
        return headers[0], headers[1]
    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ Creating user object
        """
        if user_email is None or user_pwd is None:
            return None
        try:
            users = User.search({'email':user_email})
        except Exception:
            return
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None