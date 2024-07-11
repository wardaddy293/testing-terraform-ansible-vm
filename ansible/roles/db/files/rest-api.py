from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='my_user',
        password='my_password',
        database='my_database'
    )
    return connection

@app.route('/top_scorers', methods=['GET'])
def get_top_scorers():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT country, goals FROM top_scorers')
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

