taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0
start "" "C:\Program Files\FreeCAD 0.16\bin\FreeCAD.exe" main_generator.py all
