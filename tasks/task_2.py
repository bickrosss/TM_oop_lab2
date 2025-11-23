from octal_package.octal import Octal

def main():
    print("1. Создание объектов Octal:")
    print()
    
    oct1 = Octal(42)
    print("Octal(42) = ", end="")
    oct1.display()
    
    oct2 = Octal("52")
    print("Octal('52') = ", end="")
    oct2.display()
    
    oct3 = Octal("0o63")
    print("Octal('0o63') = ", end="")
    oct3.display()
    
    oct4 = Octal("777", size=5)
    print("Octal('777', size=5) = ", end="")
    oct4.display()
    print()
    
    print("2. Операция индексирования []:")
    print()
    
    test_oct = Octal("1234")
    print("test_oct = Octal('1234')")
    print(f"test_oct[0] = {test_oct[0]} (единицы)")
    print(f"test_oct[1] = {test_oct[1]} (восьмерки)") 
    print(f"test_oct[2] = {test_oct[2]} (64-ки)")
    print(f"test_oct[3] = {test_oct[3]} (512-ки)")
    print()
    
    print("Изменение через индексирование:")
    mod_oct = Octal("100")
    print(f"До: mod_oct = {mod_oct}")
    mod_oct[0] = 5
    print(f"После mod_oct[0] = 5: mod_oct = {mod_oct}")
    print()
    
    print("3. Поля size и count:")
    print()
    
    size_demo = Octal("12345", size=8)
    print("Octal('12345', size=8):")
    print(f"  size = {size_demo.size} (максимальный размер)")
    print(f"  count = {size_demo.count} (текущее количество цифр)")
    print(f"  MAX_SIZE = {Octal.MAX_SIZE} (глобальная константа)")
    print()
    
    print("4. Арифметические операции:")
    print()
    
    a = Octal("12")
    b = Octal("7")
    
    print(f"a = {a} (десятичное: {a.to_int()})")
    print(f"b = {b} (десятичное: {b.to_int()})")
    print()
    
    sum_result = a.add(b)
    print(f"a + b = {sum_result} (десятичное: {sum_result.to_int()})")
    
    diff_result = a.subtract(b)
    print(f"a - b = {diff_result} (десятичное: {diff_result.to_int()})")
    
    mul_result = a.multiply(b)
    print(f"a * b = {mul_result} (десятичное: {mul_result.to_int()})")
    
    div_result = a.divide(b)
    print(f"a / b = {div_result} (десятичное: {div_result.to_int()})")
    print()
    
    print("5. Операции сравнения:")
    print()
    
    x = Octal("15")
    y = Octal("12") 
    
    print(f"x = {x} (десятичное: {x.to_int()})")
    print(f"y = {y} (десятичное: {y.to_int()})")
    print()
    
    print(f"x == y: {x.equals(y)}")
    print(f"x > y: {x.greater(y)}")
    print(f"x < y: {x.less(y)}")
    print(f"x == x: {x.equals(x)}")
    print()
    
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
    
    print("7. Преобразования:")
    print()
    
    demo_oct = Octal(255)
    print(f"Octal(255):")
    print(f"  to_string() = '{demo_oct.to_string()}'")
    print(f"  to_int() = {demo_oct.to_int()}")
    print(f"  str(octal) = '{str(demo_oct)}'")
    print()

if __name__ == "__main__":
    main()
