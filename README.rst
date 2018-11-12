claimchain http block server
============================

Simple http-server for "claimchain" blocks.  It uses Flask to serve HTTP GET and authenticated PUT requests.


getting started
---------------

- checkout the repository and edit ``config.py`` to sets users/passwords
  and to set the database directory.

- run ``pip install -e .``

- run ``python cchttpserver.py``

Then open another terminal and open a python prompt with "python" and type something like::

    import requests
    requests.put("http://USER:PASSWORD@localhost:5000/key1", "data1")
    r = requests.get("http://localhost:5000/key1")
    assert r.status_code == 200
    requests.delete("http://USER:PASSWORD@localhost:5000/USER/")
    r = requests.get("http://localhost:5000/key1")
    assert r.status_code == 404


