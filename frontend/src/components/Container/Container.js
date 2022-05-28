import React, { useState, useEffect } from 'react';
import { Route, Routes, BrowserRouter } from 'react-router-dom';

import { Home, NavBar, LogInForm, Logout, SignUpForm } from '../index';

const Container = () => {
    const [userEmail, setUserEmail] = useState('');
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        if (localStorage.getItem('token') === null) {
            window.location.replace('http://localhost:3000/');
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
                    setUserEmail(data.email);
                    setLoading(false);
                });
        }
    }, []);

    return (
        <div className="Container">
            <BrowserRouter>
                <NavBar />
                <Routes>
                    <Route exact path="/" element={
                        <div>
                            <Home />
                        </div>
                    } />
                    <Route exact path="/Login" element={
                        <div>
                            <LogInForm />
                        </div>
                    } />
                    <Route exact path="/Logout" element={
                        <div>
                            <Logout />
                        </div>
                    } />
                    <Route exact path="/SignUp" element={
                        <div>
                            <SignUpForm />
                        </div>
                    } />
                </Routes>
            </BrowserRouter>
        </div>
    );
}


export default Container;