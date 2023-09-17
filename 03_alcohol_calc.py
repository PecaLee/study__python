try:
    age = int(input("How old are you?"))
    if age < 18:
        print("You can't drink.")
    elif age >=18 and age <= 20:
        print("OK, Go ahead.")
    elif age == 40 or age == 30:
        print("good!")
    else:
        print("Go ahead")
except ValueError:
    print("try again")