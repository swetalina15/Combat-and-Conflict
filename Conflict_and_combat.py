# import system from os 
from os import system 
# import colorama for text colour
import colorama  
# import sleep to show output for some time period 
from time import sleep 
# define our clear function
from random import randint
# to generate random choice 
# define our clear function
def clear(): 
        _ = system('cls') 
#funtion for our introduction
name='' 
playerscore=computerscore=0
def intro():
    clear()
    global name
    print("\n\n\n\n\n")
    print("\t\t\t **-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**")
    print("\t\t\t    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("\t\t\t\t\t       = WELCOME =")
    print("\t\t\t\t\t         = TO =")
    print("\t\t\t\t\t = CONFLICT AND COMBAT =")
    print("\t\t\t		.......Developed by....... ")
    print("\t\t\t	    .......Sidhartha Parasramka.......")
    print("\t\t\t	    ..........Soumya Agrawal..........")
    print("\t\t\t	    ..........Swetalina Nayak.........")
    print("\t\t\t   =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("\t\t\t **-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**")
    print("\n\n\n\t\t\t Game Will Start In few seconds")
    print("\n\n\n\t\t\tMeanwhile You can Enter Your Name:-",end='')
    name=input()
    sleep(2)
#Exception for Wrong Selection of warriors
class WrongSelectionException(Exception):
        def __init__(self):
            print('ERROR: Invalid Selection of Number Of warriors')
#Exception for selecting less number of Warriors
class LessWarriorsError(Exception):
    def __init__(self):
        print("ERROR: Less Number Of Warriors Selected or Repetative Selection ")
def heading():
    with open('heading.txt',encoding="utf8") as f:
        print(f.read())
#funtion to print the rules from the text file
def txt(a):
    heading()
    f=open(a,'r',encoding="utf8")
    data=f.read()
    print(data)
    f.close()
intro()
clear()
txt('introduction.txt')
print("\n\n\n\tPRESS ENTER KEY TO CONTINUE:--",end='')
input()
numberElements=(3,5,7,9)
# If using Windows, init() will cause anything sent to stdout or stderr
# will have ANSI color codes converted to the Windows versions. Hooray!
# If you are already using an ANSI compliant shell, it won't do anything
colorama.init()


# Now regular ANSI codes should work, even in Windows

RED = '\033[31m'   # mode 31 = red forground
RESET = '\033[0m'  # mode 0  = reset
while True:
    clear()
    heading()
    try:
        print("\n\t\tYou can have either 3,5,7 or 9 Warriors in the pool")
        Element=int(input("\n\t\tCaution!!!- Wrong input will result in Exception\n\t\tEnter The Number Of Warriors In The Game "))
        print("\t\tselected input: "+RED + str(Element) + RESET)
        if(Element not in numberElements):
            raise WrongSelectionException
    except WrongSelectionException:
        print("\n\tINVALID SELECTION!!\n\t Press Enter to input again")
        input()
    except ValueError as msg:
        print("\t\t ERROR:",msg,"\n\tINVALID SELECTION!!\n\t Press Enter to input again")
        input()
    else:
        break    

print("\n\t\t Game will Procede in 2 seconds")
sleep(2)
clear()
txt('gamedata.txt')
print("\n\tPRESS ENTER TO START PLAYING THE GAME:--",end='')
input()
clear()
winloosemat=((0,1,-1,1,-1,1,-1,1,-1),(-1,0,1,1,-1,1,-1,1,-1),(1,-1,0,-1,1,-1,1,-1,1),(-1,-1,1,0,1,-1,1,-1,1),(1,1,-1,-1,0,-1,1,-1,1),(-1,-1,1,1,1,0,1,-1,-1),(1,-1,1,-1,-1,-1,0,1,1),(-1,-1,1,1,1,1,-1,0,-1),(1,1,-1,-1,-1,1,-1,1,0))
Twarriors=("KORG The Fighter","Jack The Ripper","Goat Skinned"," Gula monster","Bounty Hunter","Undead Ghoul","Zeus's Son","Night Crawler","Militaristic Fighting Machine")
comments=(" magnetised","Poisoned" ,"Dismantled","Vaporised","Decapitated","Shattered","Swallows","Crushed","Frightens")
while(True):
    clear()
    print("\t\t--Form Your POOL of the Warriors--")
    print("\n\n\t",'*'*50)
    print("\t\tEnter 1 for KORG The Fighter")
    print("\t\tEnter 2 for Jack The Ripper")
    print("\t\tEnter 3 for Goat Skinned")
    print("\t\tEnter 4 for  Gula monster")
    print("\t\tEnter 5 for Bounty Hunter")
    print("\t\tEnter 6 for Undead Ghoul")
    print("\t\tEnter 7 for Zeus's Son")
    print("\t\tEnter 8 for Night Crawler")
    print("\t\tEnter 9 for Militaristic Fighting Machine")
    print("\n\t",'*'*50)
    print("\n\t\tREPETATION OF SAME WARRIORS NOT ALLOWED!!")
    Pwarriors={}
    for i in range(Element):
        print("\t\tEnter your ",i+1,"th warrior:",end='')
        a=int(input())
        Pwarriors[a-1]=Twarriors[a-1]
    try:
        if(len(Pwarriors)<Element):
            raise LessWarriorsError
    except LessWarriorsError:
        input("\n\tINVALID SELECTION!!\n\tEnter the WARRIORS again")
        continue
    reset=input("\t\tAre you happy With the pool??(yes/no): ")
    if reset=='yes' or reset=='YES'or reset=="Yes":
        print("\n\t\t let's proceed")
        break

clear()
print("\n",'*'*50)
print('\t\tselcted warriors are:')
k=1
for i in Pwarriors.keys():
    print('\t\t',k,'th warrior:  '+RED + Pwarriors[i]+RESET)
    k=k+1
print("\n",'*'*50)
input("\n\t\tPRESS ENTER TO CONTINUE")
clear()
heading()
print("\n\t\t\t\tBATTLE BEGINS! ")
print("\t\tEach Battle will Have five rounds of combact")
print("\t\tThe player and the computer will have warriors of their choice from the pool")
print("\t\tPlayer will have to choose warriors for each combat")
print("\n\n\t\t\t\t !!!FIGHT IN |3| SECONDS!!!")
sleep(3)

index=list(Pwarriors.keys())
j=0
while(j<5):
    clear()
    heading()
    print("\n\n\t\t\t\t--Pool--")
    k=1
    for i in Pwarriors.keys():
            print('\t\twarrior number',k,' :  '+RED + Pwarriors[i]+RESET)
            k=k+1
    SelectedWarrior=int(input("\n\t\tEnter Your warrior For the Combact:"))
    SelectedWarrior=index[SelectedWarrior-1]
    print("\t\tYOUR WARRIOR:---",Pwarriors[SelectedWarrior])
    compWarrior=randint(0,Element-1)
    compWarrior=index[compWarrior]
    print("\t\tcomputer chose:---",Pwarriors[compWarrior])
    cscore=winloosemat[SelectedWarrior][compWarrior]
    phrase=comments[randint(0,8)]
    sleep(3)
    clear()
    txt(str(randint(1,5))+'.txt')
    print("\n",'*'*50)
    if(cscore==1):
        print(Pwarriors[SelectedWarrior],phrase,Pwarriors[compWarrior])
        print("\n\t\tWOAHH YOU WON!!!")
        playerscore+=1
    elif(cscore==-1):
           print(Pwarriors[compWarrior],phrase,Pwarriors[SelectedWarrior])
           print("\t\tAww The Computer Won")
           computerscore+=1
    else:
        print("\n\t\tLOOKS LIKE IT'S A DRAWWW!!!")
    
    print("\tSCORES OF THE BATTLES")
    print("\tuser--\t        ",playerscore,"\n\tcomputer--\t",computerscore)
    print("\n",'*'*50)
    j+=1
    if(j<5):
        print("Press Enter for round number",j+1, "OF COMBAT",end='')
        input()
    else:
        input("Press Enter to SEE the winner of the showdown")
print("\n",'*'*50)
if(computerscore<playerscore):
    txt('asc.txt')
    print("\n\n\n\t\tAND IT'S A WINNNN.",name,"WON THE ",playerscore,"COMBATS OUT OF 5")
else:
    txt("loosee.txt")
    print("""\n\n\n\t\t\t\tOOPS BETTER LUCK NEXT TIME "-" """)
    
again=input("\t\t\tFEEL LIKE PLAYING AND TESTING THE ODDS AGAIN?(YES/NO)")
if(again=="no" or again=="NO" or again=="No"):
    print("\t\tTHANKYOU FOR YOUR TIME")
else:
    clear()
    txt("end.txt")
    print("\t\t\tyou can always re-execute it again ¯")
    