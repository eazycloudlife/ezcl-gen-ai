from flask import Flask, request, jsonify
from langchain_helper import get_few_shot_db_chain

# Create a Flask application
app = Flask(__name__)

# Define a route for the endpoint '/device'
@app.route('/device', methods=['GET'])
def hello():
    question = "How many manager are there?"
    chain = get_few_shot_db_chain()
    response = chain.run(question)
    return jsonify({'result': response})

# Endpoint for handling POST requests
@app.route('/api/1.0/inventory', methods=['POST'])
def post_data():
    data = request.json  # Get JSON data from POST request body
    question = data["message"]
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    # Return a JSON response
    return jsonify({'message': 'Data received successfully', 'result': response}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
