import os

from download import _get
import helpers

def get(url, cachedir = '.', load = True, downloader = _get, sleep = helpers._randomsleep):
    'Download a web file, or load the version from disk.'
    local_file, local_dir = helpers._paths(cachedir, url)

    # mkdir -p
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

    # Download
    if not os.path.exists(local_file):
       with open(local_file, 'wb') as fp:
           fp.write(_get(url))
       sleep()

    if load:
        return open(local_file).read()
