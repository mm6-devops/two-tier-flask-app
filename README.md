# Two-Tier Flask Application

A secure login and signup system built with Flask and MySQL, featuring Docker containerization for easy deployment.

## Overview

This is a two-tier web application consisting of:
- **Frontend**: Flask web application serving HTML templates
- **Backend**: MySQL database for user authentication and storage

The application provides user registration, login, and a protected dashboard, with secure password hashing and session management.

## Features

- User registration with email validation
- Secure login with password verification
- Password hashing using Werkzeug security
- Session-based authentication
- Responsive UI with modern styling
- Database initialization and setup
- Docker containerization support

## Prerequisites

- Python 3.12+
- MySQL Server
- Docker and Docker Compose (for containerized deployment)

## Installation and Setup

### Method 1: Local Development

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd two-tier-flask-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   # Or if using poetry: poetry install
   ```

3. Set up the database:
   ```bash
   python setup_db.py
   ```
   
   This script will:
   - Create the `login_db` database
   - Create the `users` table with appropriate schema

4. Run the application:
   ```bash
   python main.py
   ```

5. Access the application at `http://localhost:5000`

### Method 2: Docker Deployment

1. Build and run with Docker Compose:
   ```bash
   docker-compose up --build
   ```

2. Access the application at `http://localhost:5000`

## Project Structure

```
two-tier-flask-app/
├── main.py              # Main Flask application
├── setup_db.py          # Database initialization script
├── Dockerfile           # Container build instructions
├── docker-compose.yaml  # Multi-container orchestration
├── pyproject.toml       # Project metadata and dependencies
├── .python-version      # Python version specification
├── .gitignore           # Git ignore rules
├── templates/           # HTML templates
│   ├── base.html        # Base template with common layout
│   ├── login.html       # Login page
│   ├── signup.html      # Registration page
│   └── dashboard.html   # User dashboard
└── README.md            # This file
```

## Configuration

### Database Configuration

The application connects to MySQL using these default settings:
- Host: localhost (or mysql in Docker)
- Username: root
- Password: xxxxxxxx
- Database: login_db

To change these values, update both `main.py` and `setup_db.py` (and `docker-compose.yaml` for Docker deployments).

### Environment Variables (Docker)

When running with Docker, the following environment variables are configured:
- `DB_HOST`: Database hostname
- `DB_USER`: Database username
- `DB_PASSWORD`: Database password
- `DB_NAME`: Database name

## Database Schema

The application creates a `users` table with the following structure:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Security Features

- Passwords are hashed using Werkzeug's security functions
- SQL injection prevention through parameterized queries
- Session-based authentication
- Input validation on both client and server side
- Secure session management with secret keys

## API Routes

- `GET /` - Redirects to login page
- `GET/POST /login` - User login page and authentication
- `GET/POST /signup` - User registration page and processing
- `GET /dashboard` - Protected user dashboard
- `GET /logout` - User logout functionality

## Templates

The application uses Jinja2 templating with a base template structure:

- `base.html` - Contains the common HTML structure and styles
- `login.html` - Login form with validation
- `signup.html` - Registration form with password confirmation
- `dashboard.html` - User-specific dashboard page

## Docker Configuration

The Docker setup includes:
- Flask application container
- MySQL database container
- Automatic network configuration
- Health checks for database readiness
- Volume persistence for database data

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Ensure MySQL server is running
   - Verify credentials in configuration files
   - Check that the database has been created

2. **Port Already in Use**
   - Change the port mapping in `docker-compose.yaml`
   - Or stop other applications using port 5000

3. **Dependency Issues**
   - Ensure Python 3.12+ is installed
   - Update pip and reinstall dependencies if needed

### Docker-specific Issues

1. **Container Won't Start**
   - Check logs: `docker-compose logs`
   - Ensure Docker daemon is running

2. **Database Not Ready**
   - The application waits for the database to be healthy
   - Check database container logs for initialization issues

## Development

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Adding New Features

When adding new features:
- Follow the existing code style
- Ensure database queries are parameterized
- Add appropriate error handling
- Update documentation as needed

## License

This project is open-source and available under the MIT License.

## Authors

- Created by the Flask-MySQL application developer team