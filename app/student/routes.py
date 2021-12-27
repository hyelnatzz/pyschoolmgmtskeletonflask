from flask import Blueprint

student_bp = Blueprint('student_bp', __name__, url_prefix='/student')


@student_bp.route('/')
def student_home():
    return 'student profile page'


@student_bp.route('/new/')
def new_student():
    return 'registering new student page'