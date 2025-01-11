from random import choice

# 1. Lambda-функция для сравнения букв
first = 'Мама мыла раму'
second = 'Рамена мало было'

# Lambda-функция сравнивает символы на одинаковых позициях
result = list(map(lambda x, y: x == y, first, second))

# 2. Замыкание для записи в файл
def get_advanced_writer(file_name):
    """
    Создает функцию для записи данных в указанный файл.
    
    Args:
        file_name (str): Имя файла для записи
    
    Returns:
        function: Функция для записи данных
    """
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for data in data_set:
                file.write(str(data) + '\n')
    return write_everything

# 3. Класс с методом __call__
class MysticBall:
    """
    Класс, который случайным образом выбирает слова из заданного набора.
    """
    def __init__(self, *words):
        """
        Инициализирует объект со списком слов.
        
        Args:
            *words: Произвольное количество слов
        """
        self.words = list(words)
    
    def __call__(self):
        """
        Выбирает случайное слово из списка.
        
        Returns:
            str: Случайно выбранное слово
        """
        return choice(self.words)

# Тестирование кода
if __name__ == "__main__":
    # Тест lambda-функции
    print("Результат сравнения строк:")
    print(result)
    
    # Тест замыкания
    write = get_advanced_writer('example.txt')
    write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
    
    # Тест класса MysticBall
    print("\nТест MysticBall:")
    first_ball = MysticBall('Да', 'Нет', 'Наверное')
    print(first_ball())
    print(first_ball())
    print(first_ball())
