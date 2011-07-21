from mineraffair.world import World
from mineraffair.player import Player

def play():
    world = World()
    player = Player(world, "Bob")


    while True:
        text = raw_input("Your command? ")

        if text == 'quit':
            break
        else:
            player.do(text)
