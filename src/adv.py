from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

name = input("\nWhat is your name, Adventurer?")
player = Player(name, room['outside'])
print(f"\nWelcome to the game, {player.name}.")


# Write a loop that:

game_is_playing = True

while game_is_playing:
#
# * Prints the current room name
    print(f"\nYou are currently {player.current_room.name}")

# * Prints the current description (the textwrap module might be useful here).
    print(f"{player.current_room.description}.")

# * Waits for user input and decides what to do.
# Print an error message if the movement isn't allowed.
# If the user enters "q", quit the game.

    player_input = input(f"\nWhich direction would you like to go, {player.name}?  \nYou can choose north, east, south, or west (n, e, s, w)").lower().strip()
    
    if player_input == "north": 
        player_input = "n"
    elif player_input == "south":
        player_input == "s"
    elif player_input == "west":
        player_input == "w"
    elif player_input == "east":
        player_input == "e"
    elif player_input == "q":
        game_is_playing = False
        print("Your adventure has ended.")
    else:
        print("Please choose a valid direction.")
    print(player_input)

# If the user enters a cardinal direction, attempt to move to the room there.
    cardinal_direction = ["n", "e", "s", "w"]

else:
    game_is_playing = False
