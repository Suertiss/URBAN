import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)
        
    def get_all_words(self):
        all_words = {}
        
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()  # Приводим к нижнему регистру
                    text = text.translate(str.maketrans('', '', string.punctuation.replace("'", "")))  # Удаляем знаки препинания, кроме апострофа
                    words = [word for word in text.split() if word]  # Разделяем текст на слова
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []  # Если файл не найден, возвращаем пустой список
                
        return all_words
        
    def find(self, word):
        word = word.lower()
        results = {}
        
        for name, words in self.get_all_words().items():
            try:
                position = words.index(word) + 1  # Позиция слова (начиная с 1)
                results[name] = position
            except ValueError:
                results[name] = None  # Если слово не найдено
                
        return results
        
    def count(self, word):
        word = word.lower()
        results = {}
        
        for name, words in self.get_all_words().items():
            results[name] = words.count(word)  # Подсчитываем количество вхождений
                
        return results


# Тестирование
if __name__ == "__main__":
    # Создаем тестовый файл
    test_content = """It's a text for task Найти везде,
Используйте его для самопроверки.
Успехов в решении задачи!
text text text"""

    with open('test_file.txt', 'w', encoding='utf-8') as f:
        f.write(test_content)

    # Создаем экземпляр класса
    finder = WordsFinder('test_file.txt')
    
    # Ожидаемый формат вывода:
    print(finder.get_all_words())  # Все слова
    print(finder.find('text'))     # Позиция слова "text"
    print(finder.count('text'))    # Количество вхождений слова "text"
