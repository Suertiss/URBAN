def is_prime(func):
    def wrapper(*args, **kwargs):
        # Получаем результат декорируемой функции
        result = func(*args, **kwargs)
        
        # Проверяем, является ли число простым
        if result < 2:
            print("Составное")
        else:
            is_prime = True
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    is_prime = False
                    break
            print("Простое" if is_prime else "Составное")
            
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    """
    Функция для сложения трех чисел
    """
    return a + b + c

# Примеры использования
if __name__ == "__main__":
    # Пример 1: 2 + 3 + 6 = 11 (простое число)
    print("Тест 1:")
    result = sum_three(2, 3, 6)
    print(result)
    print()
    
    # Пример 2: 1 + 2 + 3 = 6 (составное число)
    print("Тест 2:")
    result = sum_three(1, 2, 3)
    print(result)
    print()
    
    # Пример 3: 3 + 4 + 6 = 13 (простое число)
    print("Тест 3:")
    result = sum_three(3, 4, 6)
    print(result)
    print()
    
    # Пример 4: 2 + 2 + 2 = 6 (составное число)
    print("Тест 4:")
    result = sum_three(2, 2, 2)
    print(result)
