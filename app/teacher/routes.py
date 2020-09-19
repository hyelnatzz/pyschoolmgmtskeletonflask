from flask import Blueprint


teacher = Blueprint('teacher', __name__, url_prefix='/teacher')


@teacher.route('/')
def teacher_home():
    return 'teacher profile page'


@teacher.route('/new/')
def new_teacher():
    return 'new teacher page'