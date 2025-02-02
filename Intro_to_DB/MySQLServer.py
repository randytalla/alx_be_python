
import mysql.connector
from mysql.connector import Error

def create_database(host_name, db_user, db_password, db_name):
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host=host_name,
            user=db_user,
            password=db_password
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Create the database if it does not exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")

        # Close the cursor and connection
        cursor.close()
        connection.close()

        print(f"Database '{db_name}' created successfully!")

    except Error as e:
        print(f"Failed to connect to the database: {e}")

if __name__ == "__main__":
    host_name = "localhost"
    db_user = "your_username"
    db_password = "your_password"
    db_name = "alx_book_store"

    create_database(host_name, db_user, db_password, db_name)