from flask import Blueprint

main = Blueprint("auth_blueprint", __name__)


@main.route('/')
def index_auth():
    pass