#!/usr/bin/env python
# -*- coding:utf-8 -*-

# database.py

import os, shelve


def store_person(db):
    """
    Query user for data and store it in the shelf object
    :param db: shelf object by open file
    :return:
    """

    pid = raw_input("Enter unique ID number:")
    person = {}
    person['name'] = raw_input('Enter name:')
    person['age'] = raw_input('Enter age:')
    person['phone'] = raw_input('Enter phone:')

    db[pid] = person


def loopup_person(db):
    """
    Query user for id and desired field, and fetch the corresponding data from the shelf object
    :param db:
    :return:
    """

    pid = raw_input('Enter ID number:')
    field = raw_input('What would you like to know?(name, age, phone):')
    field = field.strip().lower()

    print field.capitalize() + ':', db[pid][field]


def print_help():
    print 'The available commands are:'
    print 'store  :  Stores information about person'
    print 'lookup :  Looks up a person from ID number'
    print 'quit   :  Save changes and exit'
    print '?      :  Prints this message'


def enter_command():
    cmd = raw_input('Enter command (? and help):')
    cmd = cmd.strip().lower()
    return cmd


def main():
    print os.getcwd()
    database = shelve.open(os.getcwd() +'/database.db')
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                loopup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()


if __name__ == '__main__':
    main()
