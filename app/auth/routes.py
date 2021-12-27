from flask import Blueprint, render_template, url_for, current_app
from flask_login import logout_user



auth_bp = Blueprint('auth_bp', __name__,url_prefix='/auth', template_folder='templates')


@auth_bp.route('/login/', methods=['GET', 'POST'])
def login():
    return 'login page'

@auth_bp.route('/teacher_signup/')
def teacherSignup():
    return 'teachers sign up page'

@auth_bp.route('/student_signup/')
def studentSignup():
    return 'student sign up page'

@auth_bp.route('/logout/')
def logout():
    return render_template('auth/logout.html')
