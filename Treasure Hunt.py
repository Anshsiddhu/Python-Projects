print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are on a scary island")
reply1 = input("Do you want to continue the mission now also , then type Y")

if reply1 == "Y":
    reply2 = input('''Will you go inside the scary Mansion or in the good looking Mansion
    (scary Mansion = Y and Good looking Mansion = N ):''')
    if reply2 == "N":
        print("Welcome to Mansion said by a tall person")
        reply3 = input('''Will you ask him about treasure or you will just escape from there
        (to escape type = escape and to ask type = ask''')
        if reply3 == "escape":
            print("You escaped from there")
            reply4 = input('''There are three doors before you a blue door....(Door of ocean) , 
            a yellow door(Heaven's Door).... and a red door....(Devil's Door)(type the colour of door you choose) ''')
            if reply4 == "blue":
                print("Every where is gold and only gold")
                print('Oh you fell sleep')
                print("Now , you are on a pirate's ship")
                reply5 = input("Will you ask him about treasure map or not (to ask type ask)")
                if reply5 == "ask":
                    print("He killed you and take away your treasure map")
                    print("You are in a heaven")
                    exit()
                else:
                    print("you escaped but you don't know swiming")
                    print("you drown")
            else:
                print('You died you fall from a peak of mountain')
                print('It was just a dreammmmmmmmm....................')
                reply6 = input("You are in a plane , you are pushed out of the plane")



        else:
            print("He said that he don't know about any treasure!")
            print('''But now he wants 50% treasure
            He gonna come with you ''')
            exit()
    else:
        print("YOU ARE KILLED BY A GHOST...........")
        print("GAME OVER")
        exit()
else:
    print("YOO ARE KILLED BY A BIGFOOT YOU CAN'T ESCAPED")
    exit()