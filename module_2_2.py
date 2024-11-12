# Получаем три числа от пользователя и записываем их в переменные first, second и third
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

# Проверяем условия для вывода количества одинаковых чисел
if first == second == third:
    print(3)  # Все числа равны
elif first == second or first == third or second == third:
    print(2)  # Только два из трех чисел равны
else:
    print(0)  # Все числа различны
