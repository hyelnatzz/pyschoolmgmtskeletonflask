from flask import Blueprint


home_bp = Blueprint('home_bp', __name__, url_prefix='/')


@home_bp.route('/')
def index():
    return 'this is homepage'


