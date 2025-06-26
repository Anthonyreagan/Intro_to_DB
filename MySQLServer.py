# MySQLServer.py

import mysql.connector
from mysql.connector import Error

def create_database():
    """
    Connects to MySQL server and creates the 'alx_book_store' database
    if it does not already exist.
    """
    connection = None
    try:
        # Establish connection to MySQL server
        # You may need to replace 'your_username' and 'your_password'
        # with your actual MySQL credentials.
        connection = mysql.connector.connect(
            host="localhost", # Or your MySQL server host
            user="Tony",
            password="Siangu@2002"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Execute SQL to create database if it doesn't exist
            # Using IF NOT EXISTS ensures the script does not fail if the DB exists.
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close the connection if it was established
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()