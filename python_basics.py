some_string = "Hello Python"
print(some_string)

firstname = "Monty"
lastname = "Python"

# To print Monty Python
print(firstname + " " + lastname)

# Can use f string to print
print(f"My name is {firstname} {lastname})

# Can use .format() to print
print("My name is {} {}".format(firstname, lastname))

# str() returns a string object
# int() returns an integer object
# float() returns a floating point object
# bool() returns a boolean value of True or False

# DICTIONARIES
# dict = {"key": "value"}
user = {"firstname": "Monty"}
print(user)

# To read the value associated with a key
print(user["firstname"])

# To add a key:value pair
user["lastname"] = "Python"
print(user) # Output would be {'firstname': "Monty', 'lastname': 'Python'}

# Delete a key-value pair
del user["lastname"]

# LISTS
# Create a list
fruit = ["apples", "oranges", "pears"]

# Read a certain index
print(fruit[1]) # Output would be oranges

# Get the length of a list
len(fruit)

# Add item to end of a list
fruit.append("grapes") #Output would be ['apples', 'oranges', 'pears', 'grapes']

# Add item to specific point in list
fruit.insert(2, "grapes") # Output would be ['apples', 'oranges', 'grapes', 'pears']

# Sort list temporarily
print(sorted(fruit))

# Sort list permanently
print(fruit.sort())

# Reverse order of list
print(fruit.reverse())

# Delete items from a list using index permanently
del fruit[1]

# Delete items from a list temporarily
print(fave_fruit = fruit.pop())

# To determine type of object
print(type(variable_name))

# FUNCTIONS
# A function to return hello world
def hello_world():
    return 'hello world'

# Assign the function to a variable
greeting = hello_world()
print(greeting) # Output would be 'hello world'

