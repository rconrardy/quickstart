################################################################################
"""                       Developer(s): Riley Conrardy                       """
################################################################################

import bcrypt
import hashlib
import itsdangerous
import flask
import flask_login
import quickstart


################################################################################
"""                             Helper Functions                             """
################################################################################

def encode_bcrypt(unhashed):
    """Encode some input using bcrypt."""

    encoded_unhashed = unhashed.encode('utf-8')
    salt =  bcrypt.gensalt()
    hashed = bcrypt.hashpw(encoded_unhashed, salt)
    decoded_hashed = hashed.decode('utf-8')

    return decoded_hashed


def check_bcrypt(unhashed, hashed):
    """Compare a unhashed value to a hashed value using bcrypt."""

    encoded_unhashed = unhashed.encode('utf-8')
    encoded_hashed = hashed.encode('utf-8')
    is_match = bcrypt.checkpw(encoded_unhashed, encoded_hashed)

    return is_match


def encode_sha512(unhashed, algorithm, salt):
    """Encode some input using sha512."""

    salted_unhashed = salt + unhashed
    hashed_object = hashlib.new(algorithm)
    encoded_salted_unhashed = salted_unhashed.encode('utf-8')
    hashed_object.update(encoded_salted_unhashed)
    decoded_hashed = hashed_object.hexdigest()

    return decoded_hashed


def encode_file_sha256(unhashed_filename):
    """Encode some file using sha256."""

    file_content = open(unhashed_filename, 'rb').read()
    hashed_object = hashlib.sha256(file_content)
    decoded_hashed = hashed_object.hexdigest()

    return decoded_hashed
