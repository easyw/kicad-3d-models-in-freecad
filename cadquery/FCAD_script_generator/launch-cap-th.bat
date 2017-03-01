taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0

start "" "c:\FreeCAD_015\bin\freecad" make_radial_cap_export_fc.py L35_D12_5_p05
::L10_D5_p05
::L11_5_D08_p05 todo filleting with D=8
:: start "" "d:\FreeCAD_015\bin\freecad" make_radial_cap_export_fc.py L10_D5
