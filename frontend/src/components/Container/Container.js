import React, { Component } from 'react';
import { Route, Routes, BrowserRouter } from 'react-router-dom';

import { Home, NavBar, UserAccount, Logout } from '../index';

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
                        <Route exact path="/UserAccount" element={
                            <div>
                                <UserAccount />
                            </div>
                        } />
                        <Route exact path="/Logout" element={
                            <div>
                                <Logout />
                            </div>
                        } />
                    </Routes>
                </BrowserRouter>
            </div>
        );
    }
}

export default Container;