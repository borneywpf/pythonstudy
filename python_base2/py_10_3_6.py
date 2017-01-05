#!/usr/bin/env python
# -*- coding:utf-8 -*-


values = range(1, 11) + 'J Q K'.split()
suits = 'Dianonds clubs hearts spades'.split()
deck = ['%s of %s' % (v, s) for v in values for s in suits]

from pprint import pprint as p

p(deck)

from random import shuffle as sh

sh(deck)

p(deck)


print '-' * 30

while deck:
    raw_input(deck.pop())