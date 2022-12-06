import random
i=0
difficulty=(input("enter the difficulty(easy,medium,hard): "))
difficulty=difficulty.lower()
if difficulty=="easy":
    number=random.randint(0,100)
elif difficulty=="medium":
    number=random.randint(0,200)
elif difficulty=="hard":
    number=random.randint(0,500)
while(True):
    value=int(input("enter the number: "))
    while(value!=number):
        if value>number:
            value=int(input("Try a smaller number: "))
        elif value<number:
            value=int(input("Try a larger value: "))
        i=i+1
    print("Booooooom You guessed it correct in",i,"turns\n\t enter 1 if you want to continue else enter any other key to exit: ")
    repeater=input()
    if repeater=="1":
        continue
    else :
        break
