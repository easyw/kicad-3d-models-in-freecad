taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0
start "" "c:\FreeCAD\bin\freecad" DPAK_export.py TO268
::VSSOP-8_2.3x2mm_Pitch0.5mm
::SOIC-8_3.9x4.9mm_Pitch1.27mm
:: start "" "d:\FreeCAD_015\bin\freecad" main_generator.py %1

::pause