from crypt import methods
from flask import Blueprint


teacher_bp = Blueprint('teacher_bp', __name__, url_prefix='/teachers')


@teacher_bp.route('/')
def teacher_home():
    return 'teacher profile page'


@teacher_bp.route('/', methods=['POST'])
def new_teacher():
    return 'new teacher page'