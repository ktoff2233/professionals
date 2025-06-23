import React, { useState } from 'react';

const App = () => {
    const [data, setData] = useState(null);

    const fetchData = async () => {
        try {
            const response = await fetch('/api/data');
            const result = await response.json();
            setData(result);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    return (
        <div>
            <h1>Welcome to the Web App</h1>
            <button onClick={fetchData}>Fetch Data</button>
            {data && <pre>{JSON.stringify(data, null, 2)}</pre>}
        </div>
    );
};

export default App;