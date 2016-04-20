taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0
start "" "c:\FreeCAD\bin\freecad" export_conn_jst_xh.py all
:: FreeCAD export_conn_jst_xh.py all
