__author__ = 'jjauhiainen'


def convert_int(val):
    try:
        return int(val)
    except ValueError:
        raise ValueError("Value needs to be integer, was: {}".format(val))

def convert_bool(val):
    try:
        return bool(val)
    except ValueError:
        raise ValueError("Value needs to be boolean, was: {}".format(val))