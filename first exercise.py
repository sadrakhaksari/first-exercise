class Animal:
    '''base class'''

    def __init__(self, kind="", name="", color="", race="", nationality="", age=""):
        self.kind = kind
        self.name = name
        self.color = color
        self.race = race
        self.nationality = nationality
        self.age = age

    def info(self):
        #very small comment about animal
        
        print(f"Hello, I am a animal"
              f"I am from {self.nationality}"
              f"My name is {self.name} "
              f"and my color is {self.color}"
              f"I am {self.race}")