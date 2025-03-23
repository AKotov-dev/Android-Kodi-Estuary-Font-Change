#!/usr/bin/env python

import xml.etree.ElementTree as ET

# Функция для замены цвета текста в файле
def replace_textcolor(xml_file, new_color):
    # Парсим XML файл
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Ищем все теги <textcolor> и меняем их значение
    for textcolor in root.findall(".//textcolor"):
        textcolor.text = new_color

    # Записываем изменённый XML обратно в тот же файл
    tree.write(xml_file, encoding="UTF-8", xml_declaration=True)

# Задаём путь к файлу и новый цвет
xml_file = 'Defaults.xml'  # Имя вашего файла
new_color = 'silver'  # Новый цвет

# Выполняем замену
replace_textcolor(xml_file, new_color)
print(f"Все цвета текста в файле {xml_file} заменены на {new_color}.")
