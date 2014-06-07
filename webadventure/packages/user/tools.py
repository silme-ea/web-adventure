import hashlib
import random


# Hashes and stuff
def get_hexdigest(salt, raw_password):
    return hashlib.sha1((salt + raw_password).encode('utf-8')).hexdigest()


def encrypt_password(raw_password):
    salt = get_hexdigest(str(random.random()),
                         str(random.random()))[:5]
    hsh = get_hexdigest(salt, raw_password)
    return 'sha1$%s$%s' % (salt, hsh)


def verify_password(user, raw_password):
    if '$' not in user.password:
        return False

    _, salt, hsh = user.password.split('$')
    return hsh == get_hexdigest(salt, raw_password)
