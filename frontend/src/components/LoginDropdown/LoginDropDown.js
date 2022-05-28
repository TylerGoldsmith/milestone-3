import React, { Component, useState, useEffect, Fragment } from 'react';
import { ButtonGroup, Button, Dropdown } from 'react-bootstrap';

// import { LoginForm } from '../index';

const LogInDropdown = () => {
  const [isAuth, setIsAuth] = useState(false);

  useEffect(() => {
    if (localStorage.getItem('token') !== null) {
      setIsAuth(true);
    }
  }, []);
  return (
    <div className="UserAccountDropdown">
      <Dropdown as={ButtonGroup}>

        <Button variant="success">Split Button</Button>

        <Dropdown.Toggle split variant="success" id="dropdown-split-basic" />

        <Dropdown.Menu>
          {isAuth === true ? (
            <Fragment>
              {' '}
              <Dropdown.Item href="/Login">Login</Dropdown.Item>
              <Dropdown.Item href="/SignUp">Signup</Dropdown.Item>
            </Fragment>
            
          ) : (
            <Fragment>
              {' '}
              <Dropdown.Item href="/UserAccount">UserAccount</Dropdown.Item>
              <Dropdown.Item href="/Logout">Logout</Dropdown.Item>
            </Fragment>


          )
          }
        </Dropdown.Menu>

      </Dropdown>
    </div>



  );
}


export default LogInDropdown;
