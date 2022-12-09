import random
print("RULE TO PLAY THIS GAME:\n1) YOU WILL GET ONLY NINE CHANCES TO GUESS\n2) IF YOU TRIED CHEATING(LIKE MESSING UP WITH CODE YOU WILL BE DISQUALIFIED)")
while(True):
    while True:
            i=1
            difficulty=(input("enter the difficulty(easy,medium,hard): "))
            difficulty=difficulty.lower()
            if difficulty=="easy":
                number=random.randint(0,100)
                attempts=12
                break
            elif difficulty=="medium":
                number=random.randint(0,200)
                attempts=9
                break
            elif difficulty=="hard":
                number=random.randint(0,500)
                attempts=7
                break
            else:
                print("please enter valid input")
    while i<=attempts:
        try:
            value=int(input("enter the number: "))
            break
        except Exception as e:
            print("You loose one attempt for invalid input")
            i=i+1
    if i>=attempts:
        print("Unfortunately you lost")
        print("enter 1 to try again or any other key to exit: ")
        repeater=input()
        if repeater=="1":
            continue
        else :
            break           
    while(value!=number):
        if value>number:
            try:
                value=int(input("Try a smaller number: "))
            except Exception as e:
                print("You loose one attempt for invalid input")
                i=i+1
        elif value<number:
            try:
                value=int(input("Try a larger value: "))
            except Exception as e:
                print("You loose one attempt for invalid input")
                i=i+1
        i=i+1
        if i>=attempts:
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
