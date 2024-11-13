# 1. Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Проверка вызовов функции с разным количеством аргументов
print_params()                  # Используются значения по умолчанию
print_params(b=25)              # Переопределение значения b
print_params(c=[1, 2, 3])       # Переопределение значения c
print_params(10, "новая строка") # Переопределение a и b

# 2. Распаковка параметров
# Создаем список и словарь для передачи в функцию
values_list = [100, 'пример', False]
values_dict = {'a': 200, 'b': 'тест', 'c': [4, 5, 6]}

# Передача списка и словаря в функцию с распаковкой
print_params(*values_list)      # Распаковка списка с помощью *
print_params(**values_dict)     # Распаковка словаря с помощью **

# 3. Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']

# Передача двух элементов из списка и добавление третьего параметра
print_params(*values_list_2, 42)

