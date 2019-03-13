taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0
:: start "" "d:\FreeCAD_015\bin\freecad" main_generator.py 0402
::start "" "c:\FreeCAD-daily\bin\freecad" main_generator.py L_Wuerth_MAPI-1610 
start "" "c:\FreeCAD\bin\freecad" main_generator.py L_Wuerth_MAPI-1610 
::start "" "c:\FreeCAD\bin\freecad" main_generator.py %1

::pause
