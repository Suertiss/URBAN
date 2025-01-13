def all_variants(text):
    """
    Генератор всех возможных подпоследовательностей строки.
    
    Args:
        text (str): Исходная строка
        
    Yields:
        str: Подпоследовательности строки в порядке увеличения длины
    """
    # Длина входной строки
    length = len(text)
    
    # Генерируем подстроки длиной 1
    for i in range(length):
        yield text[i]
    
    # Генерируем подстроки длиной от 2 до length
    for sub_len in range(2, length + 1):
        for start in range(length - sub_len + 1):
            yield text[start:start + sub_len]

# Тестирование генератора
if __name__ == "__main__":
    # Тест 1: базовый пример из задания
    print("Тест 1: строка 'abc'")
    a = all_variants("abc")
    for i in a:
        print(i)
        
    # Тест 2: более длинная строка
    print("\nТест 2: строка 'test'")
    b = all_variants("test")
    for i in b:
        print(i)
        
    # Тест 3: строка из одного символа
    print("\nТест 3: строка 'x'")
    c = all_variants("x")
    for i in c:
        print(i)
