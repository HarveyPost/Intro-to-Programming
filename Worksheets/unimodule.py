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
            raise TypeError("expected item be an instance of UniModule.")
        if item in self.modules:
            raise ValueError("module already exists!")
        self.modules.append(item)
    
    def print_transcript(self):
        for module in self.modules:
            print(module.display_details())

COMP1012 = UniModule("COMP1011", "Intro to Prog.", 1, 10, grade=75, discovery=True)
COMP1121 = UniModule("COMP1121", "Databases", 1, 10, PFP=True)
COMP1211 = UniModule("COMP1211", "Comp. Arch.", 1, 10, grade=80, PFP=True)
t_student1 = Transcript()
t_student1.add_module(COMP1012)
t_student1.add_module(COMP1121)
t_student1.add_module(COMP1211)
t_student1.print_transcript()