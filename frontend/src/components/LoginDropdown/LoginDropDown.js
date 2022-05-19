import React, { Component } from 'react';
import { ButtonGroup, Button, Dropdown } from 'react-bootstrap';

// import { LoginForm } from '../index';

class LoginDropdown extends Component {
  render() {
    return (
      <div className="LoginDropdown">
        <Dropdown as={ButtonGroup}>
          <Button variant="success">Split Button</Button>

          <Dropdown.Toggle split variant="success" id="dropdown-split-basic" />

          <Dropdown.Menu>
            <Dropdown.Item href="/Login">Login</Dropdown.Item>
            <Dropdown.Item href="#/action-2">Logout</Dropdown.Item>
            <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown>
      </div>
    );
  }
}

export default LoginDropdown;
