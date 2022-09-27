# guess number 1 to 100 game


def main():
    print("Guess the number from 1 to 100")
    import random 
    number = random.randrange(1, 100)
    guess = 0
    my_loop(number, guess)


def my_loop(number, guess):

    while number != guess:
        guess = int(input("Guess the number: "))

        if guess > number:
            print(f"The number is less than: {guess}")
            continue
        elif guess < number:
            print(f"The number is more than: {guess}")
            continue
        else:
            print("You Win!!", number)
            x = input("Play again? y or n\n").lower()
            if x == "y" or x == "yes":
                main()
            else:
                print("Hope you had fun!")



main()
