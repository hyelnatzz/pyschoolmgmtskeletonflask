from flask import Blueprint


home_bp = Blueprint('home_bp', __name__, url_prefix='/')


@home_bp.route('/')
def teacher_home():
    return 'this is homepage'


@home_bp.route('/new/')
def new_teacher():
    return 'new teacher page'
