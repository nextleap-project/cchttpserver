# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:expandtab

from __future__ import unicode_literals, print_function
import os
import functools


class CCFileStore:
    def __init__(self, dbdir):
        self.dbdir = dbdir
        self.blockdir = os.path.join(dbdir, "blocks")
        self.userdir = os.path.join(dbdir, 'users')
        if not os.path.exists(self.blockdir):
            os.makedirs(self.blockdir)
        if not os.path.exists(self.userdir):
            os.mkdir(self.userdir)

    def _get_keypath(self, key):
        assert '\0' not in key, repr(key)
        assert '..' not in key and '*' not in key, repr(key)
        return os.path.join(self.blockdir, key)

    def _get_userlist_path(self, user):
        assert '..' not in user and '*' not in user, repr(user)
        return os.path.join(self.userdir, user)

    def set_as(self, user, key, value):
        fn = self._get_keypath(key)
        user_fn = self._get_userlist_path(user)
        assert not os.path.exists(fn)
        tmp_fn = fn + ".tmp"
        with open(tmp_fn, 'wb') as f:
            f.write(value)
        with open(user_fn, 'a') as f:
            f.write(key + "\n")
        os.rename(tmp_fn, fn)

    def get_user_keys(self, user):
        user_fn = self._get_userlist_path(user)
        try:
            with open(user_fn) as f:
                return f.read().strip().split("\n")
        except IOError:
            return []

    def get(self, key):
        """ Return None or key value. """
        fn = self._get_keypath(key)
        try:
            with open(fn, "rb") as f:
                return f.read()
        except (IOError, OSError):
            return None

    def writer(self, user):
        return functools.partial(self.set_as, user)

    def delete_user(self, user):
        user_fn = self._get_userlist_path(user)
        try:
            for key in open(user_fn):
                key = key.strip()
                if not key:
                    continue
                os.remove(self._get_keypath(key))
        except IOError:
            pass
        else:
            os.remove(user_fn)
