##Animal is-a object
class Animal(object):
    pass

## make a class named dog that is-a animal:
class Dog(Animal):

    def __init__(self, name):
        ##
        self.name = name

class Cat(Animal):

    def __init__(self, name):
        ## 
        self.name = name

class Person(object):

    def __init__(self, name):
        self.name = name
        print("Person created")
        
        
        
        self.pet = None



class Employee(Person):

    def __init__(self, name, salary):
        
        super(Employee, self).__init__(name)
        print("Employee created")

        self.salary = salary
        print(self.salary)


class Fish(object):
    pass


class Salmon(Fish):
    pass


class Halibut(Fish):
    pass



rover = Dog("Rover")


satan = Cat("Satan")


mary = Person("Mary")


mary.pet = satan

print("^^^^^")
frank = Employee("Frank", 120000)


frank.pet = rover


flipper = Fish()


crouse = Salmon()


harry = Halibut()

