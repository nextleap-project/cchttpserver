# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:expandtab

from __future__ import unicode_literals, print_function


class DummyStore:
    def __init__(self):
        self._data = {}

    def set_as(self, owner, key, value):
        self._data[key] = value

    def get(self, key, default=None):
        return self._data.get(key, default)

    def writer(self, owner):
        return DummyStoreWriter(self, owner)

class DummyStoreWriter:
    def __init__(self, store, owner):
        self._store = store
        self._owner = owner

    def set(self, key, value):
        self._store.set_as(self._owner, key, value)
