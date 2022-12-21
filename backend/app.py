from flask import Flask, send_from_directory, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db = SQLAlchemy()
db.init_app(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taskName = db.Column(db.String, unique=True, nullable=False)
    dueDate = db.Column(db.String)
    time = db.Column(db.String)
    taskLength = db.Column(db.Integer)

@app.route('/addTask', methods=['POST'])
def printTask():
    print(f'POST FORM: {request.form}')
    for a in request.form:
        print(f'\tARG: {a}')
    return ''

@app.route("/")
def client():
    return send_from_directory('../frontend/tdl/dist', 'index.html')


@app.route("/<path:path>")
def home(path):
    return send_from_directory('../frontend/tdl/dist', path)
    

if __name__ == '__main__':
    app.run()