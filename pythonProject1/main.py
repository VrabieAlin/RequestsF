from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hello", methods=["POST"])
def hello():
    return jsonify({"message": "Hello world!"})

users = [
    {"id": 1, "name": "Alex"},
    {"id": 2, "name": "Andrei"}
]

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def update_user():
    new_user = request.get_json()
    new_user["id"] = len(users) + 1
    users.append(new_user)
    print(users)
    return jsonify(new_user), 201

app.run(debug=True)