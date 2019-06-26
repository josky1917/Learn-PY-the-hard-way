from sys import exit

def big_cave():
    print("Suddenly, a big devil crab appears!")
    print("Warrior, you want to fight or run?")

    while True:
        choice = input("> ")

        if choice == "fight":
            print("After a fierce bettle, you beat the crab and get a large claw!")
            congratuation()
        elif choice == "run":
            print("Man, you cannot swim faster than a marine creature let alone the owner in this cave.")
            print("You have been caught by a big claw. The big devil crab cut you into pieces.")
            failure()
        else:
            print("Man, I got no idea what that means.")

def large_abyss():
    print("Deep and deep. Now you are faced with a giant king squid!")
    print("What should you do, fight or run?")

    while True:
        choice = input("> ")

        if choice == "fight":
            print("The giant king squid is angry, and it split the ink!")
            print("You are surrounded with dark.")
            dark()
        elif choice == "run":
            print("Man, you cannot swim faster than a marine creature let alone the king in such an abyss.")
            print("You have been entangled by tentacles. The giant king squid swallow you.")
            failure()
        else:
            print("Man, I got no idea what that means.")

def dark():
    print("You cannot see anything! What should you do?")
    print("1. punch the dark shallow by fists.")
    print("2. take out your knife from pocket and hold it in front your chest.")

    choice = input("> ")

    if choice == "1":
        print("That's of no use. Man, a qualified warrior is not just with brave.")
        print("Your hands have been entangled by tantacles.")
        print("The giant king squid swallow you.")
        failure()
    elif choice == "2":
        print("That's a good choice.")
        print("The giant king squid wants to bind you.")
        print("But the tantacles have been cut down by your knife.")
        print("You got a bunch of calamari!")
        congratuation()
    else:
        print("Sorry, you didn't figure out the right choice.")
        print("You have been binded. The giant king squid has swallowed you.")
        failure()

def ocean():
    print("Warrior, after sinking deeper in ocean, here is a crossroad!")
    print("Which one is your choice:")
    print("1. a big dark cave.")
    print("2. a horror abyss.")

    while True:
        choice = input("> ")

        if choice == "1":
            big_cave()
        elif choice == "2":
            large_abyss()
        else:
            print("Man, choose 1 or 2.")

def southern_way():
    print("A hugh brown bear notice you and run to you!")
    print("What should you do now?")
    print("1. fight with bear.")
    print("2. pretend death.")
    print("3. flee away.")

    while True:
        choice = input("> ")

        if choice == "1":
            print("Your strength is too weak.")
            print("The brown bear hit you down. You will be its dinner tonight.")
            failure()
        elif choice == "2":
            print("The bear come close and start to sniff you.")
            sniff()
        elif choice == "3":
            print("When you are trying to stand up, a big slap comes.")
            print("The bear hits down you. You will be its dinner tonight.")
            failure()
        else:
            print("Man, choose 1, 2 or 3.")    

def sniff():
    print("What should you do now?")
    print("1. punch its eyes now.")
    print("2. take out your knife and sting to the bear's chese.")

    choice = input("> ")

    if choice == "1":
        print("Well done warrior! The bear runs away.")
        congratuation()
    elif choice == "2":
        print("Too slow, the bear finds you alive and scratch you into picecs")
        failure()
    else:
        print("Sorry, you didn't figure out the right choice.")
        failure()

def northern_way():
    print("This is a hard journey, cause northern side is much colder.")
    print("Then you realize that a black mamba snake is around you now.")
    print("What should you do?")
    print("1. hold on and wait for its leave.")
    print("2. fight!")

    while True:
        choice = input("> ")

        if choice == "1":
            print("That is too cold, you have been frozen!")
            failure()
        elif choice == "2":
            fight_with_manba()
        else:
            print("Man, choose 1 or 2.")

def fight_with_manba():
    print("In which way you want to fight?")
    print("1. use feet.")
    print("2. use knife.")

    choice = input("> ")

    if choice == "1":
        print("You successfully step on its joint!")
        print("Mamba is dead.")
        congratuation()
    elif choice == "2":
        print("You successfully cut manba into pieces.")
        print("Hell no! You are poisoned by touching its blood.")
        print("You fall down.")
        failure()
    else:
        print("Man, choose 1 or 2.")    

def mountain():
    print("Here are two orientations.")
    print("1. southern side with many large predator.")
    print("2. northern side with freezing temperature.")
    print("Which one do you want to try?")

    while True:
        choice = input("> ")

        if choice == "1":
            southern_way()
        elif choice == "2":
            northern_way()
        else:
            print("Man, choose 1 or 2.")

def congratuation():
    print("You are a true warrior!")
    print("Good job!")
    exit(0)

def failure():
    print("Sometimes you win and sometimes you don't.")
    print("Restart again! prove you are a ture warrior.")
    exit(0)

def start():
    print("""Dear Dakeke,
    Welcome to the adventure of warrior!
Now you are going to prove you are a ture warrior.
Here are two ways to achieve:
1. explore Atlantis, the deepest ocean region.
2. climb Mount Everest, the highest mountain field.""")
    print("So, which one do you choose?")

    while True:
        choice = input("> ")

        if choice == "1":
            ocean()
        elif choice == "2":
            mountain()
        else:
            print("Man, choose 1 or 2.")

start()

    



    