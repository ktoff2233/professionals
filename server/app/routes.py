from flask import Blueprint, jsonify, request

# Create a Blueprint for the routes
api = Blueprint('api', __name__)

@api.route('/api/example', methods=['GET'])
def example_route():
    return jsonify({"message": "This is an example route."})

@api.route('/api/data', methods=['POST'])
def data_route():
    data = request.json
    return jsonify({"received": data}), 201

# Add more routes as needed
