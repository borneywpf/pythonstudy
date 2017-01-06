#!/usr/bin/evn python

def process(line):
    print "Process:", line


with open('somescript.txt') as f:
    for line in f:
        process(line)

for line in open('somescript.txt'):
    process(line)
