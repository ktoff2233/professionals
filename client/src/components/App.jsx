import React from 'react';
import './App.css';

const App = () => {
    return (
        <div className="container">
            <h1 className="login-heading">Login</h1>
            <form id="login-form" action="/login" method="POST" className="form">
                <label for="id" className="label">ID:</label>
                <input type="text" id="id" name="id" required className="input" />
                <label for="password" className="label">Password:</label>
                <input type="password" id="password" name="password" required className="input" />
                <button type="submit" className="button">Login</button>
            </form>
        </div>
    );
};

export default App;