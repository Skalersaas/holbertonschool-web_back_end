#!/usr/bin/env python3
""" Module for auth
"""
import datetime
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
        s_id = super().creat_session(user_id)
        if not s_id:
            return None
        self.user_id_by_session_id[s_id] = \
        {"user_id": user_id, "created_at": datetime.datetime.now()}
        return s_id
    
    def user_id_for_session_id(self, session_id: str = None) -> str:
        """GEt user"""
        if session_id is None:
            return None
        if session_id not in self.user_id_by_session_id:
            return None
        if self.SESSION_DURATION <= 0:
            return self.user_id_by_session_id["user_id"]
        if not self.user_id_by_session_id[session_id]:
            return None
        created_at = self.user_id_by_session_id["created_at"]
        if datetime.timedelta(created_at + self.SESSION_DURATION) \
        >datetime.datetime.now():
            return None
        
        return self.user_id_by_session_id["user_id"]
