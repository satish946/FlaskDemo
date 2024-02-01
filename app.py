from flask import Flask, jsonify, request
app = Flask(__name__)
users = [
    {
        'id': 1,
        'user_name': 'user1',
        'password': 'Welcome'
    },
    {
        'id': 2,
        'user_name': 'user2',
        'password': 'Welcome'
    }
]


@app.route('/')
def home():
    return 'Welcome'

# Get a specific user
@app.route('/users/<user_name>/<password>', methods=['GET'])
def get_user(user_name, password):
    user = next((user for user in users if user['user_name'] == user_name and user['password'] == password), None)
    if user is None:
        return jsonify({'error': 'user not Valid'}), 404
    return jsonify({'user': 'Successfully logged in'})

if __name__ == '__main__':
    app.run(debug=True)


# # Get all users
# @app.route('/users', methods=['GET'])
# def get_users():
#     return jsonify({'users': users})
#
#
#
#
#
# # Create a new user
# @app.route('/users', methods=['POST'])
# def create_user():
#     if not request.json or 'title' not in request.json:
#         return jsonify({'error': 'Title is required'}), 400
#
#     new_user = {
#         'id': users[-1]['id'] + 1,
#         'title': request.json['title'],
#         'done': False
#     }
#     users.append(new_user)
#
#     return jsonify({'user': new_user}), 201
#
#
# # Update an existing user
# @app.route('/users/<int:user_id>', methods=['PUT'])
# def update_user(user_id):
#     user = next((user for user in users if user['id'] == user_id), None)
#     if user is None:
#         return jsonify({'error': 'user not found'}), 404
#
#     if 'title' in request.json:
#         user['title'] = request.json['title']
#     if 'done' in request.json:
#         user['done'] = request.json['done']
#
#     return jsonify({'user': user})
#
#
# # Delete a user
# @app.route('/users/<int:user_id>', methods=['DELETE'])
# def delete_user(user_id):
#     global users
#     users = [user for user in users if user['id'] != user_id]
#     return jsonify({'result': True})
#
#
