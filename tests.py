import tempfile, os
import shutil

from get import get

def test_get():
    downloader = lambda _:bytes('abcde')
    cachedir = tempfile.mkdtemp()
    sleep = lambda:None
    url = 'http://foo.bar/baz'

    observed = get(url, cachedir = cachedir, downloader = downloader,
                   sleep = sleep, load = True)
    assert observed == downloader(None)

    shutil.rmtree(cachedir)

def test_read_cache():
    downloader = lambda _:bytes('abcde')
    cachedir = tempfile.mkdtemp()
    sleep = lambda:None
    url = 'http://foo.bar/baz'
    os.makedirs(os.path.join(cachedir, 'foo.bar'))

    expected = bytes('lalalala')

    with open(os.path.join(cachedir, 'foo.bar', 'baz'), 'wb') as fp:
        fp.write(expected)

    observed = get(url, cachedir = cachedir, downloader = downloader,
                   sleep = sleep, load = True)
    assert observed == expected

    observed2 = get(url, cachedir = cachedir, downloader = downloader,
                    sleep = sleep, load = False)
    assert observed2 == None

    shutil.rmtree(cachedir)

def test_write_cache():
    downloader = lambda _:bytes('abcde')
    cachedir = tempfile.mkdtemp()
    sleep = lambda:None
    url = 'http://foo.bar/baz'
    os.makedirs(os.path.join(cachedir, 'foo.bar'))

    get(url, cachedir = cachedir, downloader = downloader,
        sleep = sleep, load = False)

    with open(os.path.join(cachedir, 'foo.bar', 'baz'), 'rb') as fp:
        read = fp.read()
    assert read == downloader(None)

    shutil.rmtree(cachedir)
