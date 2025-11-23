class Octal:
    MAX_SIZE = 100  # максимальный размер списка
    
    def __init__(self, value=0, size=10):
        self.size = min(size, Octal.MAX_SIZE)  # максимальное количество элементов
        self.count = 0  # текущее количество элементов
        self.digits = [0] * self.size  # список цифр
        
        if isinstance(value, str):
            self._init_from_string(value)
        else:
            self._init_from_int(value)
    
    def _init_from_string(self, value_str):
        """Инициализация из строки"""
        # Убираем возможный префикс '0o'
        if value_str.startswith('0o'):
            value_str = value_str[2:]
        
        # Заполняем цифры с конца (младшие разряды сначала)
        self.count = min(len(value_str), self.size)
        for i in range(self.count):
            digit_char = value_str[-(i + 1)]
            digit = int(digit_char)
            if digit < 0 or digit > 7:
                raise ValueError("Восьмеричное число должно содержать цифры 0-7")
            self.digits[i] = digit
    
    def _init_from_int(self, value_int):
        """Инициализация из целого числа"""
        if value_int < 0:
            raise ValueError("Число должно быть беззнаковым")
        
        value = value_int
        self.count = 0
        
        # Преобразуем в восьмеричное представление
        while value > 0 and self.count < self.size:
            self.digits[self.count] = value % 8
            value //= 8
            self.count += 1
        
        # Если число 0
        if self.count == 0:
            self.count = 1
            self.digits[0] = 0
    
    def __getitem__(self, index):
        """Перегрузка операции индексирования []"""
        if index < 0 or index >= self.size:
            raise IndexError("Индекс за пределами списка")
        return self.digits[index]
    
    def __setitem__(self, index, value):
        """Перегрузка операции присваивания по индексу"""
        if index < 0 or index >= self.size:
            raise IndexError("Индекс за пределами списка")
        if value < 0 or value > 7:
            raise ValueError("Восьмеричная цифра должна быть от 0 до 7")
        self.digits[index] = value
        # Обновляем count если нужно
        if index >= self.count and value != 0:
            self.count = index + 1
    
    def to_int(self):
        """Преобразование в целое число"""
        result = 0
        for i in range(self.count):
            result += self.digits[i] * (8 ** i)
        return result
    
    def to_string(self):
        """Преобразование в строку"""
        if self.count == 0:
            return "0"
        result = ""
        for i in range(self.count - 1, -1, -1):
            result += str(self.digits[i])
        return result
    
    def display(self):
        """Вывод на экран"""
        print(f"Octal: {self.to_string()} (size: {self.size}, count: {self.count})")
    
    def read(self):
        """Ввод с клавиатуры"""
        value_str = input("Введите восьмеричное число: ")
        self._init_from_string(value_str)
    
    # Арифметические операции
    def add(self, other):
        """Сложение"""
        result_int = self.to_int() + other.to_int()
        result_size = max(self.size, other.size)
        return Octal(result_int, result_size)
    
    def subtract(self, other):
        """Вычитание"""
        if self < other:
            raise ValueError("Результат не может быть отрицательным")
        result_int = self.to_int() - other.to_int()
        result_size = max(self.size, other.size)
        return Octal(result_int, result_size)
    
    def multiply(self, other):
        """Умножение"""
        result_int = self.to_int() * other.to_int()
        result_size = max(self.size, other.size)
        return Octal(result_int, result_size)
    
    def divide(self, other):
        """Целочисленное деление"""
        if other.to_int() == 0:
            raise ZeroDivisionError("Деление на ноль")
        result_int = self.to_int() // other.to_int()
        result_size = max(self.size, other.size)
        return Octal(result_int, result_size)
    
    # Операции сравнения
    def equals(self, other):
        return self.to_int() == other.to_int()
    
    def greater(self, other):
        return self.to_int() > other.to_int()
    
    def less(self, other):
        return self.to_int() < other.to_int()
    
    def __str__(self):
        return self.to_string()
    
    def __repr__(self):
        return f"Octal('{self.to_string()}', size={self.size})"


# Демонстрация работы
if __name__ == "__main__":
    print("=== Демонстрация класса Octal ===")
    print()
    
    # Создание объектов разными способами
    print("1. Создание объектов:")
    oct1 = Octal(42)  # из целого числа
    oct1.display()
    
    oct2 = Octal("52")  # из строки
    oct2.display()
    
    oct3 = Octal("0o63", size=5)  # из строки с префиксом
    oct3.display()
    print()
    
    # Тестирование индексирования
    print("2. Тестирование индексирования:")
    print(f"oct1[0] = {oct1[0]} (единицы)")
    print(f"oct1[1] = {oct1[1]} (восьмерки)")
    
    # Изменение через индексирование
    oct4 = Octal(10)
    print(f"До изменения: oct4 = {oct4}")
    oct4[0] = 2
    print(f"После oct4[0] = 2: oct4 = {oct4}")
    print()
    
    # Арифметические операции
    print("3. Арифметические операции:")
    a = Octal("12")
    b = Octal("7")
    
    sum_result = a.add(b)
    print(f"{a} + {b} = {sum_result}")
    
    diff_result = a.subtract(b)
    print(f"{a} - {b} = {diff_result}")
    
    mul_result = a.multiply(b)
    print(f"{a} * {b} = {mul_result}")
    
    div_result = a.divide(b)
    print(f"{a} / {b} = {div_result}")
    print()
    
    # Операции сравнения
    print("4. Операции сравнения:")
    x = Octal("15")
    y = Octal("12")
    
    print(f"{x} == {y}: {x.equals(y)}")
    print(f"{x} > {y}: {x.greater(y)}")
    print(f"{x} < {y}: {x.less(y)}")
    print()
    
    # Работа с размером
    print("5. Работа с размером:")
    large = Octal("777", size=5)
    large.display()
    print(f"large.size() = {large.size}")
    print(f"large.count = {large.count}")
    print()
    
    # Ввод с клавиатуры
    print("6. Ввод с клавиатуры:")
    try:
        user_oct = Octal(size=10)
        user_oct.read()
        user_oct.display()
    except Exception as e:
        print(f"Ошибка: {e}")
