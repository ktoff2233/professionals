# professionals

Google Doc: https://docs.google.com/document/d/1bJ4XtF9Ioqq5MCW53HXyMzRXsnFqFr_qwKQEf3PdXs8/edit?usp=sharing

This project is a web application that consists of a React front-end, a Flask back-end, and a MySQL database. Below are the instructions for setting up and running the application.

## Project Structure

```
web-app-project
├── client                # React front-end
│   ├── src               # Source files for the React app
│   │   ├── components     # React components
│   │   ├── tests          # Unit tests for components
│   │   └── index.jsx      # Entry point for the React application
│   ├── public            # Public assets
│   │   └── index.html     # Main HTML file
│   ├── package.json      # npm configuration file
│   └── README.md         # Documentation for the client-side application
├── server                # Flask back-end
│   ├── app               # Application code
│   │   ├── __init__.py    # Initializes the Flask app
│   │   ├── routes.py      # Defines the API routes
│   │   └── models.py      # Database models
│   ├── tests             # Unit tests for the server
│   │   └── test_routes.py  # Tests for the Flask routes
│   ├── requirements.txt   # Python dependencies
│   └── README.md         # Documentation for the server-side application
├── database              # Database schema
│   └── schema.sql        # SQL commands to create the database schema
└── README.md             # Overall documentation for the project
```

## Getting Started

### Prerequisites

- Node.js and npm for the client-side application
- Python and pip for the server-side application
- MySQL database

### Client Setup

1. Navigate to the `client` directory:
   ```
   cd client
   ```

2. Install the dependencies:
   ```
   npm install
   ```

3. Start the React application:
   ```
   npm start
   ```

### Server Setup

1. Navigate to the `server` directory:
   ```
   cd server
   ```

2. Install the Python dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the database using the `schema.sql` file located in the `database` directory.

4. Start the Flask application:
   ```
   python -m app
   ```

## Running Tests

### Client Tests

To run the unit tests for the React application, navigate to the `client` directory and run:
```
npm test
```

### Server Tests

To run the unit tests for the Flask application, navigate to the `server` directory and run:
```
pytest
```

## License

This project is licensed under the MIT License.