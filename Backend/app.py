from flask import jsonify, request, Flask
from flask_cors import CORS, cross_origin

# Create a Flask app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Define a route and its handler

@app.route('/')
@cross_origin()
def intro():
    return 'Text to SQL Application!'

@app.route("/get-query-for-one-table", methods=["POST"])
@cross_origin()
def query_for_one_table():
    body = request.json
    if not body:
        return jsonify({"message": "Cannot decode json from body"}), 422
    else:
        print("RECEIVED REQUEST")
        table_number = body["table_number"]
        table_data = body["table_data"]
        question = body["question"]
        
# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
