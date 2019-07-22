def main():
    word = input("Enter a word: ")
    
    pali = ''.join(reversed(word))
    print(pali)
    
    if pali == word:
        print("It is a palindrome.")
    else:
        print("It's not a palindrome.")
    

if __name__ == "__main__":
    main()
