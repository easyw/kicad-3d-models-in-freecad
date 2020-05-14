taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0
start "" "c:\FreeCAD\bin\freecad" main_generator.py C_01005_0402Metric
:: start "" "d:\FreeCAD\bin\freecad" main_generator.py %1

::pause
