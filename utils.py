__author__ = 'hlp'

import sys

def get_level_input():
    try:
        return float(sys.argv[1])
    except IndexError:
        return 2

def get_const_input():
    try:
        return complex(float(sys.argv[2]), float(sys.argv[3]))
    except IndexError:
        return 0

