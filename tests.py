import tempfile, os
import shutil

from get import get

def test_download():
    downloader = lambda _:bytes('abcde')
    cachedir = tempfile.mkdtemp()
    sleep = lambda:None
    url = 'http://foo.bar/baz'

    returned = get(url, cachedir = cachedir, downloader = downloader,
                   sleep = sleep, load = True)
    assert returned == downloader(None)

    with open(os.path.join(cachedir, 'foo.bar', 'baz'), 'rb') as fp:
        read = fp.read()
    assert read == downloader(None)
    shutil.rmtree(cachedir)
