from flask import Flask, send_from_directory, request
from flask_sqlalchemy import SQLAlchemy

def get_uri():
    # return open('uri.txt').readline()
    return 'sqlite:///C:/Users/Hunter/Documents/Projects/ToDoList/database/todo.db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = get_uri()

db = SQLAlchemy()
db.init_app(app)

class Task(db.Model):
    taskName = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    taskLength = db.Column(db.Integer)
    taskDate = db.Column(db.String)
    taskTime = db.Column(db.String)
    taskDescription = db.Column(db.String)

    def __repr__(self):
        return f'<Task: {self.taskName}>'

@app.route('/postTask', methods=['POST'])
def addTask():
    data = request.get_json(force=True)
    print(f'Request: {data}')
    task = Task(taskName=data['taskName'], taskLength=data['taskLength'], taskDate=data['taskDate'], taskTime=data['taskTime'], taskDescription=data['taskDescription'])

    if task.taskName == None:
        return {
            'Task': 'null',
            'Added': 'No',
        } 
    else:
        db.session.add(task)
        db.session.commit()

        return {
            'Task': data['taskName'],
            'Added': 'Yes',
        }

@app.route('/getTasks', methods=['GET'])
def getTasks():
    tasks = Task.query.all()
    taskList = []
    for t in tasks:
        # taskList[t.taskName] = {'taskName': t.taskName, 'taskLength': t.taskLength}
        taskList.append({'taskName': t.taskName, 'taskLength': t.taskLength, 'taskDate': t.taskDate, 'taskTime': t.taskTime, 'taskDescription': t.taskDescription})
    print(tasks)
    return taskList

@app.route('/')
def client():
    return send_from_directory('../frontend/tdl/dist', 'index.html')


@app.route('/<path:path>')
def home(path):
    return send_from_directory('../frontend/tdl/dist', path)
    

if __name__ == '__main__':
    app.run()