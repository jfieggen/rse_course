### Compositions
#   We use compostitions when something has something. e.g. a doctor has a patient or a patient has a observation
#   We can thus make an observation class as well as a patient class

# file: inflammation/models.py

class Observation:
    def __init__(self, day, value):
        self.day = day
        self.value = value

    def __str__(self):
        return str(self.value)

class Patient:
    """A patient in an inflammation study."""
    def __init__(self, name):
        self.name = name
        self.observations = []

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1].day + 1

            except IndexError:
                day = 0

        new_observation = Observation(day, value)

        self.observations.append(new_observation)
        return new_observation

    def __str__(self):
        return self.name


alice = Patient('Alice')
obs = alice.add_observation(3)

print(obs)
print(alice)

### The other type of relatinoship used in OOP is inheritence 
#   Inheritance is about data and behaviour shared by classes, because they have some shared identity - 'x is a y'.
#   If class X inherits from (is a) class Y, we say that Y is the superclass or parent class of X, or X is a subclass of Y.

# We can extend the above to include the class person as patients are people!
# file: inflammation/models.py

class Observation:
    def __init__(self, day, value):
        self.day = day
        self.value = value

    def __str__(self):
        return str(self.value)

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Patient(Person):
    """A patient in an inflammation study."""
    def __init__(self, name):
        super().__init__(name)
        self.observations = []

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1].day + 1

            except IndexError:
                day = 0

        new_observation = Observation(day, value)

        self.observations.append(new_observation)
        return new_observation

alice = Patient('Alice')
print(alice)

obs = alice.add_observation(3)
print(obs)

bob = Person('Bob')
print(bob)

#obs = bob.add_observation(4)
print(obs)

## Expected error with bob who is a person but not a patient

## Composition vs Inheritence
#   hen deciding how to implement a model of a particular system, you often have a choice of either composition or inheritance, where there is no obviously correct choice. 
#   For example, it's not obvious whether a photocopier is a printer and is a scanner, or has a printer and has a scanner.

# Inheritence
class Machine:
    pass

class Printer(Machine):
    pass

class Scanner(Machine):
    pass

class Copier(Printer, Scanner):
    # Copier `is a` Printer and `is a` Scanner
    pass

# Compositon
class Machine:
    pass

class Printer(Machine):
    pass

class Scanner(Machine):
    pass

class Copier(Machine):
    def __init__(self):
        # Copier `has a` Printer and `has a` Scanner
        self.printer = Printer()
        self.scanner = Scanner()


#   These are the same thing. However, generally thought preferable to use composition over inheritence


# Try to avoid multiple inheritence

