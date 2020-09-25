
Following models can be generated:
|3D file| destination dir|
| :--- | :--- |
|Nidec_Copal_SH-7010A|../3Dmodels/Button_Switch_SMD.3dshapes/
|Nidec_Copal_SH-7010B|../3Dmodels/Button_Switch_SMD.3dshapes/
|Nidec_Copal_SH-7010C|../3Dmodels/Button_Switch_THT.3dshapes/
|Nidec_Copal_SH-7040B|../3Dmodels/Button_Switch_SMD.3dshapes/          
| |            
## Running the scripts
      

to run the script just move to the scripts dir and do:

`..../bin/freecad.exe  main_generator.py  option`       

where *option* is one of *| all | allsmd | list | variant | filter*      
- *all* - generate all models    
- *allsmd* - generate all SMD models       
- *list* - list all model names     
- *variant* - a variant from the generic names found in in cq_parameters.py (`variableParams.base_params`)    
- *filter* - a reqular expression matching model names in the models list above   
     
examples in win:    
`c:\freecad\bin\freecad main_generator.py 7010B`            
`c:\freecad\bin\freecad main_generator.py *701*`           
`c:\freecad\bin\freecad main_generator.py all`        
        
in linux:   
`freecad ./main_generator.py 7040B`           
`freecad ./main_generator.py Nidec*`          
`freecad ./main_generator.py allsmd`              
       
         
When running the script with no arguments, all models will be generated.     

