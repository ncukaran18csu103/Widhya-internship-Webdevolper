from flask import Flask, jsonify, abort, make_response,request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Do Something',
        'description': u'Widhya Wintership', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Flask',
        'description': u'Frontend Web Developement from Widhya Wintership', 
        'done': False
    }
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/tasks/<int:task_id>' , methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0 :
        abort(404)
    return jsonify({'task' : task[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}) , 404)  

@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', "HEY"),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201
 
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})
#curl -i http://localhost:5000/tasks
#curl -i -H "Content-Type: application/json" -X POST -d "{"""title""":"""Read a book"""}" http://localhost:5000/tasks
#curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000//tasks/2


if __name__ == '__main__':
    app.run(debug=True)