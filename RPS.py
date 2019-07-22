import random
def main():
    while(True):
        rps =  input("Choose r/p/s: ")
        cpu = random.randint(1,3);
        
        if cpu == 1:
            print("the computer chose rock!")
        if cpu == 2:
            print("the computer chose scissors!")     
        if cpu == 3:
            print("the computer chose paper!")        
        
        if rps == "r" and cpu == 1:
            print("You tied!")
        if rps == "r" and cpu == 3:
            print("You lost!")  
        if rps == "r" and cpu == 2:
            print("You Won!")  
        if rps == "p" and cpu == 3:
            print("You tied!")  
        if rps == "p" and cpu == 2:
            print("You lost!")      
        if rps == "p" and cpu == 1:
            print("You Won!")  
        if rps == "s" and cpu == 2:
            print("You tied!")  
        if rps == "s" and cpu == 1:
            print("You lost!")      
        if rps == "s" and cpu == 3:
            print("You Won!")            
        
    
    
if __name__ == "__main__":
    main()
