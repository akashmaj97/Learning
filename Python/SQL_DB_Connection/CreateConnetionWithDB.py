import mysql.connector

# Replace these with your actual MySQL database credentials
host = 'localhost'
database = 'akashtest'
user = 'root'
password = '12345'

try:
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    if connection.is_connected():
        db_info = connection.get_server_info()
        print(f'Connected to MySQL Server version {db_info}')
        cursor = connection.cursor()

        # Example query
        cursor.execute('SELECT DATABASE();')
        db_name = cursor.fetchone()
        print(f'Connected to database: {db_name}')

        # Closing the cursor and connection
        cursor.close()
        connection.close()
        print('MySQL connection closed.')

except mysql.connector.Error as e:
    print(f'Error connecting to MySQL: {e}')

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection closed.')

