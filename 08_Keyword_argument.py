# Keyword Arguments
def say_hello(age, name = "anonymous"):
    print(f"name : {name}, age : {age}")

say_hello(12)
say_hello(name=14,age=12)