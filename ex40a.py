mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])  ##using Dict to get sth

import mystuff
mystuff.apple()
print(mystuff.tangerine)  ##using Module to get sth

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

thing = MyStuff()
thing.apple()
print(thing.tangerine)  ##using Class to get sth