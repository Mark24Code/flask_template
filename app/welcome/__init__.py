from flask import Blueprint

welcome = Blueprint('welcome', __name__, url_prefix='/')

from . import views, errors