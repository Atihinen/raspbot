__author__ = 'jjauhiainen'


def convert_int(val):
    try:
        return int(val)
    except ValueError:
        raise "Value needs to be integer, was: {}".format(val)