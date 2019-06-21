from sys import argv
script, text = argv

file = open(text, "w")
print("tell something")
file.write(f"{input('>')}")
file.close()