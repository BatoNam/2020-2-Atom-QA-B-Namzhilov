import pytest


class TestSet:
    def test_set_uniq(self):
        doubled_list = [i for i in range(3)]*2
        assert len(set(doubled_list)) == len(doubled_list)/2

    @pytest.mark.parametrize('symbol', ['a', 'b', 'c'])
    def test_set_value_check(self, symbol):
        set_example = set('abc')
        assert symbol in set_example


def test_set_add():
    set_example = set('abc')
    len_before = len(set_example)
    set_example.add('d')
    assert len(set_example) == len_before + 1


def test_set_discard():
    set_example = set('abc')
    len_before = len(set_example)
    set_example.discard('c')
    assert len(set_example) == len_before - 1


def test_set_not_iterable():
    with pytest.raises(TypeError):
        assert set('abc')[0]
