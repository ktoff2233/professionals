import React from 'react';
import './Trader.css';

const Trader = () => {
    return (
        <div className="trader-container">
            <h1 className="trader-heading">Trader</h1>
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
                    <tr>
                        <td>1</td>
                        <td>Joe</td>
                        <td>Shmo</td>
                        <td>85</td>
                        <td>1001</td>
                    </tr>
                </tbody>
            </table>
            <h2 className="transactions-heading">Transactions</h2>
            <table className="transactions-table">
                <thead>
                    <tr>
                        <th>Transaction ID</th>
                        <th>Purchase Date</th>
                        <th>Sell Date</th>
                        <th>Ticker</th>
                        <th>Quantity</th>
                        <th>Purchase Price</th>
                        <th>Sell Price</th>
                        <th>Type</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>101</td>
                        <td>2023-01-01</td>
                        <td>2023-01-10</td>
                        <td>XYZ</td>
                        <td>50</td>
                        <td>$100</td>
                        <td>$120</td>
                        <td>Call</td>
                    </tr>
                </tbody>
            </table>
        </div>
    );
};

export default Trader;
