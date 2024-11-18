def calculate_structure_sum(data):
    total = 0
    
    if isinstance(data, (int, float)):  # Если элемент число, добавляем его к сумме
        return data
    
    elif isinstance(data, str):  # Если строка, добавляем её длину
        return len(data)
    
    elif isinstance(data, (list, tuple, set)):  # Если список, кортеж или множество, рекурсивно обходим элементы
        return sum(calculate_structure_sum(item) for item in data)
    
    elif isinstance(data, dict):  # Если словарь, обходим как ключи, так и значения
        return sum(calculate_structure_sum(k) + calculate_structure_sum(v) for k, v in data.items())
    
    return total  # Для остальных типов данных (например, пустые структуры) возвращаем 0

# Тестовая структура
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# Вызываем функцию и выводим результат
result = calculate_structure_sum(data_structure)
print(result)
