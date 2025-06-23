# README for the Flask Server

## Overview
This is the server-side application of the web application project, built using Flask. It serves as the back-end for the React front-end, handling API requests and interacting with the MySQL database.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd web-app-project/server
   ```

2. **Create a Virtual Environment**
   It is recommended to use a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   Install the required Python packages listed in `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**
   Ensure that you have a MySQL database set up. You can use the `schema.sql` file located in the `database` directory to create the necessary tables.
   ```bash
   mysql -u <username> -p <database_name> < ../database/schema.sql
   ```

5. **Run the Application**
   Start the Flask server.
   ```bash
   flask run
   ```

## Testing
Unit tests for the Flask application can be found in the `tests` directory. To run the tests, ensure you are in the virtual environment and execute:
```bash
pytest
```

## API Endpoints
Document your API endpoints here, including request methods, paths, and expected responses.

## License
This project is licensed under the MIT License. See the LICENSE file for details.