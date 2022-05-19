import React, { Component } from 'react';
import { Route } from 'react-router-dom'

import { Home } from '../index';

class Container extends Component {
    render() {
        return (
            <div>
                <Route path='/'>
                    <Home />
                </Route>
            </div>
        );
    }
}

export default Container;