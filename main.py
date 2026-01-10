from flask import Flask, render_template, request, redirect, session, url_for
import mysql.connector
from mysql.connector import Error
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = 'f3104574bebfc6418b679715df0a319f'

# MySQL Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'masoom842155',
    'database': 'login_db'
}

def get_db_connection():
    """Create a database connection"""
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def init_db():
    """Initialize database and create users table"""
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
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
            print("Database initialized successfully")
        except Error as e:
            print(f"Error creating table: {e}")
        finally:
            cursor.close()
            connection.close()

@app.route('/')
def index():
    """Home page"""
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page and logic"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor(dictionary=True)
            try:
                cursor.execute("SELECT id, username, password FROM users WHERE username = %s", (username,))
                user = cursor.fetchone()
                
                if user and check_password_hash(user['password'], password):
                    session['user_id'] = user['id']
                    session['username'] = user['username']
                    return redirect(url_for('dashboard'))
                else:
                    return render_template('login.html', error='Invalid username or password')
            except Error as e:
                print(f"Error: {e}")
                return render_template('login.html', error='Database error')
            finally:
                cursor.close()
                connection.close()
        else:
            return render_template('login.html', error='Database connection error')
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Signup page and logic"""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validation
        if not username or not email or not password:
            return render_template('signup.html', error='All fields are required')
        
        if password != confirm_password:
            return render_template('signup.html', error='Passwords do not match')
        
        if len(password) < 6:
            return render_template('signup.html', error='Password must be at least 6 characters')
        
        # Hash password
        hashed_password = generate_password_hash(password)
        
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute(
                    "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                    (username, email, hashed_password)
                )
                connection.commit()
                return render_template('signup.html', success='Signup successful! Please login.')
            except Error as e:
                if 'Duplicate entry' in str(e):
                    if 'username' in str(e):
                        return render_template('signup.html', error='Username already exists')
                    elif 'email' in str(e):
                        return render_template('signup.html', error='Email already exists')
                else:
                    print(f"Error: {e}")
                    return render_template('signup.html', error='Error during signup')
            finally:
                cursor.close()
                connection.close()
        else:
            return render_template('signup.html', error='Database connection error')
    
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    """User dashboard"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    return render_template('dashboard.html', username=session.get('username'))

@app.route('/logout')
def logout():
    """Logout user"""
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    # Initialize database on first run
    init_db()
    
    # Run the Flask app
    app.run(debug=True, host='localhost', port=5000)
