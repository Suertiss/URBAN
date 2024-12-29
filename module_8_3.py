class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, vin_number, car_numbers):
        # Проверка VIN номера
        if not self.__is_valid_vin(vin_number):
            raise IncorrectVinNumber(
                'Некорректный тип vin номер' if not isinstance(vin_number, int) else 'Неверный диапазон для vin номера'
            )
        self.__vin = vin_number

        # Проверка регистрационного номера
        if not self.__is_valid_numbers(car_numbers):
            raise IncorrectCarNumbers(
                'Некорректный тип данных для номеров' if not isinstance(car_numbers, str) else 'Неверная длина номера'
            )
        self.__numbers = car_numbers

        self.model = model

    @staticmethod
    def __is_valid_vin(vin_number):
        return isinstance(vin_number, int) and 1000000 <= vin_number <= 9999999

    @staticmethod
    def __is_valid_numbers(numbers):
        return isinstance(numbers, str) and len(numbers) == 6

# Пример использования
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f"{first.model} успешно создан")

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f"{second.model} успешно создан")

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f"{third.model} успешно создан")
