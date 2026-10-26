def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def safe_divide(a, b):
    if b == 0:
        return 'Ошибка: деление на ноль'
    return a / b
