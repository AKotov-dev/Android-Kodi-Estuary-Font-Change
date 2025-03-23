#!/bin/bash

clear

# Забрать с android-tv-box
#adb shell su root cp /data/data/org.xbmc.kodi/cache/apk/assets/addons/skin.estuary/xml/Defaults.xml /sdcard/Defaults.xml
#adb pull /sdcard/Defaults.xml Defaults_orig.xml

# Отправить на android-tv-box
adb push Defaults.xml /sdcard/Defaults.xml
adb shell su root cp /sdcard/Defaults.xml /data/data/org.xbmc.kodi/cache/apk/assets/addons/skin.estuary/xml/Defaults.xml

read -p "Copy completed. Restart Kodi..."
