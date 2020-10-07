import pytest


class Test_add_and_multiplicate:
    def test_int_addition(self):
        assert 0 + 3 == 3 and -1 + 3 == 2

    def test_int_multiplication(self):
        assert 2 * 3 == 6 and 0 * 1 == 0 and 1 * 3 == 3


@pytest.mark.parametrize('equation, result', [('3/1', 3),
                                              ('6/2', 3),
                                              ('-5/-2', 2.5)
                                              ])
def test_int_division(equation, result):
    assert eval(equation) == result


def test_int_sign_change():
    assert (-1)*(-1) == 1


def test_int_zerodivisionerror():
    with pytest.raises(ZeroDivisionError):
        assert 1/0
