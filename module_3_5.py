def get_multiplied_digits(number):
    # Преобразуем число в строку для доступа к отдельным цифрам
    str_number = str(number)

    # Базовый случай: если длина строки 1, возвращаем это число как результат
    if len(str_number) == 1:
        return int(str_number)

    # Рекурсивный случай: извлекаем первую цифру и умножаем на результат рекурсивного вызова
    first = int(str_number[0])
    return first * get_multiplied_digits(int(str_number[1:]))

# Пример использования функции
result = get_multiplied_digits(40203)
print(result)
