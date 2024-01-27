#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def check_mysql_access():
    db_config = {
        'user': 'holberton_user',
        'password': 'projectcorrection280hbtn',
        'host': 'localhost',
        'database': 'tyrell_corp'
    }

    try:
        # Connect to MySQL
        connection = mysql.connector.connect(**db_config)

        # Check SELECT permission on nexus6 table
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM nexus6 LIMIT 1;")

        # If execution is successful, access is correct
        print("Correct grants given")

    except Error as e:
        print(e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    check_mysql_access()
