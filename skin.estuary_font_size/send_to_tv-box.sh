#!/bin/bash

clear

# Забрать с android-tv-box
#adb shell su root cp /data/data/org.xbmc.kodi/cache/apk/assets/addons/skin.estuary/xml/Font.xml /sdcard/Font.xml
#adb pull /sdcard/Font.xml Font.xml

# Отправить на android-tv-box
adb push Font.xml /sdcard/Font.xml
adb shell su root cp /sdcard/Font.xml /data/data/org.xbmc.kodi/cache/apk/assets/addons/skin.estuary/xml/Font.xml

read -p "Copy completed. Restart Kodi..."
