from flask import Flask, request, jsonify, Response
from functools import wraps

app = Flask(__name__)


# Function to verify credentials (replace this with your actual authentication logic)
def verify_authentication(username, password):
    # Replace this with your actual authentication mechanism (e.g., database lookup)
    return username == 'admin' and password == 'admin'


# Decorator to check for authentication before executing a route
def authentication_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization

        # For POST requests with JSON data
        if request.method == 'POST' and request.is_json:
            data = request.json
            print(data)
            username = request.form.get('userName')  # Retrieve username from JSON payload
            password = request.form.get('password')  # Retrieve password from JSON payload

            if not username or not password:
                return jsonify({'message': 'Username and password required in JSON payload'}), 400

            if not verify_authentication(username, password):
                return jsonify({'message': 'Invalid credentials!'}), 401

            return f(*args, **kwargs)

        return jsonify({'message': 'Invalid request'}), 400
    return decorated


@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to the REST API'})

# @app.route('/create_subscription', methods=['POST'])
# def create_subscription():

@app.route('/notifications', methods=['POST', 'GET'])
def receive_notification():
    # create_subscription()
    return Response(status=204)

    if request.method == 'POST':
        print(request.text)
        # data = request.get_json()
        # print(data)
        return Response(status=204)


if __name__ == '__main__':
    app.run(port=5400, host='0.0.0.0')
