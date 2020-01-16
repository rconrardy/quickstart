################################################################################
"""                       Developer(s): Riley Conrardy                       """
################################################################################

import flask
import flask_login
import quickstart


################################################################################
"""                           Application Route(s)                           """
################################################################################

@quickstart.app.route('/', methods=['GET', 'POST'])
def welcome():
    """Application route for welcome."""

    context = {}
    context['view'] = 'welcome'
    template = flask.render_template('quickstart.html', **context)

    return template
