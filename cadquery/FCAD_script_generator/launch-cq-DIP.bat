taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0
start "" "c:\FreeCAD_015\bin\freecad" make_dip_export_fc.py DIP-8_W7.62mm
:: DIP-22_W10.16mm 
:: DIP-24_W10.16mm 
:: DIP-4_W10.16mm
:: DIP-24_W10.16mm 
:: DIP-4_W10.16mm
:: DIP-64_W15.24mm
:: DIP-24_W15.24mm
:: DIP-24_W15.24mm
:: DIP-8_W7.62mm

::pause