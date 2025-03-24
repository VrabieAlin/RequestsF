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
def add_user():
    new_user = request.get_json()
    new_user["id"] = len(users) + 1
    users.append(new_user)
    print(users)
    return jsonify(new_user), 201

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    my_user = None
    for user in users:
        if user["id"] == user_id:
            my_user = user

    if my_user != None:
        data = request.get_json()
        my_user.update(data)
        return jsonify(my_user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return jsonify({"message": "User deleted"})


app.run(debug=True)