#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pair import Pair
from pair import make_pair


if __name__ == "__main__":
    print("=== Демонстрация класса Pair с перегрузкой операторов ===")
    
    print("1. Создание объектов:")
    pair1 = Pair(3, 5)
    pair2 = Pair(2, 44)
    pair3 = make_pair(7, 8)
    
    print(f"pair1 = {pair1}")  # использует __str__
    print(f"pair2 = {pair2}")
    print(f"pair3 = {pair3}")
    print(f"repr(pair1) = {repr(pair1)}")  # использует __repr__
    
    print("\n2. Перегрузка оператора умножения *:")
    result1 = pair1 * 3  # использует __mul__
    print(f"{pair1} * 3 = {result1}")
    
    result2 = 2 * pair2  # использует __rmul__
    print(f"2 * {pair2} = {result2}")
    
    result3 = pair3 * 0
    print(f"{pair3} * 0 = {result3}")
    
    result4 = pair1 * -2
    print(f"{pair1} * -2 = {result4}")
    
    print("\n3. Перегрузка оператора сравнения ==:")
    pair4 = Pair(3, 5)
    pair5 = Pair(3, 5)
    pair6 = Pair(2, 44)
    
    print(f"{pair1} == {pair4} : {pair1 == pair4}")
    print(f"{pair1} == {pair6} : {pair1 == pair6}")
    print(f"{pair1} == 'строка' : {pair1 == 'строка'}")
    
    print("\n4. Перегрузка float():")
    float_val = float(pair1)
    print(f"float({pair1}) = {float_val}")
    print(f"Тип: {type(float_val)}")
    
    print("\n5. Комбинированные операции:")
    chain_result = pair1 * 2 * 3
    print(f"({pair1} * 2 * 3) = {chain_result}")
    
    print("\n6. Ввод с клавиатуры и операции:")
    pair_input = Pair()
    pair_input.read()
    print(f"Введенное число: {pair_input}")
    
    try:
        multiplier = int(input("Введите целое число для умножения: "))
        result = pair_input * multiplier
        print(f"Результат: {pair_input} * {multiplier} = {result}")
    except ValueError:
        print("Ошибка: введите целое число")
        exit(1)
    except TypeError as e:
        print(f"Ошибка: {e}")
        exit(1)
    
    print("\n7. Демонстрация всех возможностей:")
    test_pairs = [
        Pair(1, 5),
        Pair(0, 25),
        Pair(10, 99),
        Pair(5, 0)
    ]
    
    multipliers = [1, 2, -1, 0, 10]
    
    for pair in test_pairs:
        for mult in multipliers:
            result = pair * mult
            print(f"{pair:>6} * {mult:>2} = {result}")
        print()
    
    print("=== Завершение демонстрации ===")
