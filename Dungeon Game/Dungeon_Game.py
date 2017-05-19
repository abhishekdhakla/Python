import os
import random

#draw grid
#pick a random location for player
#pick a random location for exit door
#pick a random location for the montser
#draw a player in the grid
#take input for movement
#move player, unless invalud move (past edges of grid)
#check for win/loss
#clear screen and redraw grid


CELLS = [ (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
          (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
          (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
          (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
          (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_locations():
    return random.sample(CELLS, 3)
    

def move_player(player, move):
    # get the player's location
    x, y = player
    # if move == LEFT, x-1
    if move == 'LEFT':
        x -= 1
    # if move == RIGHT, x+1
    if move == 'RIGHT':
        x += 1
    # if move == UP, y-1
    if move == 'UP':
        y -=1 
    # if move == DOWN, y+1
    if move == 'DOWN':
        y += 1
    return x, y

def get_moves(player):
    moves = ["UP", "DOWN", "LEFT", "RIGHT"]
    x, y = player
    #if players' y == 0, they cannot move UP
    if y == 0:
        moves.remove("UP")
    #if player's y == 4, they cannot move DOWN
    if y == 4:
        moves.remove("DOWN")
    #if player's x == 0, they cannot move LEFT
    if x == 0:
        moves.remove("LEFT")
    #if player's x == 4, they cannot move RIGHT
    if x == 4:
        moves.remove("RIGHT")
    return moves


monster, door, player = get_locations()

while True:
    valid_moves = get_moves(player)
    clear_screen()
    print("Welcome to Dungeon!")
    print("You are currently in room {}".format(player)) #Fill with player position
    print("You can move {}".format(", ".join(valid_moves))) # Fill with available moves
    print("Enter QUIT to quit")
    
    move = input("> ")
    move = move.upper()
    
    if move == 'QUIT':
        break
    
    if move in valid_moves:
        player = move_player(player, move)
        
    else:
        print("\n** Walls are hard, don't run into them, LMAO!! **\n")
        continue
        
    #good move? change the players position
    #bad move? Don't change anything
    #On the door? They win!
    #On the monster? They lose!
    #Otherwise, loop back again :)
