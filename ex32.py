the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for fruit in the_count:
    print(f"This is count {fruit}")

#same as above
for x in fruits:
    print(f"A fruit of type: {x}")

# also we can go through mixed list too
for i in change:
    print(f"I got {i}")

#we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0, 3):
    print(f"Adding {i+1} to the list.")
    # append is a function that lists understand
    elements.append(i+1)

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")