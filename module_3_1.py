# Создаем глобальную переменную для подсчета вызовов функций
calls = 0

# Функция для увеличения счётчика вызовов
def count_calls():
    global calls
    calls += 1

# Функция, возвращающая информацию о строке
def string_info(string):
    count_calls()  # Увеличиваем счётчик вызовов
    return (len(string), string.upper(), string.lower())

# Функция, проверяющая наличие строки в списке
def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счётчик вызовов
    string = string.lower()
    list_to_search = [item.lower() for item in list_to_search]
    return string in list_to_search

# Примеры вызова функций
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # True, Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))    # False, No matches

# Выводим количество вызовов функций
print(calls)
