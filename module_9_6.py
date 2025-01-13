# Пользовательское исключение
class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        """
        Инициализация итератора.
        
        Args:
            start: Начальное значение
            stop: Конечное значение
            step: Шаг итерации (по умолчанию 1)
            
        Raises:
            StepValueError: Если шаг равен 0
        """
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
            
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        
    def __iter__(self):
        """Сброс указателя и возврат итератора."""
        self.pointer = self.start
        return self
        
    def __next__(self):
        """
        Получение следующего значения.
        
        Returns:
            int: Следующее значение в последовательности
            
        Raises:
            StopIteration: Когда достигнут конец последовательности
        """
        current = self.pointer
        
        # Проверка условия окончания итерации
        if self.step > 0 and current > self.stop:
            raise StopIteration
        if self.step < 0 and current < self.stop:
            raise StopIteration
            
        self.pointer += self.step
        return current

# Тестирование
if __name__ == "__main__":
    # Тест 1: Проверка на неверный шаг
    print("Тест 1: Проверка на шаг = 0")
    try:
        iter1 = Iterator(100, 200, 0)
        for i in iter1:
            print(i, end=' ')
    except StepValueError:
        print('Шаг указан неверно')

    # Тест 2: Положительный шаг
    print("\nТест 2: От -5 до 1 с шагом 1")
    iter2 = Iterator(-5, 1)
    for i in iter2:
        print(i, end=' ')

    # Тест 3: Положительный шаг, больше 1
    print("\nТест 3: От 6 до 15 с шагом 2")
    iter3 = Iterator(6, 15, 2)
    for i in iter3:
        print(i, end=' ')

    # Тест 4: Отрицательный шаг
    print("\nТест 4: От 5 до 1 с шагом -1")
    iter4 = Iterator(5, 1, -1)
    for i in iter4:
        print(i, end=' ')

    # Тест 5: Попытка итерации в неверном направлении
    print("\nТест 5: От 10 до 1 с шагом 1")
    iter5 = Iterator(10, 1)
    for i in iter5:
        print(i, end=' ')
