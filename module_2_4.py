numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создаем пустые списки для простых и не простых чисел
primes = []
not_primes = []

# Перебираем числа из списка numbers
for num in numbers:
    # Пропускаем число 1, так как оно не простое и не составное
    if num == 1:
        continue

    # Устанавливаем флаг is_prime в True
    is_prime = True

    # Проверяем, есть ли делители у числа num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break  # Прерываем цикл, если найден делитель

    # Если число простое, добавляем в список primes, иначе в not_primes
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

# Выводим списки primes и not_primes
print("Primes:", primes)
print("Not Primes:", not_primes)
