import random

while True:

    secret_num= random.randint(1,100)

    while True:
        guessanynumber = int(input("Guess a number between 1 to 100 : "))

        if guessanynumber > secret_num :
            print("The number is high")

        elif guessanynumber < secret_num :
            print("The number is low")

        else:
            print("Perfect ! you won")
            break