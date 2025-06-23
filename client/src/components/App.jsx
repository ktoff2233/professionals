import React, { useState } from 'react';
import './App.css';

const App = () => {
    const [message, setMessage] = useState('');

    const handleLogin = async (event) => {
        event.preventDefault();
        const id = event.target.id.value;
        const password = event.target.password.value;

        try {
            const response = await fetch('http://localhost:8000/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ id, password }),
            });
            const data = await response.json();
            setMessage(data.message);
        } catch (error) {
            setMessage('Login failed');
        }
    };

    return (
        <div className="container">
            <h1 className="login-heading">Login</h1>
            <form id="login-form" onSubmit={handleLogin} className="form">
                <label htmlFor="id" className="label">ID:</label>
                <input type="text" id="id" name="id" required className="input" />
                <label htmlFor="password" className="label">Password:</label>
                <input type="password" id="password" name="password" required className="input" />
                <button type="submit" className="button">Login</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
};

export default App;