from flask import Flask, request, jsonify

app = Flask(__name__)

# fake database
users = [
    {"id": 1, "name": "Sayanth"},
    {"id": 2, "name": "Rahul"}
]

# credentials
credentials = {
    "Sayanth": {"password": "1234", "id": 1},
    "Rahul": {"password": "1234", "id": 2}
}

#  LOGIN ROUTE
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in credentials and credentials[username]["password"] == password:
        return jsonify({
            "message": "Login successful",
            "user_id": credentials[username]["id"]
        })

    return jsonify({"error": "Invalid credentials"}), 401


# 1. GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# 2. GET single user
@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    for user in users:
        if user["id"] == id:
            return jsonify(user)
    return {"error": "User not found"}

# 3. POST new user
@app.route('/user', methods=['POST'])
def add_user():
    data = request.json
    users.append(data)
    return {"message": "User added successfully"}

# run server
if __name__ == '__main__':
    app.run(debug=True)
