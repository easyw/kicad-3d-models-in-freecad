taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0
start "" "c:\FreeCAD\bin\freecad" make_radial_smd_export_fc.py CP_Elec_8x10
:: F_D80_L100

::pause