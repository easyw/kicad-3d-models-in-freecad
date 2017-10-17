# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating QFP/GullWings models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Dimensions are based on module library values
# Models are representative

## file of parametric definitions
from collections import namedtuple

destination_dir="/Resistors_THT.3dshapes"

Params = namedtuple("Params", [
    'l',      # length/height of body
    'd',      # diameter/depth of body
    'w',      # width of body
    'pd',     # pin diameter
    'px',     # pin pitch on board (typical)
    'py',     # pin pitch y offset (for box resistors)
    'shape',  # "din", "power", "box", "array"
    'orient'  # 'v' or 'h'
])

kicad_naming_params_resistors_tht = {
    'R_Axial_DIN0204_L3.6mm_D1.6mm_P1.90mm_Vertical': Params(	
        l = 3.6,
        d = 1.6,
        w = 0.0,
        pd = 0.5,
        px = 1.9,
        py = 0.0,
        shape = 'din',
        orient = 'v'
    ),
    'R_Axial_DIN0204_L3.6mm_D1.6mm_P2.54mm_Vertical': Params(	
        l = 3.6,
        d = 1.6,
        w = 0.0,
        pd = 0.5,
        px = 2.54,
        py = 0.0,
        shape = 'din',
        orient = 'v'
    ),
    'R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal': Params(	
        l = 3.6,
        d = 1.6,
        w = 0.0,
        pd = 0.5,
        px = 5.08,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),    
    'R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Vertical': Params(
        l = 3.6,
        d = 1.6,
        w = 0.0,
        pd = 0.5,
        px = 5.08,
        py = 0.0,
        shape = 'din',
        orient = 'v'
    ),
    'R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal': Params(
        l = 3.6,
        d = 1.6,
        w = 0.0,
        pd = 0.5,
        px = 7.62,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),
    'R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal': Params(	
        l = 6.3,
        d = 2.5,
        w = 0.0,
        pd = 0.6,
        px = 10.16,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),
    'R_Axial_DIN0207_L6.3mm_D2.5mm_P15.24mm_Horizontal': Params(	
        l = 6.3,
        d = 2.5,
        w = 0.0,
        pd = 0.6,
        px = 15.24,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),
    'R_Axial_DIN0207_L6.3mm_D2.5mm_P2.54mm_Vertical': Params(	
        l = 6.3,
        d = 2.5,
        w = 0.0,
        pd = 0.6,
        px = 2.54,
        py = 0.0,
        shape = 'din',
        orient = 'v'
    ),
    'R_Axial_DIN0207_L6.3mm_D2.5mm_P5.08mm_Vertical': Params(	
        l = 6.3,
        d = 2.5,
        w = 0.0,
        pd = 0.6,
        px = 5.08,
        py = 0.0,
        shape = 'din',
        orient = 'v'
    ),
    'R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal': Params(	
        l = 6.3,
        d = 2.5,
        w = 0.0,
        pd = 0.6,
        px = 7.62,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),  
    'R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal': Params(	
        l = 9.0,
        d = 3.2,
        w = 0.0,
        pd = 0.7,
        px = 12.70,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),  
    'R_Axial_DIN0309_L9.0mm_D3.2mm_P15.24mm_Horizontal': Params(	
        l = 9.0,
        d = 3.2,
        w = 0.0,
        pd = 0.7,
        px = 15.24,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),      
    'R_Axial_DIN0309_L9.0mm_D3.2mm_P2.54mm_Vertical': Params(	
        l = 9.0,
        d = 3.2,
        w = 0.0,
        pd = 0.7,
        px = 2.54,
        py = 0.0,
        shape = 'din',
        orient = 'v'
    ),  
    'R_Axial_DIN0309_L9.0mm_D3.2mm_P20.32mm_Horizontal': Params(	
        l = 9.0,
        d = 3.2,
        w = 0.0,
        pd = 0.7,
        px = 20.32,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),  
    'R_Axial_DIN0309_L9.0mm_D3.2mm_P25.40mm_Horizontal': Params(	
        l = 9.0,
        d = 3.2,
        w = 0.0,
        pd = 0.7,
        px = 25.40,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),  
    'R_Axial_DIN0309_L9.0mm_D3.2mm_P5.08mm_Horizontal': Params(	
        l = 9.0,
        d = 3.2,
        w = 0.0,
        pd = 0.7,
        px = 5.08,
        py = 0.0,
        shape = 'din',
        orient = 'v'
    ),
    'R_Axial_DIN0309_L9.0mm_D3.2mm_P5.08mm_Vertical': Params(
        l = 9.0,
        d = 3.2,
        w = 0.0,
        pd = 0.7,
        px = 5.08,
        py = 0.0,
        shape = 'din',
        orient = 'v'
    ),
    'R_Axial_DIN0411_L9.9mm_D3.2mm_P5.08mm_Vertical': Params(
        l = 9.9,
        d = 3.2,
        w = 0.0,
        pd = 0.8,
        px = 5.08,
        py = 0.0,
        shape = 'din',
        orient = 'v'
    ),
    'R_Axial_DIN0411_L9.9mm_D3.2mm_P12.70mm_Horizontal': Params(
        l = 9.9,
        d = 3.2,
        w = 0.0,
        pd = 0.8,
        px = 12.70,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),
    'R_Axial_DIN0411_L9.9mm_D3.2mm_P15.24mm_Horizontal': Params(
        l = 9.9,
        d = 3.2,
        w = 0.0,
        pd = 0.8,
        px = 15.24,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),
    'R_Axial_DIN0411_L9.9mm_D3.2mm_P20.32mm_Horizontal': Params(
        l = 9.9,
        d = 3.2,
        w = 0.0,
        pd = 0.8,
        px = 20.32,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),
    'R_Axial_DIN0411_L9.9mm_D3.2mm_P25.40mm_Horizontal': Params(
        l = 9.9,
        d = 3.2,
        w = 0.0,
        pd = 0.8,
        px = 25.40,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),
    'R_Axial_DIN0411_L9.9mm_D3.2mm_P5.08mm_Vertical': Params(
        l = 9.9,
        d = 3.2,
        w = 0.0,
        pd = 0.8,
        px = 5.08,
        py = 0.0,
        shape = 'din',
        orient = 'v'
    ),
    'R_Axial_DIN0411_L9.9mm_D3.2mm_P7.62mm_Vertical': Params(
        l = 9.9,
        d = 3.2,
        w = 0.0,
        pd = 0.8,
        px = 7.62,
        py = 0.0,
        shape = 'din',
        orient = 'v'
    ),
    'R_Axial_DIN0414_L11.9mm_D4.5mm_P15.24mm_Horizontal': Params(
        l = 11.9,
        d = 4.5,
        w = 0.0,
        pd = 0.8,
        px = 15.24,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),    
    'R_Axial_DIN0414_L11.9mm_D4.5mm_P20.32mm_Horizontal': Params(
        l = 11.9,
        d = 4.5,
        w = 0.0,
        pd = 0.8,
        px = 20.32,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),    
    'R_Axial_DIN0414_L11.9mm_D4.5mm_P25.40mm_Horizontal': Params(
        l = 11.9,
        d = 4.5,
        w = 0.0,
        pd = 0.8,
        px = 25.40,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),    
    'R_Axial_DIN0414_L11.9mm_D4.5mm_P5.08mm_Vertical': Params(
        l = 11.9,
        d = 4.5,
        w = 0.0,
        pd = 0.8,
        px = 5.08,
        py = 0.0,
        shape = 'din',
        orient = 'v'
    ),
    'R_Axial_DIN0414_L11.9mm_D4.5mm_P7.62mm_Vertical': Params(
        l = 11.9,
        d = 4.5,
        w = 0.0,
        pd = 0.8,
        px = 7.62,
        py = 0.0,
        shape = 'din',
        orient = 'v'
    ),  
    'R_Axial_DIN0516_L15.5mm_D5.0mm_P20.32mm_Horizontal': Params(
        l = 15.5,
        d = 5.0,
        w = 0.0,
        pd = 0.8,
        px = 20.32,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),
    'R_Axial_DIN0516_L15.5mm_D5.0mm_P25.40mm_Horizontal': Params(
        l = 15.5,
        d = 5.0,
        w = 0.0,
        pd = 0.8,
        px = 25.40,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),
    'R_Axial_DIN0516_L15.5mm_D5.0mm_P30.48mm_Horizontal': Params(
        l = 15.5,
        d = 5.0,
        w = 0.0,
        pd = 0.8,
        px = 30.48,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),    
    'R_Axial_DIN0516_L15.5mm_D5.0mm_P5.08mm_Vertical': Params(
        l = 15.5,
        d = 5.0,
        w = 0.0,
        pd = 0.8,
        px = 5.08,
        py = 0.0,
        shape = 'din',
        orient = 'v'
    ),      
    'R_Axial_DIN0516_L15.5mm_D5.0mm_P7.62mm_Vertical': Params(
        l = 15.5,
        d = 5.0,
        w = 0.0,
        pd = 0.8,
        px = 7.62,
        py = 0.0,
        shape = 'din',
        orient = 'v'
    ),       
    'R_Axial_DIN0614_L14.3mm_D5.7mm_P15.24mm_Horizontal': Params(
        l = 14.3,
        d = 5.7,
        w = 0.0,
        pd = 0.8,
        px = 15.24,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),     
    'R_Axial_DIN0614_L14.3mm_D5.7mm_P20.32mm_Horizontal': Params(
        l = 14.3,
        d = 5.7,
        w = 0.0,
        pd = 0.8,
        px = 20.32,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),         
    'R_Axial_DIN0614_L14.3mm_D5.7mm_P25.40mm_Horizontal': Params(
        l = 14.3,
        d = 5.7,
        w = 0.0,
        pd = 0.8,
        px = 25.40,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),         
    'R_Axial_DIN0614_L14.3mm_D5.7mm_P5.08mm_Vertical': Params(
        l = 14.3,
        d = 5.7,
        w = 0.0,
        pd = 0.8,
        px = 5.08,
        py = 0.0,
        shape = 'din',
        orient = 'v'
    ),         
    'R_Axial_DIN0614_L14.3mm_D5.7mm_P7.62mm_Vertical': Params(
        l = 14.3,
        d = 5.7,
        w = 0.0,
        pd = 0.8,
        px = 7.62,
        py = 0.0,
        shape = 'din',
        orient = 'v'
    ),  
    'R_Axial_DIN0617_L17.0mm_D6.0mm_P20.32mm_Horizontal': Params(
        l = 17.0,
        d = 6.0,
        w = 0.0,
        pd = 0.8,
        px = 20.32,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),      
    'R_Axial_DIN0617_L17.0mm_D6.0mm_P25.40mm_Horizontal': Params(
        l = 17.0,
        d = 6.0,
        w = 0.0,
        pd = 0.8,
        px = 25.40,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),    
    'R_Axial_DIN0617_L17.0mm_D6.0mm_P30.48mm_Horizontal': Params(
        l = 17.0,
        d = 6.0,
        w = 0.0,
        pd = 0.8,
        px = 30.48,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),    
    'R_Axial_DIN0617_L17.0mm_D6.0mm_P5.08mm_Vertical': Params(
        l = 17.0,
        d = 6.0,
        w = 0.0,
        pd = 0.8,
        px = 5.08,
        py = 0.0,
        shape = 'din',
        orient = 'v'
    ),        
    'R_Axial_DIN0617_L17.0mm_D6.0mm_P7.62mm_Vertical': Params(
        l = 17.0,
        d = 6.0,
        w = 0.0,
        pd = 0.8,
        px = 7.62,
        py = 0.0,
        shape = 'din',
        orient = 'v'
    ),      
    'R_Axial_DIN0918_L18.0mm_D9.0mm_P22.86mm_Horizontal': Params(
        l = 18.0,
        d = 9.0,
        w = 0.0,
        pd = 0.8,
        px = 22.86,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),   
    'R_Axial_DIN0918_L18.0mm_D9.0mm_P25.40mm_Horizontal': Params(
        l = 18.0,
        d = 9.0,
        w = 0.0,
        pd = 0.8,
        px = 25.40,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),  
    'R_Axial_DIN0918_L18.0mm_D9.0mm_P30.48mm_Horizontal': Params(
        l = 18.0,
        d = 9.0,
        w = 0.0,
        pd = 0.8,
        px = 30.48,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),  
    'R_Axial_DIN0918_L18.0mm_D9.0mm_P7.62mm_Vertical': Params(
        l = 18.0,
        d = 9.0,
        w = 0.0,
        pd = 0.8,
        px = 7.62,
        py = 0.0,
        shape = 'din',
        orient = 'v'
    ),  
    'R_Axial_DIN0922_L20.0mm_D9.0mm_P25.40mm_Horizontal': Params(
        l = 20.0,
        d = 9.0,
        w = 0.0,
        pd = 0.8,
        px = 25.40,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),
    'R_Axial_DIN0922_L20.0mm_D9.0mm_P30.48mm_Horizontal': Params(
        l = 20.0,
        d = 9.0,
        w = 0.0,
        pd = 0.8,
        px = 30.48,
        py = 0.0,
        shape = 'din',
        orient = 'h'
    ),
    'R_Axial_DIN0922_L20.0mm_D9.0mm_P7.62mm_Vertical': Params(
        l = 20.0,
        d = 9.0,
        w = 0.0,
        pd = 0.8,
        px = 7.62,
        py = 0.0,
        shape = 'din',
        orient = 'v'
    ),    
    'R_Axial_Power_L20.0mm_W6.4mm_P22.40mm': Params(	
        l = 20.0,
        d = 6.4,
        w = 6.4,
        pd = 0.8,
        px = 22.40,
        py = 0.0,
        shape = 'power',
        orient = 'h'
    ),
    'R_Axial_Power_L20.0mm_W6.4mm_P25.40mm': Params(	
        l = 20.0,
        d = 6.4,
        w = 6.4,
        pd = 0.8,
        px = 25.40,
        py = 0.0,
        shape = 'power',
        orient = 'h'
    ),
    'R_Axial_Power_L20.0mm_W6.4mm_P30.48mm': Params(	
        l = 20.0,
        d = 6.4,
        w = 6.4,
        pd = 0.8,
        px = 30.48,
        py = 0.0,
        shape = 'power',
        orient = 'h'
    ),
    'R_Axial_Power_L20.0mm_W6.4mm_P5.08mm_Vertical': Params(	
        l = 20.0,
        d = 6.4,
        w = 6.4,
        pd = 0.8,
        px = 5.08,
        py = 0.0,
        shape = 'power',
        orient = 'v'
    ),    
    'R_Axial_Power_L20.0mm_W6.4mm_P7.62mm_Vertical': Params(	
        l = 20.0,
        d = 6.4,
        w = 6.4,
        pd = 0.8,
        px = 7.62,
        py = 0.0,
        shape = 'power',
        orient = 'v'
    ),        
    'R_Axial_Power_L25.0mm_W6.4mm_P27.94mm': Params(	
        l = 25.0,
        d = 6.4,
        w = 6.4,
        pd = 0.8,
        px = 27.94,
        py = 0.0,
        shape = 'power',
        orient = 'h'
    ),    
    'R_Axial_Power_L25.0mm_W6.4mm_P30.48mm': Params(	
        l = 25.0,
        d = 6.4,
        w = 6.4,
        pd = 0.8,
        px = 30.48,
        py = 0.0,
        shape = 'power',
        orient = 'h'
    ),     
    'R_Axial_Power_L25.0mm_W9.0mm_P10.16mm_Vertical': Params(	
        l = 25.0,
        d = 9.0,
        w = 9.0,
        pd = 0.8,
        px = 10.16,
        py = 0.0,
        shape = 'power',
        orient = 'v'
    ),     
    'R_Axial_Power_L25.0mm_W9.0mm_P27.94mm': Params(	
        l = 25.0,
        d = 9.0,
        w = 9.0,
        pd = 0.8,
        px = 27.94,
        py = 0.0,
        shape = 'power',
        orient = 'h'
    ),   
    'R_Axial_Power_L25.0mm_W9.0mm_P30.48mm': Params(	
        l = 25.0,
        d = 9.0,
        w = 9.0,
        pd = 0.8,
        px = 30.48,
        py = 0.0,
        shape = 'power',
        orient = 'h'
    ), 
    'R_Axial_Power_L25.0mm_W9.0mm_P7.62mm_Vertical': Params(	
        l = 25.0,
        d = 9.0,
        w = 9.0,
        pd = 0.8,
        px = 7.62,
        py = 0.0,
        shape = 'power',
        orient = 'v'
    ),
    'R_Axial_Power_L38.0mm_W6.4mm_P40.64mm': Params(	
        l = 38.0,
        d = 6.4,
        w = 6.4,
        pd = 0.8,
        px = 40.64,
        py = 0.0,
        shape = 'power',
        orient = 'h'
    ),  
    'R_Axial_Power_L38.0mm_W6.4mm_P45.72mm': Params(	
        l = 38.0,
        d = 6.4,
        w = 6.4,
        pd = 0.8,
        px = 45.72,
        py = 0.0,
        shape = 'power',
        orient = 'h'
    ),    
    'R_Axial_Power_L38.0mm_W9.0mm_P40.64mm': Params(	
        l = 38.0,
        d = 9.0,
        w = 9.0,
        pd = 0.8,
        px = 40.64,
        py = 0.0,
        shape = 'power',
        orient = 'h'
    ),    
    'R_Axial_Power_L38.0mm_W9.0mm_P45.72mm': Params(	
        l = 38.0,
        d = 9.0,
        w = 9.0,
        pd = 0.8,
        px = 45.72,
        py = 0.0,
        shape = 'power',
        orient = 'h'
    ),
    'R_Axial_Power_L48.0mm_W12.5mm_P10.16mm_Vertical': Params(	
        l = 48.0,
        d = 12.5,
        w = 12.5,
        pd = 0.8,
        px = 10.16,
        py = 0.0,
        shape = 'power',
        orient = 'v'
    ),        
    'R_Axial_Power_L48.0mm_W12.5mm_P55.88mm': Params(	
        l = 48.0,
        d = 12.5,
        w = 12.5, 
        pd = 0.8,
        px = 55.88,
        py = 0.0,
        shape = 'power',
        orient = 'h'
    ),         
    'R_Axial_Power_L48.0mm_W12.5mm_P60.96mm': Params(	
        l = 48.0,
        d = 12.5,
        w = 12.5, 
        pd = 0.8,
        px = 60.96,
        py = 0.0,
        shape = 'power',
        orient = 'h'
    ),      
    'R_Axial_Power_L48.0mm_W12.5mm_P7.62mm_Vertical': Params(	
        l = 48.0,
        d = 12.5,
        w = 12.5,
        pd = 0.8,
        px = 7.62,
        py = 0.0,
        shape = 'power',
        orient = 'v'
    ),     
    'R_Axial_Power_L50.0mm_W9.0mm_P55.88mm': Params(	
        l = 50.0,
        d = 9.0,
        w = 9.0, 
        pd = 0.8,
        px = 55.88,
        py = 0.0,
        shape = 'power',
        orient = 'h'
    ),     
    'R_Axial_Power_L50.0mm_W9.0mm_P60.96mm': Params(	
        l = 50.0,
        d = 9.0,
        w = 9.0, 
        pd = 0.8,
        px = 60.96,
        py = 0.0,
        shape = 'power',
        orient = 'h'
    ),     
    'R_Axial_Power_L60.0mm_W14.0mm_P10.16mm_Vertical': Params(	
        l = 60.0,
        d = 14.0,
        w = 14.0,
        pd = 0.8,
        px = 10.16,
        py = 0.0,
        shape = 'power',
        orient = 'v'
    ),    
    'R_Axial_Power_L60.0mm_W14.0mm_P60.04mm': Params(	
        l = 60.0,
        d = 14.0,
        w = 14.0, 
        pd = 0.8,
        px = 66.04,
        py = 0.0,
        shape = 'power',
        orient = 'h'
    ), 
    'R_Axial_Power_L60.0mm_W14.0mm_P71.12mm': Params(	
        l = 60.0,
        d = 14.0,
        w = 14.0, 
        pd = 0.8,
        px = 71.12,
        py = 0.0,
        shape = 'power',
        orient = 'h'
    ), 
    'R_Axial_Power_L75.0mm_W9.0mm_P81.28mm': Params(	
        l = 75.0,
        d = 9.0,
        w = 9.0, 
        pd = 0.8,
        px = 81.28,
        py = 0.0,
        shape = 'power',
        orient = 'h'
    ),   
    'R_Axial_Power_L75.0mm_W9.0mm_P86.36mm': Params(	
        l = 75.0,
        d = 9.0,
        w = 9.0, 
        pd = 0.8,
        px = 86.36,
        py = 0.0,
        shape = 'power',
        orient = 'h'
    ),
    'R_Axial_Shunt_L22.2mm_W8.0mm_PS14.30mm_P25.40mm': Params(	
        l = 22.2,
        d = 8.0,
        w = 8.0, 
        pd = 0.8,
        px = 25.40,
        py = 14.30,
        shape = 'shunt',
        orient = 'h'
    ),
    'R_Axial_Shunt_L22.2mm_W9.5mm_PS14.30mm_P25.40mm': Params(	
        l = 22.2,
        d = 9.5,
        w = 9.5, 
        pd = 0.8,
        px = 25.40,
        py = 14.30,
        shape = 'shunt',
        orient = 'h'
    ),
    'R_Axial_Shunt_L35.3mm_W9.5mm_PS25.40mm_P38.10mm': Params(	
        l = 35.3,
        d = 9.5,
        w = 9.5, 
        pd = 0.8,
        px = 38.10,
        py = 25.40,
        shape = 'shunt',
        orient = 'h'
    ),
    'R_Axial_Shunt_L47.6mm_W12.7mm_PS34.93mm_P50.80mm': Params(	
        l = 47.6,
        d = 12.7,
        w = 12.7, 
        pd = 0.8,
        px = 50.80,
        py = 34.93,
        shape = 'shunt',
        orient = 'h'
    ),
    'R_Axial_Shunt_L47.6mm_W9.5mm_PS34.93mm_P50.80mm': Params(	
        l = 47.6,
        d = 9.5,
        w = 9.5, 
        pd = 0.8,
        px = 50.80,
        py = 34.93,
        shape = 'shunt',
        orient = 'h'
    ),
    'R_Bare_Metal_Element_L12.4mm_W4.8mm_P11.40mm': Params(	
        l = 12.4,
        d = 10.0, #height
        w = 4.8, 
        pd = 1.0,
        px = 11.40,
        py = 0.0,
        shape = 'bare',
        orient = 'h'
    ),
    'R_Bare_Metal_Element_L16.3mm_W4.8mm_P15.30mm': Params(	
        l = 16.3,
        d = 10.0, #height
        w = 4.8, 
        pd = 1.0,
        px = 15.30,
        py = 0.0,
        shape = 'bare',
        orient = 'h'
    ),    
    'R_Bare_Metal_Element_L21.3mm_W4.8mm_P20.30mm': Params(	
        l = 21.3,
        d = 10.0, #height
        w = 4.8, 
        pd = 1.0,
        px = 20.30,
        py = 0.0,
        shape = 'bare',
        orient = 'h'
    ), 
    'R_Box_L13.0mm_W4.0mm_P9.00mm': Params(	
        l = 13.0,
        d = 8.0, #height
        w = 4.0, 
        pd = 0.8,
        px = 9.00,
        py = 0.0,
        shape = 'box',
        orient = 'h'
    ),
    'R_Box_L13.0mm_W4.0mm_P9.00mm': Params(	
        l = 13.0,
        d = 8.0, #height
        w = 4.0, 
        pd = 0.8,
        px = 9.00,
        py = 0.0,
        shape = 'box',
        orient = 'h'
    ),  
    'R_Box_L14.0mm_W5.0mm_P9.00mm': Params(	
        l = 14.0,
        d = 10.0, #height
        w = 5.0, 
        pd = 0.8,
        px = 9.00,
        py = 0.0,
        shape = 'box',
        orient = 'h'
    ), 
    'R_Box_L26.0mm_W5.0mm_P20.00mm': Params(	
        l = 26.0,
        d = 10.0, #height
        w = 5.0, 
        pd = 0.8,
        px = 20.00,
        py = 0.0,
        shape = 'box',
        orient = 'h'
    ), 
    'R_Radial_Power_L11.0mm_W7.0mm_P5.00mm': Params(	
        l = 11.0,
        d = 22.0, #height
        w = 7.0, 
        pd = 0.8,
        px = 5.00,
        py = 0.0,
        shape = 'radial',
        orient = 'h'
    ), 
    'R_Radial_Power_L12.0mm_W8.0mm_P5.00mm': Params(	
        l = 12.0,
        d = 24.0, #height
        w = 8.0, 
        pd = 0.8,
        px = 5.00,
        py = 0.0,
        shape = 'radial',
        orient = 'h'
    ),
    'R_Radial_Power_L13.0mm_W9.0mm_P5.00mm': Params(	
        l = 13.0,
        d = 26.0, #height
        w = 9.0, 
        pd = 0.8,
        px = 5.00,
        py = 0.0,
        shape = 'radial',
        orient = 'h'
    ),    
    'R_Radial_Power_L16.1mm_W9.0mm_P7.37mm': Params(	
        l = 16.1,
        d = 32.2, #height
        w = 8.0, 
        pd = 0.8,
        px = 7.37,
        py = 0.0,
        shape = 'radial',
        orient = 'h'
    ),
    'R_Radial_Power_L7.0mm_W8.0mm_Px2.40mm_Py2.30mm': Params(	
        l = 7.0,
        d = 40.0, #height
        w = 8.0, 
        pd = 1.0,
        px = 2.40,
        py = 2.30,
        shape = 'radial',
        orient = 'h'
    ),
    'R_Radial_Power_L9.0mm_W10.0mm_Px2.70mm_Py2.30mm': Params(	
        l = 9.0,
        d = 80.0, #height
        w = 10.0, 
        pd = 1.0,
        px = 2.70,
        py = 2.30,
        shape = 'radial',
        orient = 'h'
    ),
    'R_Array_SIP': Params(	
        l = 0.0,
        d = 8.0, #height
        w = 4.0, 
        pd = 0.6,
        px = 2.54,
        py = 0.0,
        shape = 'array',
        orient = 'h'
    ),
}