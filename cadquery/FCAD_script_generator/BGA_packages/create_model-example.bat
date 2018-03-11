taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0
start "" "c:\FreeCAD\bin\freecad" main_generator.py BGA-48_6x8_8.0x9.0mm_Pitch0.8mm
:: start "" "d:\FreeCAD_015\bin\freecad" main_generator.py %1

::pause