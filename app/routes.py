from flask import Blueprint, jsonify, request

main = Blueprint('main', __name__)

# Banco de dados temporário em memória
tasks = []
next_id = 1

@main.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "service": "taskflow-api"})

@main.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks, "total": len(tasks)})

@main.route('/tasks', methods=['POST'])
def create_task():
    global next_id
    data = request.get_json()

    if not data or 'title' not in data:
        return jsonify({"error": "Campo 'title' é obrigatório"}), 400

    task = {
        "id": next_id,
        "title": data['title'],
        "done": False
    }
    tasks.append(task)
    next_id += 1

    return jsonify(task), 201