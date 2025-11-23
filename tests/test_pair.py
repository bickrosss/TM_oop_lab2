#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from pair import Pair
from pair import make_pair


def test_multiplication_operator():
    pair = Pair(2, 5)
    result = pair * 2
    assert result == Pair(5, 0)


def test_right_multiplication():
    pair = Pair(1, 5)
    result = 3 * pair
    assert result == Pair(4, 5)


def test_multiplication_negative():
    pair = Pair(3, 14)
    result = pair * -1
    assert result == Pair(-3, 14)


def test_multiplication_zero():
    pair = Pair(5, 5)
    result = pair * 0
    assert result == Pair(0, 0)


def test_equality_operator():
    pair1 = Pair(3, 5)
    pair2 = Pair(3, 5)
    pair3 = Pair(2, 5)
    assert pair1 == pair2
    assert not (pair1 == pair3)


def test_float_conversion():
    pair = Pair(3, 14)
    assert float(pair) == 3.14


def test_string_representation():
    pair = Pair(2, 44)
    assert str(pair) == "2.44"


def test_repr_representation():
    pair = Pair(1, 5)
    assert repr(pair) == "Pair(1, 5)"


def test_multiplication_type_error():
    pair = Pair(2, 5)
    with pytest.raises(TypeError):
        pair * "строка"


def test_make_pair_function():
    pair = make_pair(7, 8)
    assert pair == Pair(7, 8)


def test_backward_compatibility():
    pair = Pair(2, 5)
    result_old = pair.multiply(2)
    result_new = pair * 2
    assert result_old == result_new


if __name__ == "__main__":
    test_multiplication_operator()
    test_right_multiplication()
    test_multiplication_negative()
    test_multiplication_zero()
    test_equality_operator()
    test_float_conversion()
    test_string_representation()
    test_repr_representation()
    test_make_pair_function()
    test_backward_compatibility()
    print("Все тесты перегрузки операторов пройдены!")
