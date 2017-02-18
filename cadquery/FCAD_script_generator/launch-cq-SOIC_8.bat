taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0
start "" "D:\FreeCAD_015\bin\freecad" make_gw_export_fc.py SOIC_8

::pause