# TESTING

"devDependencies": {
    "jest": "^26.6.0",
    "enzyme": "^3.11.0",
    "enzyme-adapter-react-16": "^16.4.0-0"
  },





# Client-side Web Application

This project is a web application built with a React front-end and a Flask back-end, utilizing a MySQL database. Below are the instructions for setting up and running the client-side application.

## Getting Started

### Prerequisites

- Node.js (version 14 or higher)
- npm (Node Package Manager)

### Installation

1. Navigate to the client directory:

   ```
   cd client
   ```

2. Install the dependencies:

   ```
   npm install
   ```

### Running the Application

To start the development server, run:

```
npm start
```

This will launch the application in your default web browser at `http://localhost:3000`.

### Folder Structure

- `src/`: Contains the source code for the React application.
  - `components/`: Contains React components.
  - `tests/`: Contains unit tests for the components.
- `public/`: Contains static files, including the main HTML file.
- `package.json`: Configuration file for npm, including scripts and dependencies.

### Running Tests

To run the unit tests, use the following command:

```
npm test
```

This will execute the tests defined in the `tests` directory.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.