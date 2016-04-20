taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0
::start "" "c:\FreeCAD\bin\freecad" make_pinheaders_export_fc.py 254single 1-3
start "" "c:\FreeCAD\bin\freecad" make_pinheaders_export_fc.py all

:: start "" "c:\FreeCAD\bin\freecad" make_pinheaders_export_fc.py 254single 1-10
:: start "" "c:\FreeCAD\bin\freecad" make_pinheaders_export_fc.py 254dual 1-10
:: start "" "c:\FreeCAD\bin\freecad" make_pinheaders_export_fc.py 200single 1-10
:: start "" "c:\FreeCAD\bin\freecad" make_pinheaders_export_fc.py 200dual 1-10
:: start "" "c:\FreeCAD\bin\freecad" make_pinheaders_export_fc.py 127single 1-10
:: start "" "c:\FreeCAD\bin\freecad" make_pinheaders_export_fc.py 127dual 1-10
::pause