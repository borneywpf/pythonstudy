#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[31m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def pat():
    emphasis_pattern = r'\*([^\*]+)\*'

    m = re.match(emphasis_pattern, '*world*')

    print m.group(0)

    m = re.match('\s*~+', '   ~~~~~~~~~~~~  ')
    print bcolors.OKBLUE + m.group(0) + bcolors.ENDC

    print re.sub(emphasis_pattern, r'<em>\1<\em>', 'Hello, *world*')

    """贪婪的"""
    e = r'\*(.+)\*'
    print re.sub(e, r'<em>\1<\em>', '*This* is *it*')

    """非贪婪的,加?"""
    ex = r'\*\*(.+?)\*\*'
    print re.sub(ex, r'<em>\1<\em>', '**This** is **it**')


if __name__ == "__main__":
    pat()
