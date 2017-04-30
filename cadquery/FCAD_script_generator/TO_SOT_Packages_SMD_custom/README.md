# TO_SOT_Packages_SMD_custom

This folder contains non-standard and "one off" scripts used to create individual TO or SOT SMD parts.


## DPAK

Scripts to generate models for the following package types:
- TO252 (DPAK)
- TO263 (D2PAK, DDPAK)
- TO268 (D3PAK)

### Usage

Download and install `kicad-3d-models-in-freecad` from https://github.com/easyw/kicad-3d-models-in-freecad

Install the following files in the folder `.../kicad-3d-models-in-freecad/cadquery/FCAD_script_generator/<category>/`.

```
DPAK_export.py      # export script
DPAK_factory.py     # model building script
DPAK_config.yaml    # model configuration file
ribbon.py           # helper class
```

Build and export models for all types:

```
$ freecad ./DPAK_export.py
```

Build and export models for the specified types:

```
$ freecad ./DPAK_export.py TO252 TO268
```

The model configuration file is documented here: https://github.com/hackscribble/kicad-footprint-generator/blob/add_DPAK_script/scripts/TO_SOT_Packages_SMD/DPAK_README.md

User licence details are configured in `DPAK_export.py`:

```
##########################################################################################

# MODEL LICENCE CONFIGURATION

# Details to be included in the generated models
L.STR_int_licAuthor = "Ray Benitez"
L.STR_int_licEmail = "hackscribble@outlook.com"

##########################################################################################
```
