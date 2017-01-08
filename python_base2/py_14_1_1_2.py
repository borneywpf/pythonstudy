#!/usr/bin/env python

"""code list 14-2"""

import socket


s = socket.socket()

host = socket.gethostname()
port = 1234

s.connect((host, port))
print s.recv(1024)
