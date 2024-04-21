#!/usr/bin/env python3
""" Module of session authentication views
"""
from api.v1.views import app_views
from flask import jsonify, request
from models.user import User
from os import getenv


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def login():
    """ Login
    """
    email, pwd = request.form.get("email"), request.form.get("password")
    if not email:
        return jsonify({"error": "email missing"}), 400  
    if not pwd:
        return jsonify({"error": "password missing"}), 400
    user = User.search({'email': email})[0]
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    
    if not user.is_valid_password(pwd):
        return jsonify({"error": "wrong password"}), 401
    
    from api.v1.app import auth
    s_id = auth.create_session(user.id)
    SESSION_NAME = getenv(SESSION_NAME)
    
    data = jsonify(user.to_json())
    data.set_cookie(s_id, SESSION_NAME)
    return data
