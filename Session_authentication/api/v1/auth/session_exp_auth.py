#!/usr/bin/env python3
""" Module for auth
"""
from datetime import datetime, timedelta
from api.v1.auth.session_auth import SessionAuth
from os import getenv


class SessionExpAuth(SessionAuth):
    """ SessionExpAuth
    """
    def __init__(self) -> None:
        try:
            self.SESSION_DURATION = int(getenv("SESSION_DURATION"))
        except:
            self.SESSION_DURATION = 0
    
    def create_session(self, user_id: str = None) -> str:
        '''Create'''
        s_id = super().create_session(user_id)
        if not s_id:
            return None
        self.user_id_by_session_id[s_id] = \
        {"user_id": user_id, "created_at": datetime.now()}
        return s_id
    
    def user_id_for_session_id(self, session_id: str = None) -> str:
        """GEt user"""
        if session_id is None:
            return None

        if session_id not in self.user_id_by_session_id.keys():
            return None

        session_dictionary = self.user_id_by_session_id.get(session_id)

        if session_dictionary is None:
            return None

        if self.session_duration <= 0:
            return session_dictionary.get('user_id')

        created_at = session_dictionary.get('created_at')

        if created_at is None:
            return None

        expired_time = created_at + timedelta(seconds=self.session_duration)

        if expired_time < datetime.now():
            return None

        return session_dictionary.get('user_id')
