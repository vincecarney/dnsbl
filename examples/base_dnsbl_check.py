import gevent
from dnsbl import Base
from providers import BASE_PROVIDERS

def dnsbl_check(ip, timeout=2):
    jobs = [Base(ip, p).check() for p in BASE_PROVIDERS]
    gevent.joinall(jobs, timeout)
    return [job.value for job in jobs]