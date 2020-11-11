Following models can be generated:    
(Click entry to unfold/fold)  
<details>  
  <summary>Vertical connectors</summary>  

- Wago_734-132_1x02_P3.50mm_Vertical
- Wago_734-133_1x03_P3.50mm_Vertical
- Wago_734-134_1x04_P3.50mm_Vertical
- Wago_734-135_1x05_P3.50mm_Vertical
- Wago_734-136_1x06_P3.50mm_Vertical
- Wago_734-137_1x07_P3.50mm_Vertical
- Wago_734-138_1x08_P3.50mm_Vertical
- Wago_734-139_1x09_P3.50mm_Vertical
- Wago_734-140_1x10_P3.50mm_Vertical
- Wago_734-141_1x11_P3.50mm_Vertical
- Wago_734-142_1x12_P3.50mm_Vertical
- Wago_734-143_1x13_P3.50mm_Vertical
- Wago_734-144_1x14_P3.50mm_Vertical
- Wago_734-146_1x16_P3.50mm_Vertical
- Wago_734-148_1x18_P3.50mm_Vertical
- Wago_734-150_1x20_P3.50mm_Vertical
- Wago_734-154_1x24_P3.50mm_Vertical
</details>

<details>  
  <summary>Horizontal connectors</summary>
      
- Wago_734-162_1x02_P3.50mm_Horizontal
- Wago_734-163_1x03_P3.50mm_Horizontal
- Wago_734-164_1x04_P3.50mm_Horizontal
- Wago_734-165_1x05_P3.50mm_Horizontal
- Wago_734-166_1x06_P3.50mm_Horizontal
- Wago_734-167_1x07_P3.50mm_Horizontal
- Wago_734-168_1x08_P3.50mm_Horizontal
- Wago_734-169_1x09_P3.50mm_Horizontal
- Wago_734-170_1x10_P3.50mm_Horizontal
- Wago_734-171_1x11_P3.50mm_Horizontal
- Wago_734-172_1x12_P3.50mm_Horizontal
- Wago_734-173_1x13_P3.50mm_Horizontal
- Wago_734-174_1x14_P3.50mm_Horizontal
- Wago_734-176_1x16_P3.50mm_Horizontal
- Wago_734-178_1x18_P3.50mm_Horizontal
- Wago_734-180_1x20_P3.50mm_Horizontal
- Wago_734-184_1x24_P3.50mm_Horizontal
</details>

## Running the scripts
      

to run the script just move to the scripts dir and do:

`..../bin/freecad.exe  main_generator.py  option`       

where *option* is one of *| all | list | filter*      
- *all* - generate all models    
- *list* - list all model names     
- *filter* - a reqular expression matching model names in the models list above (not case sensitive)   
     
examples in win:    
`c:\freecad\bin\freecad main_generator.py wago*`            
`c:\freecad\bin\freecad main_generator.py *164*`           
`c:\freecad\bin\freecad main_generator.py all`        
        
in linux:   
`freecad ./main_generator.py *hori*`           
`freecad ./main_generator.py *1x0*`          
`freecad ./main_generator.py list`              
       
         
When running the script with no arguments, no models will be generated and a help text will be displayed in the FreeCAD `report view` window     
The 3D model files will be saved in:    
`..\_3Dmodels\Connector_Wago.3dshapes`    


