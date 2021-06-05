import mysql.connector

def get_connection():
    return mysql.connector.connect(
        user='',
        password='',
        host='',
        port='',
        database=''
    )