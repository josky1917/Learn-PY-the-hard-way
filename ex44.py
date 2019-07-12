class Parent(object):
    def implicit(self):
        print("Parent implicit()")

    def override(self):
        print("Parent overide()")

    def altered(self):
        print("Parent altered()")

class Child(Parent):
    def override(self):
        print("Child override()",self)

    def altered(self):
        print("Child, Before altered()",self)
        super(Child, self).altered()
        print("Child, After altered()",self)
    

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()