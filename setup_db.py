"""
Database setup script to create the login_db database
Run this before starting the application
"""

import mysql.connector
from mysql.connector import Error

# Configuration
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'masoom842155'
}

try:
    # Connect to MySQL without specifying a database
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    
    # Create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS login_db")
    print("✓ Database 'login_db' created successfully")
    
    # Close and reconnect to the new database
    cursor.close()
    connection.close()
    
    # Now create tables
    config['database'] = 'login_db'
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    
    # Create users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    connection.commit()
    print("✓ Table 'users' created successfully")
    print("\nDatabase setup completed!")
    print("You can now run: python main.py")
    
except Error as e:
    print(f"✗ Error: {e}")
    print("\nMake sure:")
    print("1. MySQL server is running")
    print("2. Update the username/password in config if needed")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
