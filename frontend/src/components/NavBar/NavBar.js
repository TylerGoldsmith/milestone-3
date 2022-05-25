import React, { useState, useEffect, Fragment } from 'react';
import { Link } from 'react-router-dom';

import { SearchBar, LogInDropdown } from '../index';


const NavBar = () => {
    const [isAuth, setIsAuth] = useState(false);

    useEffect(() => {
        if (localStorage.getItem('token') !== null) {
            setIsAuth(true);
        }
    }, []);

    return (
        <nav>
            <h1>NavBar</h1>
            <ul>
                {isAuth === true ? (
                    <li>
                        <Link to='/'>Home</Link>
                    </li>
                ) : (
                    <Fragment>
                        {' '}
                        <li>
                            <SearchBar />
                        </li>
                        <li>
                            <LogInDropdown />
                        </li>
                    </Fragment>
                )}
            </ul>
        </nav>
    );
};

export default NavBar;