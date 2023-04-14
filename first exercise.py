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


class Mammal(Animal):

    '''one of the group of animal'''

    def __init__(self, kind="", name="", color="", race="", nationality="", age=""):
        super().__init__(kind, name, color, race, nationality, age)

    def info(self):
        print(f"Young mammals get nourishment from milk produced by their mothers."
              f"Most mammals have hair."
              f"Their jaw is hinged directly to their skull, unlike all other vertebrates."
              f"Almost all mammals give birth to live babies."
              f"They are endothermic, or warm-blooded.")

    def make_sound(self):
        print("...")

    def move(self):
        print("I walk")

    def home(self):
        print("My home in world")


class Fish(Animal):

    '''one of the group of animal'''

    def __init__(self, kind="", name="", color="", race="", nationality="", age=""):
        super().__init__(kind, name, color, race, nationality, age)

    def info(self):
        print(f"Fish are also vertebrates, and they are considered the oldest-known vertebrates."
              f"Fish have fins"
              f"Most, but not all, fish have bodies covered in scales and breathe through gills."
              f"Fish live underwater.")

    def make_sound(self):
        print("...")

    def move(self):
        print("I swim")

    def home(self):
        print("My home in see")


class Bird(Animal):
    '''one of the group of animal'''

    def __init__(self, kind="", name="", color="", race="", nationality="", age=""):
        super().__init__(kind, name, color, race, nationality, age)

    def info(self):
        print(f"Birds are a type of warm-blooded vertebrate that are adapted to fly."
              f"Not all birds can fly, but they do all have wings."
              f"Birds have beaks that help them catch and swallow food."
              f"The digestive system of a bird allows it to eat whenever it can and digest the food later."
              f"Birds lay eggs to reproduce."
              f"They are bipedal, which means they have two legs."
              f"They have hollow bones and their bodies are covered in feathers.")

    def make_sound(self):
        print("...")

    def move(self):
        print("I fly")

    def home(self):
        print("My home in jungle and city")


class Reptile(Animal):
    '''one of the group of animal'''

    def __init__(self, kind="", name="", color="", race="", nationality="", age=""):
        super().__init__(kind, name, color, race, nationality, age)

    def info(self):
        print(f"They are cold-blooded, or ectothermic."
              f"They lay eggs to reproduce."
              f"They have four legs or are descended from animals with four legs."
              f"They breathe through lungs."
              f"Their bodies are covered in scales or scutes.")

    def make_sound(self):
        print("...")

    def move(self):
        print("I slither")

    def home(self):
        print("My home in jungle")


class Amphibians(Animal):
    '''one of the group of animal'''

    def __init__(self, kind="", name="", color="", race="", nationality="", age=""):
        super().__init__(kind, name, color, race, nationality, age)

    def info(self):
        print(f"All amphibians are vertebrates, and they need moist environments or water to survive."
              f"They are cold-blooded."
              f"They absorb water and breathe through their thin skin."
              f"They have at least one special skin gland used for defense."
              f"Most follow the life cycle of egg-larva-adult.")

    def make_sound(self):
        print("...")

    def move(self):
        print("I slither and swim")

    def home(self):
        print("I am living within terrestrial, fossorial, arboreal or freshwater aquatic ecosystems.")


class Invertebrates(Animal):
    '''one of the group of Animal'''

    def __init__(self, kind="", name="", color="", race="", nationality="", age=""):
        super().__init__(kind, name, color, race, nationality, age)

    def info(self):
        print(f"Approximately 95% of all animals are invertebrates. Invertebrates do not have a backbone."
              f"They are made up of many cells that work together or are multicellular."
              f"They generally have soft bodies.")

    def make_sound(self):
        print("...")

    def move(self):
        print("...")

    def home(self):
        print("My home in driest of desert")


class Shark(Fish):
    '''one of the group of fish'''

    def __init__(self, kind="", name="", color="", race="", nationality="", age=""):
        super().__init__(kind, name, color, race, nationality, age)

    def info(self):
        print(f"Sharks are a group of elasmobranch fish characterized by a cartilaginous skeleton,"
              f" five to seven gill slits on the sides of the head, and pectoral fins that are not fused to the head.")

    def make_sound(self):
        print("blub blub...")

    def move(self):
        print("I swim")

    def home(self):
        print("My home in see")

    def eat(self):
        print("I eat the another fish:)))")



