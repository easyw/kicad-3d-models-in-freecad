taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0
"d:\FreeCAD_015\bin\freecad" main_generator.py allSOIC
"d:\FreeCAD_015\bin\freecad" main_generator.py allSSOP
"d:\FreeCAD_015\bin\freecad" main_generator.py allTSSOP
"d:\FreeCAD_015\bin\freecad" main_generator.py allSOT
"d:\FreeCAD_015\bin\freecad" main_generator.py allQFP
::pause