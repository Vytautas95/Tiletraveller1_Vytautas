#The answers:
#1. Which implementation was easier and why?
#A: I found the implementation without functions harder because it was the first time solving the issue and grouping different parts of the program into
#functions was easy when I knew the solution. On the other hand if I had to do it from scratch with functions if would have been harder because I would have to 
#scroll up and down in the code to find errors. This is because I only call the functions at 1 point in the code in this project and therefore it is extra
#work to find where the functions are instead of reading the code line by line.
#2. Which implementation is more readable and why?
#A: The main function is smaller and more readable in the implementation with functions. But that is if you know what the functions do and these are very
#spesific (not the best kind of functions) so if you want to read the code as a whole without knowing the rules of the project the implementation without functions
#would probably be more readable.
#3. Which problems in the first implementations were you able to solve with the latter
#implementation? 
#A: All.
#The algorithm
#1.  Player moves to some direction
#2.  If the direction is a closed wall player stays on same tile and repeats step 1.
#3.  If the direction was valid move to the corresponding tile
#4.  If the new tile is not 3,1 then go back to step 1.
#5.  If the new tile is 3,1 then player wins!
def validpositions(tile):
    """ 
    Finds valid positions for Tile mover in Skilaverkefni 8
    Takes in current position of the game
    """
    if tile == 11 or tile == 21:
        valid_pos = "n"
    elif tile == 12:
        valid_pos = "nes"
    elif tile == 13:
        valid_pos = "es"
    elif tile == 22 or tile == 33:
        valid_pos = "sw"
    elif tile == 23:
        valid_pos = "ew"
    elif tile == 32:
        valid_pos = "ns"
    possible_directions(valid_pos)
    return valid_pos
def possible_directions(valid_positions):
    """ 
    Prints out valid positions to go to
    takes in valid positions in string form in this format: nesw
    Primarly used with validpositions()
    """
    if valid_positions == "n":
        print("You can travel: (N)orth.")
    elif valid_positions == "nes":
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif valid_positions == "es":
        print("You can travel: (E)ast or (S)outh.")
    elif valid_positions == "sw":
        print("You can travel: (S)outh or (W)est.")
    elif valid_positions == "ew":
        print("You can travel: (E)ast or (W)est.")
    elif valid_positions == "ns":
        print("You can travel: (N)orth or (S)outh.")
def tile_change(direction, tile):
    """
    Changes the tile according to what letter was put in a string 
    Takes 2 arguments one for which direction was chosen and one for which tile it is currently located at
    Returns new tile
    """
    lower_direction = direction.lower()
    if lower_direction == "n":
        tile += 1
    elif lower_direction == "s":
        tile -= 1
    elif lower_direction == "e":
        tile += 10
    else:
        tile -= 10
    return tile

position = 11
while position != 31:
    valid_pos = validpositions(position)
    direction = input("Direction: ")
    while direction.lower() not in valid_pos:
        print("Not a valid direction!")
        direction = input("Direction: ")
    position = tile_change(direction, position)
print("Victory!")
