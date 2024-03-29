import handler
from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/api/<user_id>/tasks', methods=['POST'])
def add_task(user_id):
    req_data = request.get_json()
    res_data = handler.add_task(req_data, user_id)
    if res_data is None:
        return Response("{'Error': 'Task not added'}", status=400, mimetype='application/json')
    else:
        return Response(json.dumps(res_data), status=201, mimetype='application/json')


@app.route('/api/<user_id>/tasks', methods=['GET'])
def get_all_tasks(user_id):
    res_data = handler.get_all_tasks(user_id)
    if ((res_data is None)or(len(res_data) == 0)):
        return Response("{'Error': 'Task not found'}", status=404, mimetype='application/json')
    else:
        return Response(json.dumps(res_data), status=200, mimetype='application/json')


@app.route('/api/<user_id>/tasks/<task_id>', methods=['GET'])
def get_task(user_id, task_id):
    res_data = handler.get_task(user_id, task_id)
    if ((res_data is None)or(len(res_data) == 0)):
        return Response("{'Error': 'Task not found'}", status=404, mimetype='application/json')
    else:
        return Response(json.dumps(res_data), status=200, mimetype='application/json')


@app.route('/api/<user_id>/tasks/<task_id>', methods=['PUT'])
def update_task(user_id, task_id):
    req_data = request.get_json()
    res_data = handler.update_task(req_data, user_id, task_id)
    if res_data is None:
        return Response("{'Error': 'Task not updated'}", status=400, mimetype='application/json')
    else:
        return Response(json.dumps(res_data), status=201, mimetype='application/json')


@app.route('/api/<user_id>/tasks/<task_id>', methods=['DELETE'])
def delete_task(user_id, task_id):

    handler.delete_task(user_id, task_id)
    return Response("{'Success': 'Task deleted'}", status=200, mimetype='application/json')
