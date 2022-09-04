# guess number 1 to 100 GAME
def main():
    import random 
    number = random.randrange(1,100)
    guess = 0
    

    while number != guess:
        guess = int(input("Guess the number: "))

        if guess > number:
            print("The number is less than your guess")
            continue
        elif guess < number:
            print("The number is more than your guess")
            continue
        else:
            print("You Win!!", number)


main()
