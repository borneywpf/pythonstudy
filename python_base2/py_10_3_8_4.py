#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re


def pat():
    emphasis_pattern = r'\*([^\*]+)\*'

    m = re.match(emphasis_pattern, '*world*')

    print m.group(0)

    print re.sub(emphasis_pattern, r'<em>\1<\em>', 'Hello, *world*')

    """贪婪的"""
    e = r'\*(.+)\*'
    print re.sub(e, r'<em>\1<\em>', '*This* is *it*')

    """非贪婪的,加?"""
    ex = r'\*\*(.+?)\*\*'
    print re.sub(ex, r'<em>\1<\em>', '**This** is **it**')


if __name__ == "__main__":
    pat()
