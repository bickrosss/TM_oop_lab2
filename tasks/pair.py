#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import gcd as gsd


class Pair:
    def __init__(self, first=0, second=0):
        if not isinstance(first, (int, float)):
            print("Ошибка: first должно быть числом")
            exit(1)
        if not isinstance(second, int) or second < 0:
            print("Ошибка: second должно быть положительным целым числом")
            exit(1)
        
        self.first = int(first)
        self.second = int(second)

    def read(self):
        try:
            self.first = int(input("Введите целую часть числа: "))
            second_input = int(input("Введите дробную часть числа: "))
            if second_input < 0:
                print("Ошибка: дробная часть должна быть положительной")
                exit(1)
            self.second = second_input
        except ValueError:
            print("Ошибка: введите целые числа")
            exit(1)

    def display(self):
        print(f"Число: {self.first}.{self.second}")

    def __mul__(self, other):
        """Перегрузка оператора * """
        if not isinstance(other, int):
            raise TypeError("Множитель должен быть целым числом")
            
        full_number = float(f"{self.first}.{self.second}")
        result_number = full_number * other
        result_str = str(result_number)
        parts = result_str.split('.')
        new_first = int(parts[0])
        new_second = int(parts[1]) if len(parts) > 1 else 0
        return Pair(new_first, new_second)

    def __rmul__(self, other):
        """Перегрузка оператора * (справа)"""
        return self.__mul__(other)

    def __str__(self):
        """Перегрузка str()"""
        return f"{self.first}.{self.second}"

    def __repr__(self):
        """Перегрузка repr()"""
        return f"Pair({self.first}, {self.second})"

    def __eq__(self, other):
        """Перегрузка оператора =="""
        if not isinstance(other, Pair):
            return False
        return self.first == other.first and self.second == other.second

    def __float__(self):
        """Перегрузка float()"""
        return float(f"{self.first}.{self.second}")

    def multiply(self, number):
        return self.__mul__(number)


def make_pair(first, second):
    if not isinstance(first, (int, float)):
        print("Ошибка: first должно быть числом")
        exit(1)
    if not isinstance(second, int) or second < 0:
        print("Ошибка: second должно быть положительным целым числом")
        exit(1)
    
    return Pair(first, second)
