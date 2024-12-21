import os
import time

# Указываем каталог для обхода
directory = "."

# Используем os.walk для обхода всех файлов и подкаталогов внутри указанного каталога
for root, dirs, files in os.walk(directory):
    # Проверка наличия файлов в текущей директории
    if files:
        # Обрабатываем каждый файл отдельно
        for file in files:
            # Формируем полный путь к файлу
            filepath = os.path.join(root, file)
            
            # Получаем время последнего изменения файла
            filetime = os.path.getmtime(filepath)
            
            # Преобразуем время в удобный формат
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            
            # Получаем размер файла
            filesize = os.path.getsize(filepath)
            
            # Получаем родительскую директорию файла
            parent_dir = os.path.dirname(filepath)
            
            # Выводим информацию о файле
            print(f"Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}")
    else:
        # Если файлов нет, прерываем обход
        break

