from dnsbl import Base
from providers import BASE_PROVIDERS

def dnsbl_check(ip):
    backend = Base(ip=ip, providers=BASE_PROVIDERS)
    return backend.check()