from flask import Flask, request, jsonify, session
from flask_session import Session
from flask_cors import CORS, cross_origin
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Import custom libraries
try:
    from get_db_tables_lib import get_all_create_table_queries, connect_to_db
    from text_to_sql_lib import get_final_query
except ImportError as e:
    logging.error("Error importing get_db_tables_lib: %s", e)

app = Flask(__name__)
CORS(app, supports_credentials=True)

# Temporary store
query_store = {}


@app.route('/')
@cross_origin()
def intro():
    return 'Text to SQL Application!'


@app.route('/api/db_credentials', methods=['POST'])
def save_create_table_queries():
    try:
        data = request.json

        query_store['db_credentials'] = data

        host = data.get('host')
        port = data.get('port')
        user = data.get('user')
        password = data.get('password')
        database = data.get('database')

        if None in [host, port, user, password, database]:
            return jsonify({"error": "Missing database credentials"}), 400

        created_table_queries = get_all_create_table_queries(
            host, port, database, user, password)
        print("FUNCTION CAME HERE")

        # Storing create table queries in the in-memory "database"
        query_store['table_query'] = created_table_queries

        print(query_store)

        logging.debug("Queries stored")
        return jsonify({"message": "Credentials successfully saved"}), 200

    except Exception as e:
        logging.error("Error saving credentials: %s", e)
        return jsonify({"error": "Failed to save credentials"}), 500


@app.route('/api/question', methods=['POST'])
def generate_sql_query():
    try:
        question = request.json.get('question')
        logging.debug("Question received")
        if not question:
            return jsonify({"error": "No question provided"}), 400

        query_to_create_tables = query_store.get('table_query')

        if not query_to_create_tables:
            logging.error("Create table queries not found in query store")
            return jsonify({"error": "Create table queries not found"}), 404
        else:
            logging.debug("Create table queries found")
            print("Create table queries found")

        sql_query = get_final_query(query_to_create_tables, question)
        query_store['sql_query'] = sql_query

        print("SQL QUERY", sql_query)
        return jsonify({"sqlQuery": sql_query}), 200

    except Exception as e:
        logging.error("Error generating SQL query: %s", e)
        return jsonify({"error": "Failed to generate SQL query"}), 500


@app.route('/api/run_query', methods=['POST'])
def run_query():

    db_creds = query_store.get('db_credentials')

    host = db_creds.get('host')
    port = db_creds.get('port')
    user = db_creds.get('user')
    password = db_creds.get('password')
    database = db_creds.get('database')

    sql_query = query_store.get('sql_query')

    conn, cursor = connect_to_db(host, port, database, user, password)

    try:
        cursor.execute(sql_query)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = [dict(zip(columns, row)) for row in result]
        return jsonify(data)
    except Exception as e:
        logging.error("Error running SQL query: %s", e)
        return jsonify({"error": "Failed to run SQL query"}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
