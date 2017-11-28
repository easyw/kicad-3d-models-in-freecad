taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0

start "" "c:\program files\freecad 0.16\bin\freecad.exe" main_generator.py R_Array_SIP

:: pause