
import random
def main():
    print("Dice")
    range = int(input("how many sides: "))
    while(True):
        number = random.randint(1,range);
        print("The number you rolled was: " + str(number))
        NUM = input("Roll again? Press enter.")
if __name__ == "__main__":
    main()
