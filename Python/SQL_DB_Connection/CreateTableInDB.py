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

        # Create a new table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE
        )
        """
        cursor.execute(create_table_query)
        print("Employees table created successfully.")

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
