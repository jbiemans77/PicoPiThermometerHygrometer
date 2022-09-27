class ReptileDetails:
    def __init__(self, species, idealTemperature, idealHumidity):
        self.species = species
        self.idealTemperature = idealTemperature
        self.idealHumidity = idealHumidity
        
    def __str__(self):
        return f"INFO:{self.species};{self.idealTemperature} C / {self.idealHumidity} %"