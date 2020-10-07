import pytest
import random


@pytest.fixture
def random_str():
    random_string = ''.join([chr(random.randint(1, 11141)) for j in range(10)])
    return random_string


class TestStrExceptions:
    def test_str_assignment(self, random_str):
        try:
            random_str[1] = 'a'
        except Exception as exception:
            assert type(exception).__name__ == 'TypeError'

    def test_str_multiple_str(self, random_str):
        with pytest.raises(TypeError):
            assert random_str * 'abcvhb'


@pytest.mark.parametrize('multiple, result', [(1, True),
                                              (0, False),
                                              (-1, False)
                                              ])
def test_str_multiple(random_str, multiple, result):
    assert (len(random_str * multiple) > 0) == result


def test_str_concatenation(random_str):
    assert 'ab' + 'cd' + '' == 'abcd'


@pytest.mark.parametrize('i', list(range(3)))
def test_str_index(i):
    str_example = '012'
    assert str_example[i] == str(i)
