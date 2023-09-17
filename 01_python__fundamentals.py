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

# Retrun Values
def return_values(prize, devide_winner):
    return prize / devide_winner

print(return_values(100,2))

# Format String
my_name = "peca"
my_age = 37

format_string = f"Hello I'm {my_name}, I have {my_age} years old."
print(format_string)