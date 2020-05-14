taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0
:: start "" "d:\FreeCAD_015\bin\freecad" main_generator.py 0402
start "" "C:\Program Files\FreeCAD 0.18\bin\freecad" main_generator.py %1

::pause