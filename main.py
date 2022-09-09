from random import randint


def guess_the_number():
    guess = 0
    secret_number = randint(1, 100)
    print(secret_number)
    while guess != secret_number:
        try:
            guess = int(input("Guess the number:"))
        except ValueError:
            print("It's not number")
            continue
        if guess < secret_number:
            print("Too small")
        elif guess > secret_number:
            print("Too big")
    print("You won")


guess_the_number()




