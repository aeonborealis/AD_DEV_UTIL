from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# user data
users = {
    "john@example.com": generate_password_hash("password"),
    "jane@example.com": generate_password_hash("password")
}

# login endpoint
@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    if email not in users:
        return jsonify({'message': 'Email not found'}), 400

    if not check_password_hash(users[email], password):
        return jsonify({'message': 'Invalid password'}), 400

    return jsonify({'message': 'Logged in successfully'}), 200

# register endpoint
@app.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')
    password = request.json.get('password')

    if email in users:
        return jsonify({'message': 'Email already registered'}), 400

    users[email] = generate_password_hash(password)

    return jsonify({'message': 'Registered successfully'}), 200

if __name__ == '__main__':
    app.run()
