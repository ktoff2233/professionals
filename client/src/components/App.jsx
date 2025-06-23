import React, { useState } from 'react';
import './App.css';
import Trader from './Trader';

const App = () => {
    const [showTraderPage, setShowTraderPage] = useState(false);

    return (
        <div className="container">
            {!showTraderPage ? (
                <>
                    <h1 className="login-heading">Login</h1>
                    <form id="login-form" className="form">
                        <label htmlFor="username" className="label">Username:</label>
                        <input type="text" id="username" name="username" required className="input" />
                        <label htmlFor="password" className="label">Password:</label>
                        <input type="password" id="password" name="password" required className="input" />
                        <button type="button" onClick={() => setShowTraderPage(true)} className="button">Go to Trader Page</button>
                    </form>
                </>
            ) : (
                <Trader username="" />
            )}
        </div>
    );
};

export default App;