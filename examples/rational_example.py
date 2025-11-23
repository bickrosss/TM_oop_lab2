#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Rational:
    def __init__(self, a: int = 0, b: int = 1) -> None:
        a = int(a)
        b = int(b)

        if b == 0:
            raise ValueError("Denominator cannot be zero")

        self.__numerator = abs(a)
        self.__denominator = abs(b)

        self.__reduce()

    def __reduce(self) -> None:
        def gcd(a: int, b: int) -> int:
            if a == 0:
                return b
            elif b == 0:
                return a
            elif a >= b:
                return gcd(a % b, b)
            else:
                return gcd(a, b % a)

        sign = 1
        if (self.__numerator > 0 and self.__denominator < 0) or (
            self.__numerator < 0 and self.__denominator > 0
        ):
            sign = -1
        a, b = abs(self.__numerator), abs(self.__denominator)
        c = gcd(a, b)

        self.__numerator = sign * (a // c)
        self.__denominator = b // c

    def __clone(self) -> "Rational":
        return Rational(self.__numerator, self.__denominator)

    @property
    def numerator(self) -> int:
        return self.__numerator

    @numerator.setter
    def numerator(self, value: int) -> None:
        self.__numerator = int(value)
        self.__reduce()

    @property
    def denominator(self) -> int:
        return self.__denominator

    @denominator.setter
    def denominator(self, value: int) -> None:
        value = int(value)
        if value == 0:
            raise ValueError("Denominator cannot be zero")
        self.__denominator = value
        self.__reduce()

    def __str__(self) -> str:
        return f"{self.__numerator}/{self.__denominator}"

    def __repr__(self) -> str:
        return self.__str__()

    def __float__(self) -> float:
        return self.__numerator / self.__denominator

    def __bool__(self) -> bool:
        return self.__numerator != 0

    def __iadd__(self, rhs: "Rational") -> "Rational":
        if isinstance(rhs, Rational):
            a = self.numerator * rhs.denominator + self.denominator * rhs.numerator
            b = self.denominator * rhs.denominator

            self.__numerator, self.__denominator = a, b
            self.__reduce()
            return self
        else:
            raise ValueError("Illegal type of  the argument")

    def __add__(self, rhs: "Rational") -> "Rational":
        return self.__clone().__iadd__(rhs)

    def __isub__(self, rhs: "Rational") -> "Rational":
        if isinstance(rhs, Rational):
            a = self.numerator * rhs.denominator - self.denominator * rhs.numerator
            b = self.denominator * rhs.denominator

            self.__numerator, self.__denominator = a, b
            self.__reduce()
            return self
        else:
            raise ValueError("Illegal type of  the argument")

    def __sub__(self, rhs: "Rational") -> "Rational":
        return self.__clone().__isub__(rhs)

    def __imul__(self, rhs: "Rational") -> "Rational":
        if isinstance(rhs, Rational):
            a = self.numerator * rhs.numerator
            b = self.denominator * rhs.denominator
            self.__numerator, self.__denominator = a, b
            self.__reduce()
            return self
        else:
            raise ValueError("Illegal type of  the argument")

    def __mul__(self, rhs: "Rational") -> "Rational":
        return self.__clone().__imul__(rhs)

    def __itruediv__(self, rhs: "Rational") -> "Rational":
        if isinstance(rhs, Rational):
            a = self.numerator * rhs.numerator
            b = self.denominator * rhs.denominator

            if b == 0:
                raise ValueError("Illegal type of  the argument")

            self.__numerator, self.__denominator = a, b
            self.__reduce()
            return self
        else:
            raise ValueError("Illegal type of  the argument")

    def __truediv__(self, rhs: "Rational") -> "Rational":
        return self.__clone().__itruediv__(rhs)

    def __eq__(self, rhs: "Rational") -> bool:
        if isinstance(rhs, Rational):
            return (
                self.numerator == rhs.numerator and self.denominator == rhs.denominator
            )
        return False

    def __ne__(self, rhs: "Rational") -> bool:
        if isinstance(rhs, Rational):
            return not self.__eq__(rhs)
        return False

    def __gt__(self, rhs: "Rational") -> bool:
        if isinstance(rhs, Rational):
            return self.__float__() > rhs.__float__()
        return False

    def __lt__(self, rhs: "Rational") -> bool:
        if isinstance(rhs, Rational):
            return self.__float__() < rhs.__float__()
        return False

    def __ge__(self, rhs: "Rational") -> bool:
        if isinstance(rhs, Rational):
            return not self.__lt__(rhs)
        return False

    def __le__(self, rhs: "Rational") -> bool:
        if isinstance(rhs, Rational):
            return not self.__gt__(rhs)
        return False


if __name__ == "__main__":

    r1 = Rational(3, 4)
    print(f"Первая дробь r1={r1}:\n", end="")

    r2 = Rational(5, 6)
    print(f"Вторая дробь r2={r2}: ", end="")

    print(f"Сложение: r1 + r2 = {r1+r2}\n", end="")

    print(f"Вычитание: r1 - r2 = {r1-r2}\n", end="")

    print(f"Умножение: r1 * r2 = {r1*r2}\n", end="")

    print(f"Деление: r1 / r2 = {r1/r2}", end="")

    print(f"Равенство: r1 == r2 = {r1==r2}")

    print(f"Неравенство: r1 != r2 = {r1!=r2}")

    print(f"Больше: r1 > r2 = {r1>r2}")

    print(f"Меньше: r1 < r2 = {r1<r2}")

    print(f"Больше или равно: r1 >= r2 = {r1>=r2}")

    print(f"Меньше или равно: r1 <= r2 = {r1<=r2}")
