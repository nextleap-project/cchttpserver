
0.6
---

- renamed blockservice to cchttpserver

- implemented persistent CCFileStorage replacing the Dummy Storage

- added per-user recording of set-operations,
  store.get_user_keys(user), add store.delete_user()
  command which clears out all blocks stored by a user

- add http DELETE /USER/ command to delete all blocks from a user
  remotely (requires that USER to be logged in)
