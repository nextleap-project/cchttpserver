# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:expandtab

from __future__ import unicode_literals, print_function


class DummyStore:
    def __init__(self):
        self._data = {}

    def set(self, key, value):
        self._data[key] = value

    def get(self, key):
        return self._data[key]
