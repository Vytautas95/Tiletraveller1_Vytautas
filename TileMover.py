#The algorithm
#1.  Player moves to some direction
#2.  If the direction is a closed wall player stays on same tile and repeats step 1.
#3.  If the direction was valid move to the corresponding tile
#4.  If the new tile is not 3,1 then go back to step 1.
#5.  If the new tile is 3,1 then player wins!

position = 11
while position != 31:
    if position == 11 or position == 21:
        validpos = "n"
    elif position == 12:
        validpos = "nes"
    elif position == 13:
        validpos = "es"
    elif position == 22 or position == 33:
        validpos = "sw"
    elif position == 23:
        validpos = "ew"
    elif position == 32:
        validpos = "ns"
    if validpos == "n":
        print("You can travel: (N)orth.")
    elif validpos == "nes":
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif validpos == "es":
        print("You can travel: (E)ast or (S)outh.")
    elif validpos == "sw":
        print("You can travel: (S)outh or (W)est.")
    elif validpos == "ew":
        print("You can travel: (E)ast or (W)est.")
    elif validpos == "ns":
        print("You can travel: (N)orth or (S)outh.")
    direction = input("Direction: ")
    direction = direction.lower()
    while direction not in validpos:
        print("Not a valid direction!")
        direction = input("Direction: ")
    if direction in validpos:
        if direction == "n":
            position += 1
        elif direction == "s":
            position -= 1
        elif direction == "e":
            position += 10
        else:
            position -= 10
print("Victory!")



