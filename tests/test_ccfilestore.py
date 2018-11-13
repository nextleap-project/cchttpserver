# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:expandtab

from __future__ import unicode_literals, print_function

import pytest
from cchttpserver.filestore import CCFileStore


class TestCCFileStore:
    @pytest.fixture
    def ds(self, tmpdir):
        return CCFileStore(tmpdir.strpath)


    def test_set_and_get(self, ds):
        a = ds.writer('a')
        b = ds.writer('b')
        a('a', b'asdf')
        b('b', b'bsdf')
        assert ds.get('a') == b'asdf'
        assert ds.get('b') == b'bsdf'
        assert ds.get('c') == None
        assert ds.get('c') is None

    def test_persistence(self, tmpdir):
        fs = CCFileStore(tmpdir.strpath)
        fs.set_as('user1', 'a', b'a1')
        del fs
        fs = CCFileStore(tmpdir.strpath)
        assert fs.get('a') == b'a1'

    def test_getuserlist(self, ds):
        ds.set_as('user1', 'a1', b'a1')
        ds.set_as('user1', 'a2', b'a2')
        ds.set_as('user2', 'b1', b'b1')
        assert ds.get_user_keys('user1') == ['a1', 'a2']
        assert ds.get_user_keys('user2') == ['b1']

    def test_delete_user(self, ds):
        ds.set_as('user1', 'a1', b'a1')
        ds.set_as('user1', 'a2', b'a2')
        ds.set_as('user2', 'b1', b'b1')
        assert ds.get('a1') == b'a1'
        ds.delete_user('user1')
        assert ds.get('a1') is None
        assert ds.get_user_keys('user1') == []
        ds.delete_user("user1")
        assert ds.get_user_keys('user1') == []
