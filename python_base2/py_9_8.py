#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
八皇后问题
"""


def conflict(state, nextX):
    print "conflict:nextX =", nextX, " state =", state
    '''
    :param state: 前面的皇后状态位置
    :param nextX: 下一个皇后的水平位置(x坐标或列)
    :return:
    '''
    nextY = len(state)  # 表示垂直位置
    for i in range(nextY):
        """
        如果下一个皇后和正在考虑的前一个皇后的水平距离为0(列相同)或者等于垂直距离(在一条对角线上)就返回True,否则返回False
        """
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False


def queens(num, state):
    if len(state) == num - 1:
        for pos in range(num):
            if not conflict(state, pos):
                yield pos


def queens_new(num, state = ()):
    print '-' * 30
    print "num =", num, "state =", state
    for pos in range(num):
        con = conflict(state, pos)
        print "con =", con
        if not con:
            if len(state) == num - 1:
                z = (pos,)
                print "z =", z
                yield z
            else:
                for result in queens_new(num, state + (pos,)):
                    y = (pos,) + result
                    print "y =", y
                    yield y


if __name__ == "__main__":
    #print list(queens(4, (1, 3, 0)))
    #print list(queens_new(3))
    print list(queens_new(4))
    #print list(queens_new(8))
