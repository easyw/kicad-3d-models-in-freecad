Following SMD models can be generated:    
(Click entry to unfold/fold)  
<details>  
  <summary>SMD tactile buttons</summary>  

- SW_SPST_B3S-1000      
- SW_SPST_B3S-1100      
- SW_SPST_B3SL-1002P      
- SW_SPST_B3SL-1022P      
- SW_SPST_B3U-1100P-B      
- SW_SPST_B3U-1100P      
- SW_SPST_Omron_B3FS-100xP      
- SW_SPST_Omron_B3FS-101xP      
- SW_SPST_Omron_B3FS-105xP      
- SW_push_1P1T_NO_CK_KSC6xxJxxx      
- SW_push_1P1T_NO_CK_KSC7xxJxxx      
- SW_SPST_EVPBF
- SW_SPST_EVQP0
- SW_SPST_EVQP2
- SW_SPST_Panasonic_EVQPL_3PL_5PL_PT_A08
- SW_SPST_Panasonic_EVQPL_3PL_5PL_PT_A15
- SW_PUSH_6mm_H9.5mm
- SW_SPST_SKQG_WithStem
- SW_SPST_SKQG_WithoutStem
- SW_SPST_TL3305A
- SW_SPST_TL3305B
- SW_SPST_TL3305C
- SW_Push_SPST_NO_Alps_SKRK
- SW_Push_1P1T_NO_CK_PTS125Sx43PSMTR
- SW_Push_1P1T_NO_CK_PTS125Sx85PSMTR
- SW_Push_1P1T_NO_CK_PTS125Sx73PSMTR
- SW_Push_1P1T_NO_CK_PTS125Sx43SMTR
- SW_Push_1P1T_NO_CK_PTS125Sx85SMTR
- SW_Push_1P1T_NO_CK_PTS125Sx73SMTR
- Panasonic_EVQPUJ_EVQPUA
- Panasonic_EVQPUK_EVQPUB
- Panasonic_EVQPUL_EVQPUC
- Panasonic_EVQPUM_EVQPUD
- SW_SPST_EVQP7A
- SW_SPST_EVQP7C
- SW_SPST_B3U-3000P-B
- SW_SPST_B3U-3000P
- SW_SPST_B3U-3100P-B
- SW_SPST_B3U-3100P
- SW_Push_1P1T-SH_NO_CK_KMR2xxG
- SW_Push_1P1T_NO_CK_KMR2
- SW_SPST_PTS810
</details>

<details>  
  <summary>THT tactile buttons</summary>
      
- SW_TH_Tactile_Omron_B3F-10xx
- SW_TH_Tactile_Omron_B3F-11xx
- SW_Tactile_Straight_KSA0Axx1LFTR
- SW_Tactile_Straight_KSL0Axx1LFTR
- SW_PUSH_6mm_H8.5mm
- SW_PUSH-12mm
- SW_PUSH-12mm_Wuerth-430476085716
</details>

## Running the scripts
      

to run the script just move to the scripts dir and do:

`..../bin/freecad.exe  main_generator.py  option`       

where *option* is one of *| all | list | filter*      
- *all* - generate all models    
- *list* - list all model names     
- *filter* - a reqular expression matching model names in the models list above (not case sensitive)   
     
examples in win:    
`c:\freecad\bin\freecad main_generator.py sw_push*`            
`c:\freecad\bin\freecad main_generator.py *B3U*`           
`c:\freecad\bin\freecad main_generator.py all`        
        
in linux:   
`freecad ./main_generator.py *tactile*`           
`freecad ./main_generator.py *evqp*`          
`freecad ./main_generator.py list`              
       
         
When running the script with no arguments, no models will be generated and a help text will be displayed in the FreeCAD `report view` window     
The 3D model files will be saved in:    
`..\_3Dmodels\Button_Switch_SMD.3dshapes`    
`..\_3Dmodels\Button_Switch_THT.3dshapes`    


