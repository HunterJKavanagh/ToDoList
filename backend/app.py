from flask import Flask, send_from_directory, request
from supabase import create_client, Client
import os

app = Flask(__name__)

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

@app.route('/postTask', methods=['POST'])
def addTask():
    data = request.get_json(force=True)

    # d = supabase.table('tasks').insert({'taskName': data['taskName'], 'taskLength': data['taskLength'], 'taskDate': data['taskDate'], 'taskTime': data['taskTime'], 'taskDescription': data['taskDescription']}).execute()
    d = supabase.table('tasks').insert(data).execute()

    return {
        'Task': 'null',
        'Added': 'No',
    } 

@app.route('/getTasks', methods=['GET'])
def getTasks():
    tasks = supabase.table('tasks').select('*').order(column='taskTime', desc=False).execute()
    for t in tasks.data:
        print(t)
    return tasks.data

@app.route('/')
def client():
    return send_from_directory('../frontend/tdl/dist', 'index.html')


@app.route('/<path:path>')
def home(path):
    return send_from_directory('../frontend/tdl/dist', path)
    

if __name__ == '__main__':
    app.run()