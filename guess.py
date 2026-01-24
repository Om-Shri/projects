import random

com_choice = random.randint(1,100)

while True:
    try:
        player_choice = int(input("Guess no between (1-100): "))
    

        if player_choice < com_choice :
            print("Low!")
        elif player_choice > com_choice:
            print("High!")
        else:
            print("Congratulations! you guessed it right.")
            break

    except ValueError:
        print("Enter valide no!")