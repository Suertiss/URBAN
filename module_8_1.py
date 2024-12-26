def add_everything_up(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        result = a + b
        return f"{result:g}"
    return str(a) + str(b)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

