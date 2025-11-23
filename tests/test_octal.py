from octal_package.octal import Octal

def test_octal_creation():
    """Тест создания объектов Octal"""
    oct1 = Octal(42)
    assert oct1.to_string() == "52"
    
    oct2 = Octal("52")
    assert oct2.to_int() == 42

def test_octal_indexing():
    """Тест операции индексирования"""
    oct1 = Octal("123")
    assert oct1[0] == 3
    assert oct1[1] == 2

def test_octal_arithmetic():
    """Тест арифметических операций"""
    a = Octal("12")
    b = Octal("7")
    
    sum_result = a.add(b)
    assert sum_result.to_int() == 17
    
    diff_result = a.subtract(b)
    assert diff_result.to_int() == 3

def test_octal_comparison():
    """Тест операций сравнения"""
    a = Octal("15")
    b = Octal("12")
    
    assert a.greater(b) == True
    assert b.less(a) == True
    assert a.equals(a) == True

def test_octal_size():
    """Тест работы с размерами"""
    oct1 = Octal("777", size=5)
    assert oct1.size == 5
    assert oct1.count == 3