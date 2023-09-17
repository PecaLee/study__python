from random import randint

checker = True

while checker:
    try:
        user_choice = int(input("Choose number. : "))
        pc_choice = randint(1,50)

        if user_choice == pc_choice:
            print("Draw.")
        elif user_choice > pc_choice:
            checker = False
            print("You Win!")
        else:
            print(f"You lose, computer chose {pc_choice}.")
    except ValueError:
        print("retry.")