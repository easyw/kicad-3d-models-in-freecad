import FreeCAD

def say(*arg):
    FreeCAD.Console.PrintMessage(" ".join(map(str,arg)) + "\r\n")
    
def sayw(*arg):
    FreeCAD.Console.PrintWarning(" ".join(map(str,arg)) + "\r\n")
    
def saye(*arg):
    FreeCAD.Console.PrintError(" ".join(map(str,arg)) + "\r\n")