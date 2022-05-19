import React, { Component } from 'react';
import { Route, Routes, BrowserRouter } from 'react-router-dom';

import { Home, NavBar, LoginForm } from '../index';

class Container extends Component {
    render() {
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
                                <LoginForm />
                            </div>
                        } />
                    </Routes>
                </BrowserRouter>
            </div>
        );
    }
}

export default Container;