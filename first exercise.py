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

    def move(self):
        pass

    def home(self):
        pass

    def make_sound(self):
        pass

    def eat(self):
        pass


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

    def eat(self):
        print("We eat every thing")


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

    def eat(self):
        print("I eat every thing in see")


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

    def eat(self):
        print("I eat bugs")


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

    def eat(self):
        print("...")


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

    def eat(self):
        print("...")


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

    def eat(self):
        print('...')


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


class Cat(Mammal):
    '''one of the group of Mammal'''

    def __init__(self, kind="", name="", color="", race="", nationality="", age=""):
        super().__init__(kind, name, color, race, nationality, age)

    def info(self):
        print(f"Hello, I am a cat"
              f"I am from {self.nationality}"
              f"My name is {self.name} "
              f"and my color is {self.color}"
              f"I am {self.race}")

    def make_sound(self):
        print("meeeoowwww...")

    def move(self):
        print("I walk")

    def eat(self):
        print("I eat meat")

    def home(self):
        print("My home in jungle and city")


class Cow(Mammal):
    '''one of the group of Mammal'''

    def __init__(self, kind="", name="", color="", race="", nationality="", age=""):
        super().__init__(kind, name, color, race, nationality, age)

    def info(self):
        print(f"Hello, I am a cow"
              f"I am from {self.nationality}"
              f"My name is {self.name} "
              f"and my color is {self.color}"
              f"I am {self.race}")

    def make_sound(self):
        print("moooow...")

    def move(self):
        print("I walk")

    def eat(self):
        print("I eat plant")

    def home(self):
        print("My home in village")


class Dog(Mammal):
    '''one of the group of Mammal'''

    def __init__(self, kind="", name="", color="", race="", nationality="",age=""):
        super().__init__(kind, name, color, race, nationality, age)

    def info(self):
        print(f"Hello, I am a dog"
              f"I am from {self.nationality}"
              f"My name is {self.name} "
              f"and my color is {self.color}"
              f"I am {self.race}")

    def make_sound(self):
        print("hoop hop...")

    def move(self):
        print("I walk")

    def eat(self):
        print("I eat meat")

    def home(self):
        print("My home in jungle and village and city")


class Ship(Mammal):
    '''one of the group of Mammal'''

    def __init__(self, kind="", name="", color="", race="", nationality="", age=""):
        super().__init__(kind, name, color, race, nationality, age)

    def info(self):
        print(f"Hello, I am a ship"
              f"I am from {self.nationality}"
              f"My name is {self.name} "
              f"and my color is {self.color}"
              f"I am {self.race}")

    def make_sound(self):
        print("beeee bee...")

    def move(self):
        print("I walk")

    def eat(self):
        print("I eat plant")

    def home(self):
        print("My home in village")


class Frog(Amphibians):
    '''one of the group of Amphibians'''

    def __init__(self, kind="", name="", color="", race="", nationality="", age=""):
        super().__init__(kind, name, color, race, nationality, age)

    def info(self):
        print(f"An adult frog has a stout body, protruding eyes, anteriorly-attached tongue, limbs folded underneath, "
              f"and no tail (the tail of tailed frogs is an extension of the male cloaca). Frogs have glandular skin, "
              f"with secretions ranging from distasteful to toxic."
              f" Their skin varies in colour from well-camouflaged dappled brown,"
              f" grey and green to vivid patterns of bright red or yellow and black"
              f" to show toxicity and ward off predators.")

    def make_sound(self):
        print("ghooor ghor ...")

    def move(self):
        print("I jump and swim")

    def home(self):
        print("I am living in marsh.")

    def eat(self):
        print("I eat bugs")


class Passerine_Bird(Bird):
    '''one of the group of Bird'''

    def __init__(self, kind="", name="", color="", race="", nationality="",age=""):
        super().__init__(kind, name, color, race, nationality, age)

    def info(self):
        print(f"A passerine is any bird of the order Passeriformes , "
              f"which includes more than half of all bird species. "
              f"Sometimes known as perching birds, passerines generally have "
              f"an anisodactyl arrangement of their toes (three pointing forward and one back),"
              f" which facilitates perching")

    def eat(self):
        print("I eat worm")

    def home(self):
        print("My home in jungle and city")


class Old_World_Sparrow(Passerine_Bird):
    '''one of the group of Passerine_Bird'''

    def __init__(self, kind="", name="", color="", race="", nationality="",age=""):
        super().__init__(kind, name, color, race, nationality, age)

    def info(self):
        print(f"Old World sparrows are a group of small passerine birds forming the family Passeridae."
              f" They are also known as true sparrows, a name also used for a particular genus of the family, Passer."
              f" They are primarily seed-eaters, though they also consume small insects.")

    def eat(self):
        print("I eat seed and worm")

    def make_sound(self):
        print("jiik jik...")

    def home(self):
        print("My home in jungle and city")

