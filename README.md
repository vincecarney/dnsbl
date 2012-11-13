DNSBL.py
========

Simple backend to query DNS-based Blackhole Lists.

Backends should handle hundreds of providers in seconds, thanks to [Gevent](http://www.gevent.org/).

Usage
-----
Check out examples folder...


    def dnsbl_check(ip, timeout=2):
        jobs = [Base(ip, p).check() for p in BASE_PROVIDERS]
        gevent.joinall(jobs, timeout)
        return [job.value for job in jobs]