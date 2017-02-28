taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0

start "" "d:\FreeCAD_015\bin\freecad" make_radial_cap_export_fc.py all 
:: start "" "d:\FreeCAD_015\bin\freecad" make_radial_cap_export_fc.py L10_D5
