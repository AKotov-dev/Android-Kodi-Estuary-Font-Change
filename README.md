# Android-Kodi-Estuary-Font-Change

Это скрипты для изменения [размера](https://github.com/AKotov-dev/Android-Kodi-Estuary-Font-Change/raw/refs/heads/main/skin.estuary_font_color.tar.gz) и [цвета](https://github.com/AKotov-dev/Android-Kodi-Estuary-Font-Change/raw/refs/heads/main/skin.estuary_font_color.tar.gz) шрифтов Kodi (skin.estuary) для Android-TV-Box. В моём случае при подключении приставки [x96q-pro1](https://slimboxtv.ru/x96q/) к телевизору шрифты были слишком мелкие, а регулировка размера шрифтов в самом Kodi, разумеется, отсутствует. В результате пришлось делать это...

Для работы требуется рутированный tv-box и хотя бы 1 раз запущенный Kodi, поскольку нужные для редактирования файлы появляются именно после первого запуска Kodi.

Файлы в skin.estuary_font_size.tar.gz
--
`Font_orig.xml` - оригинальный файл настройки шрифтов (взят из Kodi-21.2)  
`Font.xml` - измененный файл настройки шрифтов для замены на tv-box  
`Restore_Font.xml.sh` - скрипт, переcoздаёт ./Font.xml из оригинального ./Font_orig.xml  

**Вариант изменения-1 (избирательный, рекомендуется)**  
`size+10%.py` - скрипт, избирательное увеличение размера шрифтов + 10% (фильмы, серии, заголовки)  
`size-10%.py` - скрипт, избирательное уменьшение размера шрифтов - 10% (фильмы, серии, заголовки)  

**Вариант изменения-2 (общий)**  
`size_all+10%.py` - скрипт, общее увеличение размера шрифтов + 10%  
`size_all-10%.py` - скрипт, общее уменьшение размера шрифтов - 10%  

`send_to_tv-box.sh` - скрипт, отправляет изменённый ./Font.xml на tv-box

Как изменить размер шрифта
--
1. Подключиться к tv-box, например через [ADBManager](https://github.com/AKotov-dev/adbmanager)
2. Запустить `Restore_Font.xml.sh` чтобы начать с дефолтного `Font.xml`
3. Для увеличения на 20% нажать 2 раза `size+10%.py` (или `size_all+10%.py`, если увеличиваем всё)
4. Запустить `send_to_tv-box.sh` и тем самым отправить изменённый ./Font.xml на tv-box
5. Перезапустить Kodi и посмотреть результат

![](https://github.com/AKotov-dev/Android-Kodi-Estuary-Font-Change/blob/main/screenshots/screenshot1.png)
![](https://github.com/AKotov-dev/Android-Kodi-Estuary-Font-Change/blob/main/screenshots/screenshot2.png)

Как изменить цвет шрифта
--
В моём случае при подключении приставки [x96q-pro1](https://slimboxtv.ru/x96q/) к телевизору белый текст был слишком ярким, а регулировка цвета шрифта в самом Kodi, разумеется, отсутствует. Чтобы не надевать сварочную маску для просмотра любимых фильмов через Kodi было сделано следующее...

Файлы в архиве skin.estuary_font_color.tar.gz
--
`Defaults_orig.xml` - оригинальный файл настройки цвета (взят из Kodi-21.2)
`Defaults.xml` - измененный файл настройки цвета для замены на tv-box
`Restore_Defaults.xml.sh` - скрипт, переcoздаёт ./Defaults.xml из оригинального ./Defaults_orig.xml
`change_color.py` - скрипт, изменение цвета (silver) текста (фильмы, серии, заголовки)
`send_to_tv-box.sh` - скрипт, отправляет изменённый ./Font.xml на tv-box

Как изменить цвет текста
--
1. Подключиться к tv-box, например через [ADBManager](https://github.com/AKotov-dev/adbmanager)
2. Запустить `Restore_Defaults.xml.sh` чтобы начать с дефолтного `Defaults.xml`
3. Для изменения цвета запустить `change_color.py` (по умолчанию цвет silver)
4. Запустить `send_to_tv-box.sh` и тем самым отправить изменённый ./Defaults.xml на tv-box
5. Перезапустить Kodi и посмотреть результат
