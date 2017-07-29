taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0
start "" "d:\FreeCAD_015\bin\freecad" main_generator.py all

:: start "" "d:\FreeCAD_015\bin\freecad" main_generator.py 254single 1-10
:: start "" "d:\FreeCAD_015\bin\freecad" main_generator.py 254dual 1-10
:: start "" "d:\FreeCAD_015\bin\freecad" main_generator.py 200single 1-10
:: start "" "d:\FreeCAD_015\bin\freecad" main_generator.py 200dual 1-10
:: start "" "d:\FreeCAD_015\bin\freecad" main_generator.py 127single 1-10
:: start "" "d:\FreeCAD_015\bin\freecad" main_generator.py 127dual 1-10
::pause

:: start "" "d:\FreeCAD_015\bin\freecad" main_generator.py %1

::pause