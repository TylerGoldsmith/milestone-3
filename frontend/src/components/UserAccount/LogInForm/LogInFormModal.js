import React, { Component, Fragment } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import { LogInForm } from "../../index";

class LogInFormModal extends Component {
  state = {
    modal: false
  };

  toggle = () => {
    this.setState(previous => ({
      modal: !previous.modal
    }));
  };

  render() {
    const create = this.props.create;

    var title = "Log in";
    var button = <Button onClick={this.toggle}>Log in</Button>;
    if (create) {
      title = "Log in";

      button = (
        <Button
          color="primary"
          className="float-right"
          onClick={this.toggle}
          style={{ minWidth: "200px" }}
        >
          Log in
        </Button>
      );
    }

    return (
      <Fragment>
        {button}
        <Modal isOpen={this.state.modal} toggle={this.toggle}>
          <ModalHeader toggle={this.toggle}>{title}</ModalHeader>

          <ModalBody>
            <LogInForm
              resetState={this.props.resetState}
              toggle={this.toggle}
              user_account={this.props.user_account}
            />
          </ModalBody>
        </Modal>
      </Fragment>
    );
  }
}

export default LogInFormModal;