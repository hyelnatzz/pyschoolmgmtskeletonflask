from flask import Flask
from .student.routes import student
from .teacher.routes import teacher



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')


    #blueprints
    app.register_blueprint(student)
    app.register_blueprint(teacher)

    return app