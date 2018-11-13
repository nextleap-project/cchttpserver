
0.6.2
-----

- move modules into a package and make "python -m cchttpserver" work.

- introduce environment variable CCHTTPSERVER_CONFIG which needs
  to point to a config file

0.6.1
-----

- restrict keys to be alphanumberic and at least 32 chars long

0.6
---

- renamed blockservice to cchttpserver

- implemented persistent CCFileStorage replacing the Dummy Storage

- added per-user recording of set-operations,
  store.get_user_keys(user), add store.delete_user()
  command which clears out all blocks stored by a user

- add http DELETE /USER/ command to delete all blocks from a user
  remotely (requires that USER to be logged in)
