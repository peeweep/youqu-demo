from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 解决跨域问题

# 临时内存数据库
users = {
    1: {"name": "Alice", "age": 25},
    2: {"name": "Bob", "age": 30}
}

@app.before_request
def log_request_info():
    """记录请求日志"""
    app.logger.debug(f"Request: {request.method} {request.url}")
    app.logger.debug(f"Headers: {dict(request.headers)}")
    app.logger.debug(f"Body: {request.get_data()}")

@app.route('/api/hello', methods=['GET'])
def hello():
    """基础 GET 接口"""
    return jsonify({"code": 0, "msg": "success", "data": "Hello, World!"})

@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """带路径参数的 GET 接口"""
    user = users.get(user_id)
    if user:
        return jsonify({"code": 0, "msg": "success", "data": user})
    return jsonify({"code": 404, "msg": "User not found"}), 404

@app.route('/api/search', methods=['GET'])
def search():
    """带查询参数的 GET 接口"""
    query = request.args.get('q', '')
    return jsonify({
        "code": 0,
        "msg": "success",
        "data": f"Search results for: {query}"
    })

@app.route('/api/login', methods=['POST'])
def login():
    """表单 POST 接口"""
    if not request.is_json:
        return jsonify({"code": 400, "msg": "Request must be JSON"}), 400
    
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"code": 400, "msg": "Missing parameters"}), 400

    if username == "admin" and password == "123456":
        return jsonify({"code": 0, "msg": "Login success"})
    return jsonify({"code": 401, "msg": "Invalid credentials"}), 401

@app.route('/api/users', methods=['POST'])
def create_user():
    """JSON POST 接口"""
    if not request.is_json:
        return jsonify({"code": 400, "msg": "Request must be JSON"}), 400
    
    user_data = request.get_json()
    new_id = max(users.keys()) + 1
    users[new_id] = user_data
    return jsonify({"code": 0, "msg": "User created", "data": {"id": new_id}}), 201

@app.route('/api/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """PUT 接口"""
    if user_id not in users:
        return jsonify({"code": 404, "msg": "User not found"}), 404
    
    update_data = request.get_json()
    users[user_id].update(update_data)
    return jsonify({"code": 0, "msg": "User updated"})

@app.route('/api/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """DELETE 接口"""
    if user_id not in users:
        return jsonify({"code": 404, "msg": "User not found"}), 404
    
    del users[user_id]
    return jsonify({"code": 0, "msg": "User deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


