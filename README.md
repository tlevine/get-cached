This was extracted from [hardhat](https://github.com/tlevine/hardhat).

I used it briefly but now recommend
[requests and vlermv](http://thomaslevine.com/!/web-sites-to-data-tables-in-depth/) instead.

```sh
pip install get-cached
```

Make a get request for a url and cache it,
or load it from a cache if it has already been downloaded.

```python
from get import get
print(get(url))
```

This works in Python 2.7 and Python 3.3.
