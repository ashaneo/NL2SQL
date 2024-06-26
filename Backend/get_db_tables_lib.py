import mysql.connector
from mysql.connector import Error


def connect_to_db(host, port, dbname, user, password):
    try:
        conn = mysql.connector.connect(
            host=host,
            port=port,
            database=dbname,
            user=user,
            password=password
        )
        if conn.is_connected():
            cursor = conn.cursor()
            return conn, cursor
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None, None


def get_all_table_names(cursor):
    try:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        table_names = [table[0] for table in tables]
        return table_names
    except Error as e:
        print("Error fetching table names", e)
        return []


def get_table_structure(cursor, table_name):
    print(f"Fetching structure for table {table_name}")
    try:
        cursor.execute(f"DESCRIBE `{table_name}`")         
        columns = cursor.fetchall()
        column_info = {}
        for column in columns:
            print(f"Column: {column}")
            print("debugginggg")
            column_name, column_type = column[0], column[1]
            print(f"Column Name: {column_name}, Column Type: {column_type}")
            # Simplify column types to generic types like TEXT, INT, etc.
            if 'char' in column_type or 'text' in column_type:
                column_type = 'TEXT'
            elif 'int' in column_type:
                column_type = 'INT'
            elif 'date' in column_type or 'time' in column_type:
                column_type = 'DATETIME'
            elif 'decimal' in column_type or 'double' in column_type or 'float' in column_type:
                column_type = 'FLOAT'
            else:
                column_type = 'OTHER'  # For other less common data types
            print(f"cccColumn Name: {column_name}, Column Type: {column_type}")
            column_info[column_name] = column_type
            print("DONEEEE")
        return column_info
    except Error as e:
        print(f"Error fetching structure for table {table_name}", e)
        return {}


def generate_single_create_table_sql(table_name, columns):
    sql = f"CREATE TABLE {table_name} ("     # Start the CREATE TABLE statement

    column_definitions = []  # Add columns to the statement
    for column_name, data_type in columns.items():
        column_definitions.append(f'"{column_name}" {data_type}')

    sql += ', '.join(column_definitions)

    sql += '); '

    return sql


def generate_create_table_sql(table_data):
    sql = ""
    for table_name, columns in table_data.items():
        sql += generate_single_create_table_sql(table_name, columns)
    return sql


def get_all_create_table_queries(host, port, dbname, user, password):
    print("Connecting to database.....")
    conn, cursor = connect_to_db(host, port, dbname, user, password)

    if conn is None or cursor is None:
        return {}

    print("Fetching Table Names...")

    table_names = get_all_table_names(cursor)

    print(table_names)
    
    all_table_structures = {}

    for table_name in table_names:
        table_structure = get_table_structure(cursor, table_name)
        all_table_structures[table_name] = table_structure
        print(f"Structure for table {table_name}: {table_structure}")

    print(all_table_structures)

    cursor.close()
    conn.close()

    create_table_query = generate_create_table_sql(all_table_structures)

    return create_table_query


# This is only to test this script individually
if __name__ == "__main__":
    # Database credentials
    host = '127.0.0.1'
    port = '3306'
    dbname = 'small_schema'
    user = 'root'
    password = '12345678'

    # Get table structures
    create_table_query = get_all_create_table_queries(
        host, port, dbname, user, password)

    # Print all table structures
    print(create_table_query)
