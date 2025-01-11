# Исходные списки
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# 1. Генераторная сборка с использованием zip
# Вычисляем разницу длин, если они не равны
first_result = (abs(len(f) - len(s)) 
                for f, s in zip(first, second) 
                if len(f) != len(s))

# 2. Генераторная сборка с использованием range
# Сравниваем длины строк на одинаковых позициях
second_result = (len(first[i]) == len(second[i]) 
                 for i in range(len(first)))

# Вывод результатов
print(list(first_result))
print(list(second_result))
