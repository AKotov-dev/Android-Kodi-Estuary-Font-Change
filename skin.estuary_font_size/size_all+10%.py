#!/usr/bin/env python

import xml.etree.ElementTree as ET

def modify_font_sizes(file_path, scale_factor):
    # Загружаем XML файл
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Проходим по всем элементам <font>, которые содержат размер шрифта
    for font in root.iter('font'):
        size_element = font.find('size')
        if size_element is not None:
            try:
                current_size = int(size_element.text)  # Получаем текущий размер шрифта
                new_size = int(current_size * scale_factor)  # Применяем масштабирование
                size_element.text = str(new_size)  # Записываем новый размер
            except ValueError:
                pass  # Если значение размера не является числом, пропускаем

    # Сохраняем изменения в новый файл
    tree.write(file_path)

# Пример использования: увеличение всех шрифтов на 10%
file_path = 'Font.xml'  # Путь к файлу Font.xml
scale_factor = 1.10  # Коэффициент увеличения (например, 1.10 для увеличения на 10% или 0.90 для уменьшения на 10%)

modify_font_sizes(file_path, scale_factor)
print("Шрифты успешно изменены!")
