#!/usr/bin/env python3
"""Auth module"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str = '') -> str:
    """Hashing"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registration"""
        try:
            if self._db.find_user_by(email=email):
                raise ValueError(f"{email} already exists")
        except NoResultFound:
            hash = _hash_password(password)

        return self._db.add_user(email, hash)
