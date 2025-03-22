#!/usr/bin/env python

import xml.etree.ElementTree as ET

def modify_selected_font_sizes(file_path, scale_factor, font_names):
    # Загружаем XML файл
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Проходим по всем элементам <font>, которые содержат размер шрифта
    for font in root.iter('font'):
        font_name_element = font.find('name')
        size_element = font.find('size')
        
        # Проверяем, что имя шрифта входит в список выбранных и что есть элемент <size>
        if font_name_element is not None and size_element is not None:
            font_name = font_name_element.text
            if font_name in font_names:
                try:
                    current_size = int(size_element.text)  # Получаем текущий размер шрифта
                    new_size = int(current_size * scale_factor)  # Применяем масштабирование
                    size_element.text = str(new_size)  # Записываем новый размер
                except ValueError:
                    pass  # Если значение размера не является числом, пропускаем

    # Сохраняем изменения в новый файл
    tree.write(file_path)

# Пример использования: увеличение всех выбранных шрифтов на 10%
file_path = 'Font.xml'  # Путь к файлу Font.xml
scale_factor = 1.10  # Коэффициент увеличения (например, 1.10 для увеличения на 10% или 0.90 для уменьшения на 10%)
selected_fonts = ['font10', 'font12', 'font13', 'font14', 'font27', 'font37', 'font_MainMenu']  # Список выбранных шрифтов

modify_selected_font_sizes(file_path, scale_factor, selected_fonts)
print("Шрифты для выбранных секций успешно изменены!")
