# /usr/bin/env python

"""code list 14-5"""

from SocketServer import ThreadingMixIn, StreamRequestHandler, TCPServer


class Server(ThreadingMixIn, TCPServer):
    pass


class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from', addr

        self.wfile.write('Thank you for connecting')


server = Server(('', 1234), Handler)
server.serve_forever()
