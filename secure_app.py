from flask import Flask, request, jsonify

app = Flask(__name__)

# fake database
users = [
    {"id": 1, "name": "JOHN"},
    {"id": 2, "name": "RAHUL"}
]

# credentials
credentials = {
    "JOHN": {"password": "1234", "id": 1},
    "RAHUL": {"password": "1234", "id": 2}
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
            "token": str(credentials[username]["id"])   # simple token
        })

    return jsonify({"error": "Invalid credentials"}), 401


#  SECURE USER ENDPOINT (IDOR FIXED)
@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    token = request.headers.get("Authorization")

    # 1. Check if user is logged in
    if not token:
        return jsonify({"error": "Unauthorized"}), 401

    try:
        user_id = int(token)
    except:
        return jsonify({"error": "Invalid token"}), 400

    # 2. Authorization check (IMPORTANT FIX)
    if user_id != id:
        return jsonify({"error": "Access denied"}), 403

    # 3. Return only allowed user data
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)

    return jsonify({"error": "User not found"}), 404


# GET all users (optional - you can protect this too)
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


# ADD user
@app.route('/user', methods=['POST'])
def add_user():
    data = request.json
    users.append(data)
    return jsonify({"message": "User added successfully"})


# run server
if __name__ == '__main__':
    app.run(debug=True)
