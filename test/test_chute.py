from __future__ import absolute_import
from hellbox.chute import Chute
from mock import Mock


class TestChute(object):

    def test_init(self):
        f = Mock()
        chute = Chute.create(f)()
        assert not f.called
        assert len(chute.callbacks) is 0

    def test_callbacks(self):
        f = Mock()
        chute = Chute.create(f)()
        assert chute.callbacks == []
        chute.callbacks.append('foo')
        assert 'foo' in chute.callbacks

    def test_call(self):
        f = Mock()
        f2 = Mock()
        chute = Chute.create(f)()
        chute.to(Chute.create(f2)())
        chute()
        assert f.called
        assert f2.called

    def test_to(self):
        chute = Chute.create(Mock())()
        cb = Chute.create(Mock())()
        chute.to(cb)
        assert cb in chute.callbacks