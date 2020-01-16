################################################################################
"""                       Developer(s): Riley Conrardy                       """
################################################################################

import re
import flask
import flask_login
import quickstart


################################################################################
"""                             Helper Functions                             """
################################################################################

_VALIDATORS = {}

def validate_input(*args, **kwargs):
    """Ensure that inputs are valid, gathers all returned messages."""

    messages = {}
    for key, value in kwargs.items():
        messages[key] = _VALIDATORS[key](value)

    return messages


################################################################################
"""                      Validator Class with Decorator                      """
################################################################################

class Validator:
    """Base class for all validators, each validator has a name and function."""

    def __init__(self, name, func):
        """Initialize a validator with a name and the function associated."""

        self.name = name
        self.func = func

    def __call__(self, *args):
        """Defines what happens when validator is called."""

        return self.func(*args)


def validator(*names):
    """Decorator for declaring a new validator."""

    def add_validators(func):
        """Create a validator for names that call the function."""

        for name in names:
            lowercase_name = name.lower()
            _VALIDATORS[lowercase_name] = Validator(lowercase_name, func)

        return func

    return add_validators


################################################################################
"""                            Validate Functions                            """
################################################################################

@validator('name', 'first_name', 'last_name')
def validate_name(name):
    """Validate the user entered a 'valid' name."""

    regex = '(?=.{1,})'
    if not re.search(regex, name):
        return False, 'Name is not valid'

    return True, 'Okay'


@validator('email')
def validate_email(email):
    """Validate the user entered a 'valid' email."""

    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if not re.search(regex, email):
        return False, 'Email is not valid.'

    return True, 'Okay'


@validator('password')
def validate_password(password):
    """Validate the user entered a 'valid' password."""

    regex = '(?=.{4,})'
    if not re.search(regex, password):
        return False, 'Password must longer than 4 characters.'

    return True, 'Okay'


@validator('filename')
def validate_filename(filename):
    """Validate the user entered a 'valid' filename."""

    is_extension = '.' in filename
    extension = filename.rsplit('.', 1)[1].lower()
    is_allowed = extension in app.config['ALLOWED_EXTENSIONS']

    if not (is_extension and is_allowed):
        return False, 'Filename is not valid.'

    return True, 'Okay'
