from flask import Flask, request, jsonify, Response
from functools import wraps
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to the REST API'})

# @app.route('/create_subscription', methods=['POST'])
# def create_subscription():

'''Route to receive notifications from OSM'''
@app.route('/notifications', methods=['GET', 'POST'])
def notifications():
    # create_subscription()
    if request.method == 'GET':
        dados = request.json
        return Response(status=204)

    if request.method == 'POST':
        dados = request.json
        print(dados)
        return Response(status=204)

if __name__ == '__main__':
    app.run(port=5400, host='0.0.0.0')