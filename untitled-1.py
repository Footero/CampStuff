import random
def main():
    print("guess the number.")
    answer = random.randint(1,100);
    tries = 10;
    while (tries > 0):
        guess = int(input("guess a number: "))
        if answer == guess:
            print("yes")
            break
        else:
            if guess > answer:
                print("Too high!")
            if guess < answer:
                print("Too low!")
            tries = tries - 1;
            print("You have " + str(tries) + " tries left")
    if tries == 0:
        print("you lose")
        print("the number was " + str(answer))
if __name__ == "__main__":
    main()