from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here is your {filename}:")
print(txt.read())##read the file content

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again) 
##txt_again is not the content of file but an object
print(f"Here is the {file_again}:")
print(txt_again.read()) ##use .read() to get content of object