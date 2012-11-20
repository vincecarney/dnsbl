import gevent
from gevent import socket
from gevent.pool import Pool

class Base(object):
    """A simple DNSBL backend."""

    def __init__(self, ip=None, provider=None, pool_size=None):
        self.ip = ip
        self.provider = provider
        self.pool = Pool(size=pool_size)

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
        return self.pool.apply(self.query)