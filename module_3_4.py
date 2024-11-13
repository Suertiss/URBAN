def single_root_words(root_word, *other_words):
    # Приводим root_word к нижнему регистру для корректного сравнения
    root_word = root_word.lower()
    # Создаем пустой список для подходящих слов
    same_words = []
    
    # Перебираем слова в other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()
        
        # Если root_word содержится в слове или слово содержится в root_word, добавляем его в список
        if root_word in word_lower or word_lower in root_word:
            same_words.append(word)
    
    # Возвращаем список подходящих слов
    return same_words

# Примеры вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Вывод результатов на консоль
print(result1)  # Ожидаемый результат: ['richiest', 'orichalcum', 'richies']
print(result2)  # Ожидаемый результат: ['Able', 'Disable']

