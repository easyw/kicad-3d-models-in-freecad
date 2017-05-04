taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0
:: start "" "d:\FreeCAD_015\bin\freecad" main_generator.py SOIC-8_3.9x4.9mm_Pitch1.27mm
start "" "d:\FreeCAD_015\bin\freecad" main_generator.py %1

::pause