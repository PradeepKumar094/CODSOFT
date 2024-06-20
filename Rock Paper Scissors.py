import random
GameList=['Rock','Paper','Scissors']
D={'R':'Rock','P':'Paper','S':'Scissors'}
co=0
pl=0
key=0
print("Score: Player ",pl," Computer ",co)
run=True
while run:
    comp_choice=random.choice(GameList)
    key=input("Enter\n R for Rock\n P for Paper\n S for scissors:")
    key=D[key.upper()]
    if(key==comp_choice):
        print("Tie")
    elif key=='Paper':
        if comp_choice == "Rock":
            print("player won!")
            pl+=1
        else:
            print("Computer won!")
            co+=1
    elif key=='Rock':
        if comp_choice == "Scissors":
            print("player won!")
            pl+=1
        else:
            print("Computer won!")
            co+=1
    elif key=="Scissors":
        if comp_choice=="Paper":
            print("player won!")
            pl+=1
        else:
            print("Computer won!")
            co+=1
    else:
        print("Wrong input")
    a=int(input("Enter 1 to play again 0 to stop"))
    if a==1:
        run=True
    else:
        run=False
    print("Player: "+ key)
    print("computer: "+comp_choice)
    print("Score: Player ",pl," Computer ",co)
