        print(f'Некорректный тип данных для подсчёта суммы - {item}')
    
    return result, incorrect_data

def calculate_average(numbers):
    """
    Вычисляет среднее арифметическое чисел в коллекции.
    
    Args:
        numbers: Коллекция для подсчета среднего
        
    Returns:
        float: Среднее арифметическое или None при ошибке
    """
    try:
        # Пытаемся получить сумму чисел и количество некорректных данных
        total_sum, incorrect_count = personal_sum(numbers)
        
        # Получаем общее количество элементов и вычитаем некорректные
        valid_count = len(numbers) - incorrect_count
        
        # Вычисляем среднее
        if valid_count > 0:
            return total_sum / valid_count
        else:
            return 0
            
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    except ZeroDivisionError:
        return 0

# Тестирование функций
if __name__ == "__main__":
    print(f'Результат 1: {calculate_average("1, 2, 3")}')
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
    print(f'Результат 3: {calculate_average(567)}')
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')


