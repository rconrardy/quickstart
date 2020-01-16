////////////////////////////////////////////////////////////////////////////////
/*                        Developer(s): Riley Conrardy                        */
////////////////////////////////////////////////////////////////////////////////

import React from 'react';
import ReactDOM from 'react-dom';


////////////////////////////////////////////////////////////////////////////////
/*                             React Component(s)                             */
////////////////////////////////////////////////////////////////////////////////

class Welcome extends React.Component {
  /* React component for Welcome application. */

  constructor(props) {
    /* React constructor for Welcome component. */

    super(props);
    this.state = {};
  }

  render() {
    /* React render for Welcome component. */

    return (
      <div
        id="welcome"
        className="welcome">
        <h1>Welcome Component</h1>
      </div>
    );
  }
} export default Welcome;
