def apply_all_func(int_list, *functions):
    """
    Применяет набор функций к списку чисел.
    
    Args:
        int_list: Список чисел
        *functions: Набор функций для применения к списку
        
    Returns:
        dict: Словарь с результатами работы функций
    """
    results = {}
    
    # Применяем каждую функцию к списку
    for func in functions:
        # Получаем имя функции и результат её работы
        results[func.__name__] = func(int_list)
    
    return results

# Тестирование функции
if __name__ == "__main__":
    # Тест 1: использование max и min
    test_list1 = [6, 20, 15, 9]
    print(apply_all_func(test_list1, max, min))
    
    # Тест 2: использование len, sum и sorted
    test_list2 = [6, 20, 15, 9]
    print(apply_all_func(test_list2, len, sum, sorted))
    
    # Дополнительные тесты
    # Тест 3: пустой список функций
    print(apply_all_func([1, 2, 3]))  # -> {}
    
    # Тест 4: список с одним элементом
    print(apply_all_func([42], max, min, len))  # -> {'max': 42, 'min': 42, 'len': 1}
    
    # Тест 5: использование лямбда-функции
    avg = lambda x: sum(x) / len(x)
    print(apply_all_func([1, 2, 3, 4], avg, max, min))  # -> {'<lambda>': 2.5, 'max': 4, 'min': 1}
