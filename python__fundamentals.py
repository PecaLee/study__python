print("Hello world!")

# Variables
a = 2
b = 3
c = a + b
c = 1

print(c)

# Booleans and Strings
my_name = "peca"
print(my_name)

true_Boolean = True
false_Boolean = False

# Function
def say_hello():
    print("hello how r u?")

say_hello()

# Parameters
def print_human_age(name,age):
    print(name,age)

print_human_age("peca", 13)

# Default Parameters
def default_parameters(user_name="anonymous"):
    print("Hello", user_name)

default_parameters()
default_parameters("peca")
