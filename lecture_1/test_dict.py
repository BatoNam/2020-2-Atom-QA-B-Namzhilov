import pytest
import random


@pytest.fixture(scope='class')
def random_dict():
    dictionary = {}
    for i in range(random.randint(1, 5)):
        key = ''.join([chr(random.randint(1, 1114111)) for j in range(i)])
        dictionary[key] = random.randint(-1000, 1000)
    return dictionary


class TestDictMethods:
    def test_dict_clear(self, random_dict):
        cleared_dict = random_dict.clear()
        assert cleared_dict is None

    def test_dict_copy(self, random_dict):
        copy_of_dict = random_dict.copy()
        assert copy_of_dict == random_dict

    def test_dict_get(self):
        dict_example = {'a': 4}
        assert dict_example.get('a') == 4


@pytest.mark.parametrize('str_num', ['1', '2', '5', '3'])
def test_dict_key_to_value(str_num):
    dict_example = {'1': 1, '3': 3, '2': 2, '5': 5}
    assert dict_example[str_num] == int(str_num)


def test_dict_update():
    dict_example = {'sex': 'male', 'height': 180, 'weight': 80}
    len_before = len(dict_example)
    dict_example.update({'year': 1999})
    assert len(dict_example)-1 == len_before
