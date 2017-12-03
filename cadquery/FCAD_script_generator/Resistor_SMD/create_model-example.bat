taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0
start "" "c:\FreeCAD\bin\freecad" main_generator.py R_01005_0402Metric
:: start "" "D:\FreeCAD_016_6712\bin\freecad" main_generator.py R_01005_0402Metric
:: start "" "d:\FreeCAD_015\bin\freecad" main_generator.py %1

::pause