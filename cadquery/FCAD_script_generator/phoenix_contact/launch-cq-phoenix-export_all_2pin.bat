taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0
start /b "" "C:\Program Files\FreeCAD 0.15\bin\freecad" export_conn_phoenix.py filter=*01x02*
