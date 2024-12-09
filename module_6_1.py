print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

# Демонстрация работы классов
def main():
    # Создание объектов
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    # Проверка имен объектов
    print(a1.name)
    print(p1.name)

    # Проверка начальных состояний
    print(a1.alive)
    print(a2.fed)

    # Попытки поедания
    a1.eat(p1)
    a2.eat(p2)

    # Проверка состояний после поедания
    print(a1.alive)
    print(a2.fed)

if __name__ == "__main__":
    main()

