# using the @property

class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    @property
    def temperature(self):
        print("Getting value...")
        return self._temp

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Not possible")
        self._temp = value


human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())



coldest_thing = Celsius(-300)











    
