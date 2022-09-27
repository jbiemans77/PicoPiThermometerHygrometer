class DisplayScreenDetails():
    def __init__(self, current, ideal, label, sufix):
        self.current = current
        self.ideal = ideal
        self.label = label
        self.sufix = sufix
        
    def __str__(self):
        returnString = f"Current: {self.current}. "
        returnString += f"Ideal: {self.ideal}. "
        returnString += f"Label: {self.label}. "
        returnString += f"Sufix: {self.sufix}. "
        
        return returnString
        
        