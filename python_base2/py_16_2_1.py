#!/usr/bin/env python

"""code my_path.py"""


def square(x):
    '''
    Squares a number and returns the result

    >>> square(2)
    4
    >>> square(3)
    9

    :param x:
    :return:
    '''

    return x ** 2


if __name__ == "__main__":
    import doctest, py_16_2_1
    '''run as python py_16_2_1.py -v'''
    doctest.testmod(py_16_2_1)
