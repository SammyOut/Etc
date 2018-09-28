from flask import Flask, request, jsonify
from flask.views import MethodView
from uuid import uuid4
from pymongo import MongoClient

app = Flask(__name__)

collection = MongoClient()['use_nginx']['todo']


class Todo(MethodView):
    def get(self, todo_id):
        if todo_id is None:
            todo = [a for a in collection.find()]
        else:
            todo = collection.find_one({'_id': todo_id})
            if todo is None:
                return '', 204

        if todo:
            return jsonify(todo), 200
        else:
            return '', 204

    def post(self):
        payload = request.json
        payload['_id'] = str(uuid4())
        todo_id = collection.insert_one(payload).inserted_id
        return str(todo_id), 201

    def delete(self, todo_id):
        if collection.find_one({'_id': todo_id}) is None:
            return '', 204
        collection.delete_one({'_id': todo_id})
        return '', 201


view = Todo.as_view('todo_api')
app.add_url_rule('/todo/', defaults={'todo_id': None}, view_func=view, methods=['GET'])
app.add_url_rule('/todo/', view_func=view, methods=['POST'])
app.add_url_rule('/todo/<todo_id>', view_func=view, methods=['GET', 'PUT', 'DELETE'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
