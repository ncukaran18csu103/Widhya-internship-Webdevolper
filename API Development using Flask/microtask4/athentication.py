from flask import Flask, jsonify, request, abort
from flask_httpauth import HTTPBasicAuth

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


auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'Karan choudhary':
        return 'rathore'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
   
   

@app.route('/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks': tasks})
    
#curl -u parikshit:rathore -i http://localhost:5000/tasks
    
if __name__ == '__main__':
    app.run(debug=True)