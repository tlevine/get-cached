#!/usr/bin/env python
import os
import re
from time import sleep
from random import normalvariate

try:
    import requests
except ImportError:
    try:
        from urllib.request import urlopen
    except ImportError:
        from urllib2 import urlopen
    def _get(url):
        return urlopen(url).read()
else:
    def _get(url):
        return requests.get(url).content

def _randomsleep(mean = 8, sd = 4):
    "Sleep for a random amount of time"
    seconds=normalvariate(mean, sd)
    if seconds>0:
        sleep(seconds)

def get(url, cachedir = '.', load = True, downloader = _get):
    'Download a web file, or load the version from disk.'
    tmp1 = re.sub(r'^https?://', '', url)
    tmp2 = [cachedir] + list(filter(None, tmp1.split('/')))
    local_file = os.path.join(*tmp2)
    local_dir = os.path.join(*tmp2[:-1])
    del(tmp1)
    del(tmp2)

    # mkdir -p
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

    # Download
    if not os.path.exists(local_file):
       print('Downloading and saving %s' % url)
       with open(local_file, 'wb') as fp:
           fp.write(_get(url))
       _randomsleep(1, 0.5)

    if load:
        return open(local_file).read()
