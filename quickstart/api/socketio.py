################################################################################
"""                       Developer(s): Riley Conrardy                       """
################################################################################

import flask
import quickstart


################################################################################
"""                             Helper Functions                             """
################################################################################

@quickstart.socketio.on('connect')
def on_connect():
    """Socket.io helper function for on_connect."""

    return

@quickstart.socketio.on('join')
def on_join(data):
    """Socket.io helper function for on_join."""

    room = data
    join_room(room)

    return

@quickstart.socketio.on('leave')
def on_leave(data):
    """Socket.io helper function for on_leave."""

    room = data['room']
    leave_room(room)

    return
