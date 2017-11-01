taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0
start "" "C:\Program Files\FreeCAD 0.16\bin" main_generator.py DIP-8_W7.62mm
