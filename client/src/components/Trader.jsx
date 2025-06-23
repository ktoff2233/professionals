import React, { useState, useEffect } from 'react';
import './Trader.css';

const Trader = ({ traderId }) => {
    const [traderData, setTraderData] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchTraderData = async () => {
            try {
                const response = await fetch(`http://localhost:8000/traders/${traderId}`);
                const data = await response.json();
                setTraderData(data);
                setLoading(false);
            } catch (error) {
                console.error("Error fetching trader data:", error);
                setLoading(false);
            }
        };

        fetchTraderData();
    }, [traderId]);

    return (
        <div className="trader-container">
            <h1 className="trader-heading">Trader Information</h1>
            {loading ? (
                <p>Loading...</p>
            ) : (
                <table className="trader-table">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>First Name</th>
                            <th>Last Name</th>
                            <th>Score</th>
                            <th>Manager ID</th>
                        </tr>
                    </thead>
                    <tbody>
                        {traderData.map((trader) => (
                            <tr key={trader.id}>
                                <td>{trader.id}</td>
                                <td>{trader.fname}</td>
                                <td>{trader.lname}</td>
                                <td>{trader.score}</td>
                                <td>{trader.manager_id}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            )}
        </div>
    );
};

export default Trader;
