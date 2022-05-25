import React, { Component } from 'react';
import { ButtonGroup, Button, Dropdown } from 'react-bootstrap';

// import { LoginForm } from '../index';

class LogInDropdown extends Component {
  render() {
    return (
      <div className="UserAccountDropdown">
        <Dropdown as={ButtonGroup}>
          <Button variant="success">Split Button</Button>

          <Dropdown.Toggle split variant="success" id="dropdown-split-basic" />

          <Dropdown.Menu>
            <Dropdown.Item href="/UserAccount">UserAccount</Dropdown.Item>
            <Dropdown.Item href="/Logout">Logout</Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown>
      </div>
    );
  }
}

export default LogInDropdown;
