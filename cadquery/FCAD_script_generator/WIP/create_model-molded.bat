taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0
start "" "c:\FreeCAD\bin\freecad" main_generator_molded.py DFN-6-1EP_2x2mm_Pitch0.5mm
::QFN-12-1EP_3x3mm_Pitch0.5mm
:: QFN-20-1EP_3x4mm_Pitch0.5mm
::QFN-12-1EP_3x3mm_Pitch0.5mm
:: start "" "d:\FreeCAD_015\bin\freecad" main_generator.py %1

::pause