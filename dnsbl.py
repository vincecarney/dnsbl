import gevent
from gevent import socket

class Base(object):
    """A simple DNSBL backend."""

    def __init__(self, ip=None, provider=None):
        self.ip = ip
        self.provider = provider

    def build_query(self):
        reverse = '.'.join(reversed(self.ip.split('.')))
        return '{reverse}.{provider}.'.format(reverse=reverse, provider=self.provider)

    def query(self):
        try:
            result = socket.gethostbyname(self.build_query())
        except socket.gaierror:
            result = False
        return self.provider, result

    def check(self):
        return gevent.spawn(self.query)