import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [message, setMessage] = useState('Click a button to get started!');

  const handleAction = async (action) => {
    try {
      const response = await axios.get(`http://localhost:8000/api/${action}`);
      setMessage(response.data.message);
    } catch (error) {
      console.error(error);
      setMessage('There was an error fetching the data!');
    }
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>{message}</h1>
      <button onClick={() => handleAction('action1')} style={{ marginRight: '10px' }}>
        Trigger Action 1
      </button>
      <button onClick={() => handleAction('action2')}>
        Trigger Action 2
      </button>
    </div>
  );
}

export default App;
