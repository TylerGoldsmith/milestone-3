import React, { useState, useEffect, Fragment } from 'react';

const Home = () => {
  const [username, setUsername] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (localStorage.getItem('token') === null) {
      window.location.replace('http://localhost:3000/login');
    } else {
      fetch('http://127.0.0.1:8000/api/v1/todo/auth/username/', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Token ${localStorage.getItem('token')}`
        }
      })
        .then(res => res.json())
        .then(data => {
          setUsername(data.username);
          setLoading(false);
        });
    }
  }, []);

  return (
    <div>
      {loading === false && (
        <Fragment>
          <h1>Dashboard</h1>
          <h2>Hello {username}!</h2>
        </Fragment>
      )}
    </div>
  );
};

export default Home;