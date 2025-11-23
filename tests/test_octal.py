from octal import Octal

def test_octal_creation():
    """Тест создания объектов Octal"""
    oct1 = Octal(42)
    assert oct1.to_string() == "52"  # 42 в десятичной = 52 в восьмеричной
    
    oct2 = Octal("52")
    assert oct2.to_int() == 42
    
    oct3 = Octal("0o63")
    assert oct3.to_int() == 51

def test_octal_indexing():
    """Тест операции индексирования"""
    oct1 = Octal("123")
    assert oct1[0] == 3  # младший разряд
    assert oct1[1] == 2
    assert oct1[2] == 1  # старший разряд
    
    # Тест изменения через индексацию
    oct1[0] = 5
    assert oct1.to_string() == "125"

def test_octal_arithmetic():
    """Тест арифметических операций"""
    a = Octal("12")  # 10 в десятичной
    b = Octal("7")   # 7 в десятичной
    
    sum_result = a.add(b)
    assert sum_result.to_int() == 17
    
    diff_result = a.subtract(b)
    assert diff_result.to_int() == 3
    
    mul_result = a.multiply(b)
    assert mul_result.to_int() == 70

def test_octal_comparison():
    """Тест операций сравнения"""
    a = Octal("15")  # 13 в десятичной
    b = Octal("12")  # 10 в десятичной
    
    assert a.greater(b) == True
    assert b.less(a) == True
    assert a.equals(a) == True

def test_octal_size():
    """Тест работы с размерами"""
    oct1 = Octal("777", size=5)
    assert oct1.size == 5
    assert oct1.count == 3

if __name__ == "__main__":
    test_octal_creation()
    test_octal_indexing()
    test_octal_arithmetic()
    test_octal_comparison()
    test_octal_size()
    print("Все тесты пройдены!")
