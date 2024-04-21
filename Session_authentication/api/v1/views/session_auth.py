#!/usr/bin/env python3
""" Module of session authentication views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
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
    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if not user.is_valid_password(pwd):
            return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    user = users[0]
    s_id = auth.create_session(user.id)
    SESSION_NAME = getenv("SESSION_NAME")

    data = jsonify(user.to_json())
    data.set_cookie(SESSION_NAME, s_id)
    return data


@app_views.route("/auth_session/logout", methods=["DELETE"], strict_slashes=False)
def logout():
    from api.v1.app import auth
    if not auth.destroy_sesion(request):
        return False, abort(404)
    return jsonify({}), 200