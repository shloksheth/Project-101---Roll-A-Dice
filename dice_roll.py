import random
rollornot = "not set"

if input("Do you want to roll a dice? Enter y/n:   ") == "y":
    rollornot = "Yes"
elif input("Do you want to roll a dice? Enter y/n:   ") == "n":
    rollornot = "No"
   
while rollornot != "No":  
    if rollornot == "Yes" :
        dice_roll = random.randint(1,6)

    if dice_roll == 1 :
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")

    if dice_roll == 2 :
        print("[-----]")
        print("[     ]")
        print("[ 0 0 ]")
        print("[     ]")
        print("[-----]")

    if dice_roll == 3 :
        print("[-----]")
        print("[0    ]")
        print("[  0  ]")
        print("[    0]")
        print("[-----]")

    if dice_roll == 4 :
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")

    if dice_roll == 5 :
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
        
    if dice_roll == 6 :
        print("[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]")

    if input("Do you want to roll a dice again? Enter y to roll and n to exit:   ") == "y":
        rollornot = "Yes"
    elif input("Do you want to roll a dice again? Enter y to roll and n to exit:   ") == "n":
        rollornot = "No"
