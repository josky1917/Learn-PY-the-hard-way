def print_two(*args):##asterisk arguments which means more args than one
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}.")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothing.")

print_two("Jie","Zhu")
print_two_again("Yang","Ke")
print_one("First!")
print_none()