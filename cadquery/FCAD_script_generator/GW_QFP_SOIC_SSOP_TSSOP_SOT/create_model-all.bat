taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0
"d:\FreeCAD_015\bin\freecad" main_generator.py
::pause
