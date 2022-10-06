import random


valid = ["pierre", "feuille", "ciseaux"]

def main():
    human_choice: str = input("Ton choix ?  ")
    if not validate(human_choice):
        human_choice = rdmChoice()
        print("Je décide pour toi: ")
    print("Humain: " + human_choice)
    computer_choice = rdmChoice()
    print("Computer: " + computer_choice)
    w: int = human_winner(human_choice, computer_choice)
    if w == 0:
        print("Winner : Computer")
    elif w == 1:
        print("Winner : Human")
    else:
        print("Winner : None")
    
def human_winner(h: str, c: str) -> int:
    if (h.lower() == "pierre" and c.lower() == "ciseaux") or (h.lower() == "ciseaux" and c.lower() == "feuille") or (h.lower() == "feuille" and c.lower() == "pierre"): 
        return 1
    elif (h.lower() == c.lower()):
        return 2
    else:
        return 0
    
    
def validate(c: str) -> bool:
    if c.lower() in valid:
        return True
    else:
        return False 
    
def rdmChoice() -> str:
    return valid[random.randrange(0, len(valid) -1)]

    
main()