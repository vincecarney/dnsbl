DNSBL
=====

Simple backend to query DNS-based Blackhole Lists.

Backends should handle hundreds of providers in seconds, thanks to [Gevent](http://www.gevent.org/).

Usage
-----
Check out the examples folder...


    def dnsbl_check(ip):
        backend = Base(ip=ip, providers=BASE_PROVIDERS)
        return backend.check()