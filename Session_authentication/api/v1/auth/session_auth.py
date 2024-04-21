#!/usr/bin/env python3
""" Module for auth
"""
from typing import TypeVar
import uuid
from models.user import User
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ Child"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creating
        """
        if user_id is None or type(user_id) is not str:
            return None
        id = str(uuid.uuid4())
        self.user_id_by_session_id[id] = user_id
        return id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Gets user
        """
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get user id
        """
        s_id = self.session_cookie(request)
        if s_id is None:
            return None
        user_id = self.user_id_for_session_id(s_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """ Destroy session
        """
        if request is None:
            return False
        s_id = self.session_cookie(request)
        if s_id is None:
            return False
        if self.user_id_for_session_id(s_id) is None:
            return False
        del self.user_id_by_session_id[s_id]
        return True
