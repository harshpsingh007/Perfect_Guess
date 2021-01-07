import random
from playsound import playsound

computer = random.randint(1,100)
def guess_number(i):
    user_input = int(input("Guess the Number between 1 to 100 \n "))
    if user_input in range(1,100):
        if user_input == computer:
            print(f"Congrats,You won in {i} times ")
            playsound("win_sound.mp3")
        elif user_input > computer:
            print("Enter Lower number Please")
            i += 1
            guess_number(i)
        else:
            print("Enter Higher number Please")
            i += 1
            guess_number(i)
    else:
        print("Invalid Input,Please try Again")
        i += 1
        guess_number(i)

guess_number(1)
