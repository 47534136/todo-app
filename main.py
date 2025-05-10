from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
TASKS_FILE = 'app/tasks.json'

# Cargar tareas desde archivo
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

# Guardar tareas en archivo
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    tasks = load_tasks()
    new_task = request.json
    tasks.append(new_task)
    save_tasks(tasks)
    return jsonify({'message': 'Tarea agregada'}), 201

@app.route('/tasks/<int:index>', methods=['DELETE'])
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        deleted = tasks.pop(index)
        save_tasks(tasks)
        return jsonify({'message': 'Tarea eliminada', 'tarea': deleted})
    return jsonify({'error': 'Índice inválido'}), 400

if __name__ == '__main__':
    app.run(debug=True)
