import FreeCAD

class FreeCADVersionError(Exception):
    def __init__(self, required_version, reason=""):
        self.required_version = required_version
        self.reason = reason
    def __str__(self):
        return "FreeCAD version to old. Required version: {:s}\n{:s}".format(
                        self.required_version, self.reason
                    )

class BOBError(Exception):
    def __init__(self, modelName, obj_name, obj_label, details):
        self.modelName = modelName
        self.obj_name = obj_name
        self.obj_label = obj_label
        self.details = details

    def __str__(self):
        return "Geometry check for model {:s} ({:s}:{:s}) failed\n".format(
            self.modelName, self.obj_name, self.obj_label)
    def getDetails(self):
        return self.details

class NotUnionedError(Exception):
    def __init__(self, modelName):
        self.modelName = modelName
    def __str__(self):
        return "Step file for model {:s} not correctly unioned\n".format(self.modelName)

class GeometryError(Exception):
    def __init__(self):
        self.union_error = None
        self.bob_errors = []
        self.error_encountered = False
    def append(self,e):
        self.error_encountered = True
        if isinstance(e, BOBError):
            self.bob_errors.append(e)
        elif isinstance(e, NotUnionedError):
            self.union_error = e
    def print_errors(self, with_details=False):
        if self.union_error:
            FreeCAD.Console.PrintError(self.union_error)
        for bob_error in self.bob_errors:
            FreeCAD.Console.PrintError(bob_error)
            if with_details:
                FreeCAD.Console.PrintWarning(bob_error.getDetails())
