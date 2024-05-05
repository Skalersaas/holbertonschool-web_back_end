#!/usr/bin/env python3
"""Base flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union

app = Flask(__name__)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Setups"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


def get_user() -> Union[dict, None]:
    """Getting user"""
    try: 
        return users.get(int(request.args.get('login_as')))
    except RuntimeError:
        return None


@babel.localeselector
def get_locale():
    """Get locale"""
    lang = request.args.get("locale")
    if lang in app.config["LANGUAGES"]:
        return lang
    else:
        return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.before_request
def b_req():
    """Before request"""
    g.user = get_user()


@app.route('/')
def home():
    """ Home Page
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
