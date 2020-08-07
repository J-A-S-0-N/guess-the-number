import random 
from os import system

def rand():
    global randnumber
    randnumber = random.randint(0,10)

def main():
    guessing = False
    rand()
    while True:
        print("enter an number that is from 0 to 10")
        inp = input(">> ")
        if randnumber == int(inp):
            guessing = True
            system("cls")
            print("you guessed it right it was " + str(inp))
            
        if guessing ==  True:
            break
        system("cls")

if __name__ == "__main__":main()