class House:
    houses_history = []  # Атрибут класса для хранения истории зданий

    def __new__(cls, *args, **kwargs):
        # Добавляем название здания в историю
        if args:  # Проверяем, есть ли позиционные аргументы
            cls.houses_history.append(args[0])  # args[0] - название здания
        return super().__new__(cls)  # Создаём объект с помощью базового метода __new__

    def __init__(self, name, floors):
        self.name = name  # Название здания
        self.floors = floors  # Количество этажей

    def __del__(self):
        # Вывод сообщения при удалении объекта
        print(f"{self.name} снесён, но он останется в истории")

# Создание объектов класса
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

# Проверяем историю после удаления объектов
print(House.houses_history)
