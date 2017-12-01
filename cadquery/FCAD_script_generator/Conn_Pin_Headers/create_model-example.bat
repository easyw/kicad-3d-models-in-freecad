taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0
start "" "c:\FreeCAD_016\bin\freecad" main_generator.py PinHeader_1xyy_P2.54mm_Vertical
:: start "" "d:\FreeCAD_015\bin\freecad" main_generator.py %1

::pause