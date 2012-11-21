import gevent
from gevent import socket

class Base(object):
    """A simple DNSBL backend."""

    def __init__(self, ip=None, providers=[], timeout=2):
        self.ip = ip
        self.providers = providers
        self.timeout = timeout

    def build_query(self, provider):
        reverse = '.'.join(reversed(self.ip.split('.')))
        return '{reverse}.{provider}.'.format(reverse=reverse, provider=provider)

    def query(self, provider):
        try:
            result = socket.gethostbyname(self.build_query(provider))
        except socket.gaierror:
            result = False
        return provider, result

    def check(self):
        results = []
        jobs = [gevent.spawn(self.query, provider) for provider in self.providers]
        gevent.joinall(jobs, self.timeout)
        for job in jobs:
            if job.successful():
                results.append(job.value)
            else:
                results.append((job.args[0], None))
        return results