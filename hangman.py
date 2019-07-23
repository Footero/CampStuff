import random
import sys

def main():
    print("Welcome to hangman!")
    tries = 10;
    win = 0
    l1 = '_'
    l2 = '_'
    l3 = '_'
    l4 = '_'
    l5 = '_'    
    while(tries > 0 and win < 1):
        
        guess = input("Guess a letter: ")
        
        if guess == 'h':
            print("You got a letter!")
            l1 = 'h'
        elif guess == 'a':
            print("You got a letter!")
            l2 = 'a' 
        elif guess == 'p':
            print("You got 2 letters!")
            l3 = 'p' 
            l4 = 'p' 
        elif guess == 'y':
            print("You got a letter!")
            l5 = 'y'         
        else:
            tries = tries - 1
            print("You didn't guess a letter! You have " + str(tries) + " tries remaining")
            
        if l1 == 'h' and l2 == 'a' and l3 == 'p' and l4 == 'p' and l5 == 'y':
            print("You guessed the word!")
            win = 10
            
        print("The word is: " + l1 + l2 + l3 + l4 + l5)
    if tries == 0:
        print("You loose! The word was HAPPY.")
    
    
    

if __name__ == "__main__":
    main()
