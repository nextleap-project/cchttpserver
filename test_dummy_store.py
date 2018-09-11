# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:expandtab

from __future__ import unicode_literals, print_function

import pytest
from dummy_store import DummyStore


class TestDummyStore:
    @pytest.fixture
    def ds(self):
        return DummyStore()


    def test_set_and_get(self, ds):
        a = ds.writer('a')
        b = ds.writer('b')
        a.set('a', b'asdf')
        b.set('b', b'bsdf')
        assert ds.get('a') == b'asdf'
        assert ds.get('b') == b'bsdf'
        assert ds.get('c') == None
        assert ds.get('c', 'default') == 'default'
