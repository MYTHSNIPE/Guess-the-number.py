import random
print("RULE TO PLAY THIS GAME:\n1) YOU WILL GET ONLY NINE CHANCES TO GUESS\n2) IF YOU TRIED CHEATING(LIKE MESSING UP WITH CODE YOU WILL BE DISQUALIFIED)")
while(True):
    i=1
    difficulty=(input("enter the difficulty(easy,medium,hard): "))
    difficulty=difficulty.lower()
    if difficulty=="easy":
        number=random.randint(0,100)
        attempts=12
    elif difficulty=="medium":
        number=random.randint(0,200)
        attempts=9
    elif difficulty=="hard":
        number=random.randint(0,500)
        attempts=7
    value=int(input("enter the number: "))
    while(value!=number):
        if value>number:
            value=int(input("Try a smaller number: "))
        elif value<number:
            value=int(input("Try a larger value: "))
        i=i+1
        if i==attempts:
            print("Unfortunately you lost :( ")
            break
    if i!=attempts:
        print("Booooooom You guessed it correct in",i,"turns\n\t enter 1 if you want to continue else enter any other key to exit: ")
        repeater=input()
        if repeater=="1":
            continue
        else :
            break
    else:
        print("enter 1 to try again or any other key to exit: ")
        repeater=input()
        if repeater=="1":
            continue
        else :
            break
