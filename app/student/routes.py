from flask import Blueprint

student_bp = Blueprint('student_bp', __name__, url_prefix='/students')


@student_bp.route('/')
def student_home():
    return 'student profile page'


@student_bp.route('/', methods=['POST'])
def new_student():
    return 'registering new student page'