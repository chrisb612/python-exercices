import random

r = 42

def main():
    #print("Try to guess the number")
    # cli(rdmNum())
    comp_guess()
    
def rdmNum():
    return random.randrange(1, 100)

def rdmComputer(min: int, max: int) -> int:
    return round((min + max) / 2)
    # return random.randrange(min, max)
    
def decimal_to_bin(n: int) -> str:
    return bin(n).replace("0b", "")

    
def bin_to_decimal(s: str) -> int:
    return int(s, 2)    
    
def comp_guess():
    correct = ["+", "-", "="]

    found = False
    n, min, max = 0, 1, 100
    while(1):
        guessable_str: str = input("What number to guess ? ")
        try:
            guessable = int(guessable_str, 2)
            break
        except: 
            print("invalid input !")
            
    while not found and n < 7:
        n +=1
        choice = rdmComputer(min, max)
        print(f"Computer choice : {decimal_to_bin(choice)}")
        while 1:
            answer: str =  input("Answer : ")
            if answer in correct:
                break
            else:
                print("Invalid input !")
        
        if answer == "+":
            if (choice >= guessable):
                print("CHEATER !")
                n= 0
                found = True
            min = choice
        elif answer == "-":
            if (choice <= guessable):
                print("CHEATER !")
                found = True
                n = 0
            max = choice
        elif answer == "=":
            if (choice != guessable):
                print("CHEATER !")
                found = True
                n = 0
            found = True
    if (found == True ):
        print("Computer won")
    else:
        print("Computer is bad at guessing")
        

def cli(r):
    n=0
    result = False
    while(n<=7 and not result):
        n+=1
        value = input("Input: ")
        try:
            intValue = int(value)
        except:
            print("invalid input !")
            n-=1
            continue
            
        if intValue == r:
            result = True
        elif intValue > r: 
            print("-")
        elif intValue < r:
            print("+")
    
    if result:
        print(f"GG ! You find the answer trying {n} times.")
    else:
        print("You just lost, u noob !")
    
main()