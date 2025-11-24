import random
print("Welcome to Guess the no. game!!!")
print("Rules:")
print("1. There will be 3 levels of difficulty")
print("2. Level 1: You will get 2 Chances to guess the correct number between 1 and 5")
print("3. Level 2: You will get 3 Chances to guess the correct number between 1 and 10")
print("4. Level 3: You will get 5 Chances to guess the correct number between 1 and 20")
def lvlone():
    number = random.randint(1,5)
    print("Welcome to Level 1")
    print("Here you will get 2 chances")
    for i in range(2):
        guessed = int(input("Guess the number: "))
        if guessed == number:
            print("Computer chose: ", number)
            print("YOu chose: ", guessed)
            print("You Won!!!")
            break
        else:
            
            print("Better Luck Next Time!!!")
            if i==1:
                print("Computer chose: ", number)

def lvltwo():
    number2 = random.randint(1,10)
    print("Welcome to Level 2")
    print("Here you will get 3 chances")
    for i in range(3):
        guessed = int(input("Guess the number: "))
        if guessed == number2:
            print("Computer chose: ", number2)
            print("YOu chose: ", guessed)
            print("You Won!!!")
            break
        else:
            
            print("Better Luck Next Time!!!")
            if i==2:
                print("Computer chose: ", number2)

def lvlthree():
    number3 = random.randint(1,20)
    print("Welcome to Level 3")
    print("Here you will get 5 chances")
    for i in range(5):
        guessed = int(input("Guess the number: "))
        if guessed == number3:
            print("Computer chose: ", number3)
            print("YOu chose: ", guessed)
            print("You Won!!!")
            break
        else:
            
            print("Better Luck Next Time!!!")
            if i==4:
                print("Computer chose: ", number3)

print()
print()
print()

while True:
    print("1. Start Level 1")
    print("2. Start Level 2")
    print("3. Start Level 3")
    print("4. Leave the Game")
    print()
    print()
    choice = int(input("Enter your choice[1/2/3]: "))
    if choice==1:
        lvlone()
    elif choice==2:
        lvltwo()
    elif choice==3:
        lvlthree()
    elif choice==4:
        print("Game Over......")
        break
    else:
        ask = int(input("GO TO MAIN MENU?[y/n]: "))
        if ask.lower()=="y":
            continue
        else:
            break