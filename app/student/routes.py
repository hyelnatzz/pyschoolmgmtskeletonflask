from flask import Blueprint

student = Blueprint('student', __name__, url_prefix='/student')


@student.route('/')
def student_home():
    return 'student profile page'


@student.route('/new/')
def new_student():
    return 'regustering new student page'