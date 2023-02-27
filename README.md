Usage
-----

* python3 -m venv .venv
* source .venv/bin/activate
* pip install -r requirements.txt
* pytest

Notes
-----

* The real trouble I had was with dealing with the "No such module" errors. Had to put my classes into Thing/ with an \_\_init\_\_.py to make them a module
* I also tried mocking urllib.request.urlopen, but that didn't work for some reason.
* Still - this is definitely working:
  - If you comment the mocker.patch line out, it tries to fetch from the URL and times out
  - If you change the 15 to a 16, the assertion says "nope - wrong number!"
