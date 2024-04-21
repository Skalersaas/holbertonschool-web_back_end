#!/usr/bin/env python3
""" Module for auth
"""
import uuid
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
