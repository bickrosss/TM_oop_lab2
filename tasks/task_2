from octal import Octal

def main():
    print("=== Задание 3: Класс Octal для работы с восьмеричными числами ===")
    print()
    
    # 1. Демонстрация создания объектов
    print("1. Создание объектов Octal:")
    print()
    
    # Из целого числа
    oct1 = Octal(42)
    print("Octal(42) = ", end="")
    oct1.display()
    
    # Из строки
    oct2 = Octal("52")
    print("Octal('52') = ", end="")
    oct2.display()
    
    # Из строки с префиксом
    oct3 = Octal("0o63")
    print("Octal('0o63') = ", end="")
    oct3.display()
    
    # С указанием размера
    oct4 = Octal("777", size=5)
    print("Octal('777', size=5) = ", end="")
    oct4.display()
    print()
    
    # 2. Демонстрация операции индексирования
    print("2. Операция индексирования []:")
    print()
    
    test_oct = Octal("1234")  # 1234 в восьмеричной = 668 в десятичной
    print("test_oct = Octal('1234')")
    print(f"test_oct[0] = {test_oct[0]} (единицы)")
    print(f"test_oct[1] = {test_oct[1]} (восьмерки)") 
    print(f"test_oct[2] = {test_oct[2]} (64-ки)")
    print(f"test_oct[3] = {test_oct[3]} (512-ки)")
    print()
    
    # Изменение через индексирование
    print("Изменение через индексирование:")
    mod_oct = Octal("100")
    print(f"До: mod_oct = {mod_oct}")
    mod_oct[0] = 5
    print(f"После mod_oct[0] = 5: mod_oct = {mod_oct}")
    print()
    
    # 3. Демонстрация полей size и count
    print("3. Поля size и count:")
    print()
    
    size_demo = Octal("12345", size=8)
    print("Octal('12345', size=8):")
    print(f"  size = {size_demo.size} (максимальный размер)")
    print(f"  count = {size_demo.count} (текущее количество цифр)")
    print(f"  MAX_SIZE = {Octal.MAX_SIZE} (глобальная константа)")
    print()
    
    # 4. Демонстрация арифметических операций
    print("4. Арифметические операции:")
    print()
    
    a = Octal("12")  # 10 в десятичной
    b = Octal("7")   # 7 в десятичной
    
    print(f"a = {a} (десятичное: {a.to_int()})")
    print(f"b = {b} (десятичное: {b.to_int()})")
    print()
    
    # Сложение
    sum_result = a.add(b)
    print(f"a + b = {sum_result} (десятичное: {sum_result.to_int()})")
    
    # Вычитание
    diff_result = a.subtract(b)
    print(f"a - b = {diff_result} (десятичное: {diff_result.to_int()})")
    
    # Умножение
    mul_result = a.multiply(b)
    print(f"a * b = {mul_result} (десятичное: {mul_result.to_int()})")
    
    # Деление
    div_result = a.divide(b)
    print(f"a / b = {div_result} (десятичное: {div_result.to_int()})")
    print()
    
    # 5. Демонстрация операций сравнения
    print("5. Операции сравнения:")
    print()
    
    x = Octal("15")  # 13 в десятичной
    y = Octal("12")  # 10 в десятичной
    
    print(f"x = {x} (десятичное: {x.to_int()})")
    print(f"y = {y} (десятичное: {y.to_int()})")
    print()
    
    print(f"x == y: {x.equals(y)}")
    print(f"x > y: {x.greater(y)}")
    print(f"x < y: {x.less(y)}")
    print(f"x == x: {x.equals(x)}")
    print()
    
    # 6. Демонстрация ввода с клавиатуры
    print("6. Ввод с клавиатуры:")
    print()
    
    try:
        user_oct = Octal(size=10)
        print("Введите восьмеричное число (только цифры 0-7):")
        user_oct.read()
        print("Введенное число: ", end="")
        user_oct.display()
        print(f"В десятичной системе: {user_oct.to_int()}")
    except Exception as e:
        print(f"Ошибка ввода: {e}")
    print()
    
    # 7. Демонстрация преобразований
    print("7. Преобразования:")
    print()
    
    demo_oct = Octal(255)  # 255 в десятичной = 377 в восьмеричной
    print(f"Octal(255):")
    print(f"  to_string() = '{demo_oct.to_string()}'")
    print(f"  to_int() = {demo_oct.to_int()}")
    print(f"  str(octal) = '{str(demo_oct)}'")
    print()
    
    # 8. Демонстрация обработки ошибок
    print("8. Обработка ошибок:")
    print()
    
    try:
        # Попытка создать Octal с невосьмеричными цифрами
        bad_oct = Octal("89")
    except ValueError as e:
        print(f"Octal('89') -> ValueError: {e}")
    
    try:
        # Попытка выйти за границы индекса
        test = Octal("123")
        value = test[10]
    except IndexError as e:
        print(f"test[10] -> IndexError: {e}")
    
    try:
        # Попытка присвоить невосьмеричную цифру
        test = Octal("123")
        test[0] = 8
    except ValueError as e:
        print(f"test[0] = 8 -> ValueError: {e}")
    print()
    
    print("=== Демонстрация завершена ===")

if __name__ == "__main__":
    main()
