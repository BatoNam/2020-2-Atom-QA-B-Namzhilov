import pytest
import random


class TestEqualMultiple:
    """
    Есть два ответа умножения списка на что-либо:
    - Положительный, умножение на положительное число
    - Вывод ошибки, умножение на остальные типы данных
    В данном тесте я руководствовался тем, что для
    техники эквивалентных классов для каждого ответа достаточно одного
    экземпляра. (Насколько это применимо в данном случае?)
    """
    def test_multiple_int(self):
        list_example = [1, 2, 's']
        assert type(list_example*random.randint(-1, 1)).__name__ == 'list'

    def test_multiple_not_int(self):
        list_example = [1, 2, 's']
        with pytest.raises(TypeError):
            assert list_example*1.5


def test_list_concatenation():
    list_1 = [1, 2]
    list_2 = ['s', [1, 2]]
    assert list_1 + list_2 == [1, 2, 's', [1, 2]]


@pytest.mark.parametrize('i', [0, 1, 2, -1])
def test_list_index(i):
    list_example = [0, 1, 2, -1]
    assert list_example[i] == i


def test_list_sort():
    list_example = [random.randint(1, 100) for i in range(3)]
    list_example.sort()
    assert all(list_example[i] <= list_example[i+1] for i in range(2))
