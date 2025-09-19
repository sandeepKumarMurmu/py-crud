from flask import Flask, request, jsonify
import jwt, datetime

MY_SECRETE = "mysecrete"
app = Flask(__name__)

users = [
    {"username": "user1", "email": "user1@example.com", "password": "pass123"},
    {"username": "user2", "email": "user2@example.com", "password": "pass234"},
    {"username": "user3", "email": "user3@example.com", "password": "pass345"},
    {"username": "user4", "email": "user4@example.com", "password": "pass456"},
    {"username": "user5", "email": "user5@example.com", "password": "pass567"},
    {"username": "user6", "email": "user6@example.com", "password": "pass678"},
    {"username": "user7", "email": "user7@example.com", "password": "pass789"},
    {"username": "user8", "email": "user8@example.com", "password": "pass890"},
    {"username": "user9", "email": "user9@example.com", "password": "pass901"},
    {"username": "user10", "email": "user10@example.com", "password": "pass012"},
]

@app.route("/", methods=["GET"])
def check():
    return {"status": "success", "message": "Test route working!"}, 200

@app.route("/auth/login", methods=["POST"])
def login():
    return {"status": "success", "message": "Login route working!"}, 200


@app.route("/auth/signup", methods=["POST"])
def signup():
    data = request.get_json() or {}

    email = data.get("email")
    emails = {user["email"] for user in users}

    if email in emails:
        return jsonify({"message":f"User already available with email {email}"}), 400
    
    payload = { 
        "username": data.get("username"),
        "email": data.get("email"),
        "password": data.get("password")
        }
    
    users.append(payload)

    token = jwt.encode({**payload, "exp":datetime.datetime.now() + datetime.timedelta(hours=1)}, MY_SECRETE, algorithm="HS256")
    print(token)
    return jsonify({
        "message": "User registered.",
        "data": {
            "token": token,
            "email": data.get("email")
        }
    }), 200

if __name__ == "__main__":
    app.run(debug=True)