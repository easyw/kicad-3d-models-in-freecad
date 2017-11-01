taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0

start "" "d:\FreeCAD_015\bin\freecad" main_generator.py R_Bare_Metal_Element_L16.3mm_W4.8mm_P15.30mm

:: pause