print("Which file do you want to open?")
filename = input("> ")
text = open(filename)

print("Here is the content:")
print(text.read())

text.close()

text = open(filename, "w")
print("Now we are going to truncate it.")
text.truncate()

print("Mission complete")
text.close()