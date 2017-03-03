taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0
start "" "c:\FreeCAD_015\bin\freecad" make_pinheaders_export_fc.py 254single 1

::pause