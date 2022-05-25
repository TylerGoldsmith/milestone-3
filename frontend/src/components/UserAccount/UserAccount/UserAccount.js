import React, { Component } from 'react';

import { LogInFormModal, SignUpFormModal } from '../../index';

class UserAccount extends Component {
    render() {
        return (
            <div className="UserAccount">
                <LogInFormModal />
                <SignUpFormModal />
            </div>
        );
    }
}

export default UserAccount;