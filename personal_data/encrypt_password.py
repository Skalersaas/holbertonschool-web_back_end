#!/usr/bin/env python3
'''Module for encrypting'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''Returns hash'''
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
