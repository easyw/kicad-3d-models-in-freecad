::taskkill -im freecad.exe /f
@echo OFF
echo cadquery-freecad-module required
@echo ON
cd %~p0

"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py HTQFP-64_1EP_10x10mm_Pitch0.5mm_ThermalPad
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py LQFP-100_14x14mm_Pitch0.5mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py LQFP-128_14x14mm_Pitch0.4mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py LQFP-128_14x20mm_Pitch0.5mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py LQFP-144_20x20mm_Pitch0.5mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py LQFP-160_24x24mm_Pitch0.5mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py LQFP-176_20x20mm_Pitch0.4mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py LQFP-176_24x24mm_Pitch0.5mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py LQFP-208_28x28mm_Pitch0.5mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py LQFP-216_24x24mm_Pitch0.4mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py LQFP-32-1EP_5x5mm_Pitch0.5mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py LQFP-32_5x5mm_Pitch0.5mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py LQFP-32_7x7mm_Pitch0.8mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py LQFP-36_7x7mm_Pitch0.65mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py LQFP-44_10x10mm_Pitch0.8mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py LQFP-48_7x7mm_Pitch0.5mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py LQFP-52-1EP_10x10mm_Pitch0.65mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py LQFP-52_10x10mm_Pitch0.65mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py LQFP-64-1EP_10x10mm_Pitch0.5mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py LQFP-64_10x10mm_Pitch0.5mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py LQFP-64_14x14mm_Pitch0.8mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py LQFP-64_7x7mm_Pitch0.4mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py LQFP-80_12x12mm_Pitch0.5mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py PQFP-100_14x20mm_Pitch0.65mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py PQFP-256_28x28mm_Pitch0.4mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py PQFP-80_14x20mm_Pitch0.8mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py TQFP-100-1EP_14x14mm_Pitch0.5mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py TQFP-100_12x12mm_Pitch0.4mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py TQFP-100_14x14mm_Pitch0.5mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py TQFP-120_14x14mm_Pitch0.4mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py TQFP-128_14x14mm_Pitch0.4mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py TQFP-144_16x16mm_Pitch0.4mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py TQFP-144_20x20mm_Pitch0.5mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py TQFP-32_7x7mm_Pitch0.8mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py TQFP-44-1EP_10x10mm_Pitch0.8mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py TQFP-44_10x10mm_Pitch0.8mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py TQFP-48-1EP_7x7mm_Pitch0.5mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py TQFP-48_7x7mm_Pitch0.5mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py TQFP-64_10x10mm_Pitch0.5mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py TQFP-64_14x14mm_Pitch0.8mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py TQFP-64_1EP_10x10mm_Pitch0.5mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py TQFP-64_7x7mm_Pitch0.4mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py TQFP-80_12x12mm_Pitch0.5mm
"c:\FreeCAD_015\bin\freecad" make_gw_export_fc.py TQFP-80_14x14mm_Pitch0.65mm
