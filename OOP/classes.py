
import numpy as np

# Define data
data = np.array([[1., 2., 3.],
                 [4., 5., 6.]])

print(data)

#Define patients
patients = [
    {
        'name': 'Alice',
        'data': [1., 2., 3.],
    },
    {
        'name': 'Bob',
        'data': [4., 5., 6.],
    },
]

print(patients)

#Write a function  attach_names, which can be used to attach names to our patient dataset.
def attach_names(data, names):
    """Create datastructure containing patient records."""
    output = []

    for i in range(len(data)):
        output.append({'name': names[i],
                       'data': data[i]})

    return output

#Use Zip and Assert to avoid need for indexing and to ensure data and names are the same length
def attach_names(data, names):
    """Create datastructure containing patient records."""
    assert len(data) == len(names)
    output = []

    for data_row, name in zip(data, names):
        output.append({'name': name,
                       'data': data_row})

    return output

output = attach_names(data, ['Alice', 'Bob'])
print(output)

## Classes
#A class is a template or blueprint to avoid having to use nested dictionaries and lists
#instances of classess are called objects
#All objects from a class bydeinfition must follow the same strcuture

#Already know some classes:
my_list = [1, 2, 3]
my_dict = {1: '1', 2: '2', 3: '3'}
my_set = {1, 2, 3}

print(type(my_list))
print(type(my_dict))
print(type(my_set))

#Start with a simple class to represent our patients:

class Patient:
    def __init__(self, name):
        self.name = name
        self.observations = []

alice = Patient('Alice')
print(alice.name)

# Methods are functions within classess
# The Method __init__  is the initialiser method, which is responsible for setting up the initial values and structure of the data inside a new instance of the class
# Init must be called every time, the argument self refers to the instance on which we're calling the method and gets filled automatically
# Attributes are typically hidden (encapsulated) internal object details ensuring that access to data is protected from unintended changes. 
#   They are manipulated internally by the class, which, in addition, can expose certain functionality as public behavior of the class to allow other objects to interact with this class' instances.

####
# Classes contain encapsulated methods (functions) which describe the behaviour of the data within the class
# Methods on classes are the same as normal functions, except that they live inside a class and have an extra first parameter `self`.

#Adding a method that adds observations

# file: inflammation/models.py

#define
class Patient:
    """A patient in an inflammation study."""
    def __init__(self, name):
        self.name = name
        self.observations = []

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1]['day'] + 1

            except IndexError:
                day = 0

        new_observation = {
            'day': day,
            'value': value,
        }

        self.observations.append(new_observation)
        return new_observation

# call patient
alice = Patient('Alice')
print(alice)

#add observation to alice for day 0
observation = alice.add_observation(3)
observation = alice.add_observation(4)
observation = alice.add_observation(5)

print(observation)
print(alice.observations)

### Dunders

## a method starting with a _ _ is a dunder method. __init__ is one, and __str__ is another. Here we use it to override the string 
#       representation of our object alice(<__main__.Patient object at 0x104f25f90>)

# file: inflammation/models.py

class Patient:
    """A patient in an inflammation study."""
    def __init__(self, name):
        self.name = name
        self.observations = []

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1]['day'] + 1

            except IndexError:
                day = 0


        new_observation = {
            'day': day,
            'value': value,
        }

        self.observations.append(new_observation)
        return new_observation

    def __str__(self):
        return self.name

alice = Patient('Alice')
print(alice)

# Common Dunders include:
#   __str__ - converts an object into its string representation, used when you call str(object) or print(object)
#   __getitem__ - Accesses an object by key, this is how list[x] and dict[x] are implemented
#   __len__ - gets the length of an object when we use len(object) - usually the number of items it contains

### Implement a class
# Implement a class to represent a book. Your class should have a title, an author, and when printed using print(book), show text in the format "title by author"

class Book:
    """A class to link an author and a title"""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title + ' by ' + self.author
    
book = Book('A Book', 'Me')

print(book)

### Properties  Properties are methods which behave like data. When we access them we do not need to use brackets to call the method manually

class Patient:
    """A patient in an inflammation study."""
    def __init__(self, name):
        self.name = name
        self.observations = []

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1]['day'] + 1

            except IndexError:
                day = 0


        new_observation = {
            'day': day,
            'value': value,
        }

        self.observations.append(new_observation)
        return new_observation

    def __str__(self):
        return self.name

    @property
    def last_observation(self):
        return self.observations[-1]

alice = Patient('Alice')

alice.add_observation(3)
alice.add_observation(4)
alice.add_observation(5)

obs = alice.last_observation
print(obs)
