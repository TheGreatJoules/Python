#-----------------------------------------------------------------------
# animals.py
#-----------------------------------------------------------------------

## Animal is-a object
class Animal(object):
    pass

## Dog is-a kind of Animal
class Dog(Animal):

    def __init__(self, name):
        ##
        self.name = name
        print("Dog: ", name)


## Cat is-a kind of Animal
class Cat(Animal):

    def __init__(self, name):
        ##
        self.name = name
        print("Cat: ", name)

## Person is-a object
class Person(object):

    def __init__(self, name):
        ##
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None
        print("Person: ", name)

## Employee is-a kind of Person
class Employee(Person):

    def __init__(self, name, salary):
        ## hmm what is this strange magic
        super(Employee, self).__init__(name)
        self.salary = salary
        print("Employee: ", name)

##
class Fish(object):
    pass

##
class Salmon(Fish):
    pass

##
class Halibut(Fish):
    pass

## rover is a dog
rover = Dog("Rover")

## luna is a cat
luna = Cat("Luna")

## mary is a person
mary = Person("Mary")
mary.pet = luna

frank = Employee("Frank", 120000)
frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()
