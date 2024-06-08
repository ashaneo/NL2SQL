from load_model_are_get_query.get_query import generate_query

import os
import sys

def generate_single_create_table_sql(table_name, columns):
    sql = f"CREATE TABLE {table_name} ("    

    column_definitions = []  
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

def generate_prompt(table_sql, question):
    prompt = f"tables:\n{table_sql}\nquery for: {question}"
    return prompt

def get_final_query(table_sql, question):
    prompt = generate_prompt(table_sql, question)
    print("this is the prompt", prompt)
    generated_sql = generate_query(prompt)
    return generated_sql

#This is only to test this script individually
if __name__ == '__main__':
    table_data = {
        "table1": {
            "column1": "TEXT",
            "column2": "TEXT",
            "column3": "TEXT"
        },
        "table2": {
            "column1": "TEXT",
            "column2": "TEXT",
            "column3": "TEXT"
        }
    }

    question = "What is the name of the person with id 1?"

    (get_final_query(table_data, question))
