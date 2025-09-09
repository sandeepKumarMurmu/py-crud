import datetime
import jwt
from flask import Flask, request, jsonify

app = Flask(__name__)

# Default route
@app.route('/')
def home():
    return "Hello, Flask!"

# Example API route
@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')
    return jsonify({"message": f"Hello, {name}!"})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data:  # None or empty dict
        return jsonify({"error": "Request body cannot be empty"}), 400
    
    username = data.get('username')
    password = data.get('password')

    if username == 'admin' and password == 'admin@123':
        token = jwt.encode({"username":username,"password":password},"test@123", algorithm="HS256")
        return jsonify({"token": token})
    return jsonify({"message":"Unauthorized"}), 401

if __name__ == '__main__':
    app.run(debug=True)
