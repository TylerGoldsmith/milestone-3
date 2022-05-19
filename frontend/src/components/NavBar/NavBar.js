import React, { Component } from 'react';

import { SearchBar, LoginDropdown } from '../index';

class NavBar extends Component {

    render() {
        return (
            <div className="NavBar">
                <ul className="NavBarUL">
                    <li><a href="/">Home</a></li>
                    <li><SearchBar
                    // searchQuery={searchQuery}
                    // setSearchQuery={setSearchQuery}
                    /></li>
                    <li><LoginDropdown /></li>
                </ul>
            </div>
        );
    }
}

export default NavBar;