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


def get_locations():
    monster = None
    door = None
    player = None
    
    return monster, door, player

while True:
    print("Welcome to Dungeon!")
    print("You are currently in room {}" ) #Fill with player position
    print("You can move {}") # Fill with available moves
    print("Enter QUIT to quit")
    
    move = input("> ")
    move = move.upper()
    
    if move == 'QUIT':
        break
        
    #good move? change the players position
    #bad move? Don't change anything
    #On the door?
