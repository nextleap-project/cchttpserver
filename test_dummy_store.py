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
        ds.set('a', 'a', b'asdf')
        ds.set('c', 'c', b'csdf')
        assert ds.get('a') == b'asdf'
        assert ds.get('c') == b'csdf'
        with pytest.raises(KeyError):
            ds.get('b')
