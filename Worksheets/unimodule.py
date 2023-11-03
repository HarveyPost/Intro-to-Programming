class UniModule():
    def __init__(self, code, name, year, credit, grade = 0, PFP = False, discovery = False):
        self.code = code
        self.name = name
        self.year = year
        self.credit = credit
        self.grade = grade
        self.PFP = PFP
        self.discovery = discovery
    
    def display_details(self):
        PFP_string = "PFP" if self.PFP else "NPFP"
        discovery_string = "Disc" if self.discovery else "NDisc"
        return f"{self.code}:{self.name}:Y{self.year}:{self.credit}CR:{self.grade}GRD:{PFP_string}:{discovery_string}"
    

class Transcript():
    def __init__(self, modules = []):
        self.modules = modules
    
    def add_module(self, item):
        if not isinstance(item, UniModule):
            raise ValueError("expected item be an instance of UniModule.")
        if item in self.modules:
            raise ValueError("module already exists!")
        self.modules.append(item)
    
    def print_transcript(self):
        for module in self.modules:
            print(module.display_details())