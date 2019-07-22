#!/usr/bin/env python3

"""
File: dice.py
Name: Daniel Staples
Rolls a dice and outputs the result
Concepts covered: Random, printing
"""

import random

def main():
    print("Dice")
    number = random.randint(1,6);
    print("The number was: " + number)
    

if __name__ == "__main__":
    main()