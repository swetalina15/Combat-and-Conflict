from random import randint
def menu():
    a="*"
    print("\t********")
    print("\tEnter 1 for KORG the fighter")
    print("\tEnter 2 for jack the ripper")
    print("\tEnter 3 for goat skinned")
    print("\tEnter 4 for gula monster")
    print("\tEnter 5 for Bounty Hunter")
    print("\tEnter 6 for undead ghoul")
    print("\tEnter 7 for Zeus's Son")
    print("\tEnter 8 for Night Crawler")
    print("\tEnter 9 for militaristic fighting machine")
def game(n):
    if(n==1):
        print("\n\tchoose stone")
    elif(n==2):
        print("\n\tchoose scissors")
    elif(n==3):
        print("\n\tchoose paper")
    elif(n==4):
        print("\n\tchoose dog")
    elif(n==5):
        print("\n\tchoose human")
    else:
        print("\n\OOPS ,,wrong choice try again")
p=0
c=0
print("\t\t Welcome to CONFLICT and COMBAT") 

choice=True
while(choice):
    p=0
    c=0
    while(p<7 and c<7):
     menu()
     n=0
     k=eval(input("\n\tenter your choice of element--"))
     if(k<4 and k>0):
        game(k)
     else:
        print('wrong choice please enter again')
        continue
     print("\n\tnow computer will choose")
     l=randint(1,5)
     game(l)
     if((k==1 and l==3) or (k==2 and l==1) or (k==3 and l==2)) :
        c+=1
        n=1
     elif(k==l):
        print('\tdraw')
        n=2
     else:
        p+=1
        n=3
        
     if(n==3):
        print("\n\!!!!YOU WON !!!this round")
     elif(n==2):
        print("\n\tthis round is a draw")
     elif(n==1):
        print("\n\tcomputer won this round")

     print("\n\tthe scores are")
     print("\tuser--\t        ",p,"\n\tcomputer--\t",c)
    if(p==5):
        print("\t\tuser won the game")
    elif(p==4):
        print("\t\tuser won the game")
    elif(p==3):
        print("\t\tuser won the game")
    else:
        print("\t\tcomputer won the game")
    print("\t********")
    w=input("do you want to play again(y/n)")
    if(w=='n'):
        choice=False