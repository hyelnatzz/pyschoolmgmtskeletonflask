from flask import Flask
from .student.routes import student_bp
from .teacher.routes import teacher_bp
from .auth.routes import auth_bp
from .routes import home_bp
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')


    #blueprints
    app.register_blueprint(student_bp)
    app.register_blueprint(teacher_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)

    return app
