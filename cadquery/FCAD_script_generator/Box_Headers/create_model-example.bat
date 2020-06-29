taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0
:: can either use ranges or a list separated by commas
:: start "" "d:\FreeCAD_015\bin\freecad" main_generator.py 2-6
start "" "d:\FreeCAD_015\bin\freecad" main_generator.py 2,6,10


::pause