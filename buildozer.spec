
[app]
title = EchoPot
package.name = echopot
package.domain = org.wodzianovsky.echopot
source.dir = .
source.include_exts = py,png
version = 1.0
requirements = python3,kivy,requests,beautifulsoup4
icon.filename = icon.png
orientation = portrait
entrypoint = main.py
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
