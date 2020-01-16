#!/usr/bin/env python

################################################################################
"""                       Developer(s): Riley Conrardy                       """
################################################################################

import quickstart


################################################################################
"""                         Run SocketIO Application                         """
################################################################################

if __name__ == '__main__':
    quickstart.socketio.run(
        quickstart.app,
        host='0.0.0.0',
        port='8000',
        debug='True'
    )
