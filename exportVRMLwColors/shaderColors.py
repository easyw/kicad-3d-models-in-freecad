class shaderColor():
    def __init__(self, diffuseColor, name = None, ambientIntensity=None, specularColor=None, emissiveColor=None, transparency=None, shininess=None):
        self.name = name #none means do not define within the header of vrml file
        self.ambientIntensity = ambientIntensity if ambientIntensity is not None else 0.0
        self.diffuseColor = diffuseColor if diffuseColor is not None else (0.0, 0.0, 0.0)
        self.specularColor = specularColor if specularColor is not None else (0.0, 0.0, 0.0)
        self.emissiveColor = emissiveColor if emissiveColor is not None else (0.0, 0.0, 0.0)
        self.transparency = transparency if transparency is not None else 0.0
        self.shininess = shininess if shininess is not None else 0.0

    def toVRMLdefinition(self):
        if self.name is None:
            return ""
        result =  'Shape {\n'
        result += '\tappearance Appearance {material DEF ' + self.name +' Material {\n'
        result += '\t\tambientIntensity ' + str(self.ambientIntensity)
        result += '\n\t\tdiffuseColor ' + ' '.join(map(str,self.diffuseColor))
        result += '\n\t\tspecularColor ' + ' '.join(map(str,self.specularColor))
        result += '\n\t\temissiveColor ' + ' '.join(map(str,self.emissiveColor))
        result += '\n\t\ttransparency ' + str(self.transparency)
        result += '\n\t\tshininess ' + str(self.shininess)
        result += '\n\t\t}\n\t}\n}\n'
        return result

    def toVRMLuseColor(self):
        if self.name is None:
            return "appearance Appearance{material Material{\n"+\
            "\tdiffuseColor "+ ' '.join(map(str,self.diffuseColor)) +\
            "\n\t\ttransparency " +str(self.transparency)+"}\n"
        return "appearance Appearance{material USE "+self.name+" }\n"

    def getDiffuseInt(self):
        return self.diffuseColor[0]*255, self.diffuseColor[1]*255, self.diffuseColor[2]*255

    def __str__(self):
        return self.toVRMLdefinition()



named_colors = {
    "metal grey pins":shaderColor(
        name="PIN-01",
        ambientIntensity= 0.271,
        diffuseColor= (0.824, 0.820, 0.781),
        specularColor= (0.328, 0.258, 0.172),
        shininess= 0.70
    ),
    "gold pins":shaderColor(
        name="PIN-02",
        ambientIntensity= 0.379,
        diffuseColor= (0.859, 0.738, 0.496),
        specularColor= (0.137, 0.145, 0.184),
        shininess= 0.40
    ),
    "black body":shaderColor(
        name="IC-BODY-EPOXY-04",
        ambientIntensity= 0.293,
        diffuseColor= (0.148, 0.145, 0.145),
        specularColor= (0.180, 0.168, 0.160),
        shininess= 0.35
    ),
    "resistor black body":shaderColor(
        name="RES-SMD-01",
        diffuseColor= (0.082, 0.086, 0.094),
        specularColor= (0.066, 0.063, 0.063),
        ambientIntensity= 0.638,
        shininess= 0.3
    ),

    "grey body":shaderColor(
        name="CAP-CERAMIC-05",
        ambientIntensity= 0.179,
        diffuseColor= (0.273, 0.273, 0.273),
        specularColor= (0.203, 0.188, 0.176),
        shininess= 0.15
    ),
    "dark grey body":shaderColor(
        name="IC-BODY-EPOXY-01",
        ambientIntensity= 0.117,
        diffuseColor= (0.250, 0.262, 0.281),
        specularColor= (0.316, 0.281, 0.176),
        shininess= 0.25
    ),
    "brown body":shaderColor(
        name="CAP-CERAMIC-06",
        ambientIntensity= 0.453,
        diffuseColor= (0.379, 0.270, 0.215),
        specularColor= (0.223, 0.223, 0.223),
        shininess= 0.15
    ),
    "light brown body":shaderColor(
        name="RES-THT-01",
        ambientIntensity= 0.149,
        diffuseColor= (0.883, 0.711, 0.492),
        specularColor= (0.043, 0.121, 0.281),
        shininess= 0.40
    ),
    "blue body":shaderColor(
        name="PLASTIC-BLUE-01",
        ambientIntensity= 0.565,
        diffuseColor= (0.137, 0.402, 0.727),
        specularColor= (0.359, 0.379, 0.270),
        shininess= 0.25
    ),

    "green body":shaderColor(
        name="PLASTIC-GREEN-01",
        ambientIntensity= 0.315,
        diffuseColor= (0.340, 0.680, 0.445),
        specularColor= (0.176, 0.105, 0.195),
        shininess= 0.25
    ),
    "orange body":shaderColor(
        name="PLASTIC-ORANGE-01",
        ambientIntensity= 0.284,
        diffuseColor= (0.809, 0.426, 0.148),
        specularColor= (0.039, 0.102, 0.145),
        shininess= 0.25
    ),
    "red_body":shaderColor(
        name="RED-BODY",
        ambientIntensity= 0.683,
        diffuseColor= (0.700, 0.100, 0.050),
        specularColor= (0.300, 0.400, 0.150),
        shininess= 0.25
    ),
    "pink body":shaderColor(
        name="CAP-CERAMIC-02",
        ambientIntensity= 0.683,
        diffuseColor= (0.578, 0.336, 0.352),
        specularColor= (0.105, 0.273, 0.270),
        shininess= 0.25
    ),
    "yellow body":shaderColor(
        name="PLASTIC-YELLOW-01",
        ambientIntensity= 0.522,
        diffuseColor= (0.832, 0.680, 0.066),
        specularColor= (0.160, 0.203, 0.320),
        shininess= 0.25
    ),
    "white body":shaderColor(
        name="PLASTIC-WHITE-01",
        ambientIntensity= 0.494,
        diffuseColor= (0.895, 0.891, 0.813),
        specularColor= (0.047, 0.055, 0.109),
        shininess= 0.25
    ),
    "light brown label":shaderColor(
        name="IC-LABEL-01",
        ambientIntensity= 0.082,
        diffuseColor= (0.691, 0.664, 0.598),
        specularColor= (0.000, 0.000, 0.000),
        shininess= 0.01
    ),

    "led red":shaderColor(
        name="LED-RED",
        ambientIntensity= 0.789,
        diffuseColor= (0.700, 0.100, 0.050),
        specularColor= (0.300, 0.400, 0.150),
        transparency= 0.10,
        shininess= 0.125
    ),
    "led green":shaderColor(
        name="LED-GREEN",
        ambientIntensity= 0.789,
        diffuseColor= (0.400, 0.700, 0.150),
        specularColor= (0.600, 0.300, 0.100),
        transparency= 0.10,
        shininess= 0.05
    ),
    "led blue":shaderColor(
        name="LED-BLUE",
        ambientIntensity= 0.789,
        diffuseColor= (0.100, 0.250, 0.700),
        specularColor= (0.500, 0.600, 0.300),
        transparency= 0.10,
        shininess= 0.125
    ),
     "led white":shaderColor(
        name="LED-WHITE",
        ambientIntensity=0.494,
        diffuseColor=(0.895, 0.891, 0.813),
        specularColor=(0.047, 0.055, 0.109),
        transparency=0.10,
        shininess=0.125
        )
}
