////////////////////////////////////////////////////////////////////////////////
/*                        Developer(s): Riley Conrardy                        */
////////////////////////////////////////////////////////////////////////////////

import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import Welcome from './views/Welcome';


////////////////////////////////////////////////////////////////////////////////
/*                             React Component(s)                             */
////////////////////////////////////////////////////////////////////////////////

class Quickstart extends React.Component {
  /* React component for Quickstart application. */

  constructor(props) {
    /* React constructor for Quickstart component. */

    super(props);
    this.state = {};
  }

  render() {
    /* React render for Quickstart component. */

    return (
      <Router>
        <Switch>
          <Route
            path='/'
            component={Welcome} />
        </Switch>
      </Router>
    );
  }
}


////////////////////////////////////////////////////////////////////////////////
/*                              React DOM Render                              */
////////////////////////////////////////////////////////////////////////////////

ReactDOM.render(
  <Quickstart />,
  document.getElementById('quickstart')
);
