import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="yourpassword", database="chatbot")
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def create_tables():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chatbot (
                id INT AUTO_INCREMENT PRIMARY KEY,
                statement TEXT,
                response TEXT
            )
        """)
        connection.commit()
        cursor.close()
        connection.close()

def insert_training_data(training_data):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        for statement, response in training_data:
            cursor.execute("INSERT INTO chatbot (statement, response) VALUES (%s, %s)", (statement, response))
        connection.commit()
        cursor.close()
        connection.close()