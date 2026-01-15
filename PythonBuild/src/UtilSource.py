import os
import ReCoreLib

class __polishutil__:
    def __init__(self, name, factor, path, eor, filename=None):
        self.name = name
        self.factor = factor
        self.path = path
        self.eor = eor
        self.filename = filename or f"{self.name.replace(' ', '_')}.py"
    
    def __call__(self):
        print(f"Creating {self.name} utility...")
    
        current_dir = os.path.dirname(os.path.abspath(__file__))
        uc_path = os.path.join(current_dir, self.path)
        os.makedirs(uc_path, exist_ok=True)
        file_path = os.path.join(uc_path, self.filename)
    
        with open(file_path, "w") as file:
            if self.eor:
                file.writelines(ReCoreLib.UEOR)
            else:
                file.write(ReCoreLib.PHC)
                file.write("\n")
                file.write(ReCoreLib.UPHC)
    
        print(f"Utility saved to {file_path}")
        return print(f"Utility '{self.name}' created at '{file_path}' with EOR set to {self.eor}.")
    
    def __repr__(self):
        return f"PolishUtil(name='{self.name}', factor='{self.factor}', path='{self.path}', eor={self.eor})"
