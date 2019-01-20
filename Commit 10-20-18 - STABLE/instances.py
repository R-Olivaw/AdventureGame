# -*- coding: utf-8 -*-

from collections import OrderedDict
import world, items, enemies, npc, dialog, puzzles, utilities
from player import Player


'''
Items
-------------------------------------------------------------------------------
'''
buttered_bread = items.Food("Buttered Bread", 10, 5)
smoked_fish = items.Food("Smoked Fish", 15, 10)
grain_potion = items.HealingPotion("Grain Potion", 30, 15)

pocket_watch = items.Loot("Pocket Watch", "A gold pocket watch.", 15)

magic_disk = items.Quest_Object("Magic Disk", "A glowing magic disk", 0)  

rusty_sheild = items.Sheild("Rusty Sheild", "A rusted sheild with a dent in the middle.", 10, 15)
rusty_helmet = items.Helmet("Rusty Helmet", "The top is rusted out of this helmet.", 5, 7)
moth_eaten_pants = items.Pants("Moth Eaten Pants", "These pants have been eaten by moths", 4, 6)
stained_shirt = items.Torso("Stained Shirt", "A shirt with a red stain.", 2, 4)
crushed_gloves = items.Gauntlets("Crused Gloves", "Some crushed, wrinkled gloved.", 3, 4)
scuffed_boots = items.Boots("Scuffed Boots", "A pair of scuffed up boots", 4, 5)

stone = items.Rock("Stone", "A fist-sized stone.", 5, 0)
rusty_dagger = items.Dagger("Rusty Dagger", "A rusted dagger.", 10, 3)
rusty_sword = items.Sword("Rusty Sword", "A rusted sword.", 15, 5)
flickering_torch = items.Torch("Flickering Torch", "A rag soaked in oil burns on a stick.", 5, 0)

'''
NPCs
-------------------------------------------------------------------------------
'''

alex = npc.Villager('Alexander',
                'male',
                1000,
                [])

alyssa = npc.Villager('Alyssa',
                      'female',
                      1000,
                      [])

mark = npc.Villager('Mark',
                'male',
                80,
                [])

mary = npc.Villager('Mary',
                'trans',
                70,
                [])

randy = npc.Villager('Randy',
                'male',
                80,
                [])

ruth = npc.Villager('Ruth',
                'female',
                80,
                [])

trader_bob = npc.Trader("Bob",
                    100,
                    [buttered_bread,
                     buttered_bread,
                     smoked_fish,
                     grain_potion,
                     scuffed_boots])
    
mayor_steve = npc.QuestGiver("Mayor Steve",
                         10,
                         [buttered_bread,
                          grain_potion,
                          magic_disk])
'''
Enemies
-------------------------------------------------------------------------------
'''
evil_robot = enemies.BasicMonster("Evil Robot",
                                  50,
                                  20,
                                  40)

evil_cow = enemies.BasicMonster("Evil Cow",
                                12,
                                5,
                                0)

dave = enemies.Man("Dave", 100, 30, 0, 0, [buttered_bread, crushed_gloves, moth_eaten_pants, rusty_dagger])

'''
Dialog
-------------------------------------------------------------------------------
'''

sample_dialog = dialog.TestDialog()


'''
Tiles
-------------------------------------------------------------------------------
'''

first_room = world.StartTile(0, 1, "WELCOME HONORED PLAYER!")

one_bot_room = world.SingleEnemyTile(0, 2, evil_robot, "The robot is alive.", "The robot is dead.")

two_bot_room = world.MultiEnemyTile(0, 2, evil_robot, evil_cow, "Robot and cow alive!", "Robot alive, cow dead!", "Robot dead, cow alive!", "BOTH DEAD!")

last_room = world.VictoryTile(0, 3, "YOU HAVE WON CONGRATULATIONS!")

nothing_room = world.EmptyTile(0, 2, "NOTHING HERE DUDE!")

poor_house = world.InhabitedTile(0, 2, [alex, alyssa],
                                 "A little poor house",
                                 sample_dialog)

password_room = world.PuzzleTile(0, -2, puzzle=puzzles.simple_puzzle(),
                                 unsolved_description="What is love?",
                                 solved_description="The room is now empty.",
                                 reward_item=smoked_fish)
'''
Dungeons
-------------------------------------------------------------------------------
'''
'''
Main Map
-------------------------------------------------------------------------------
'''
game_map = OrderedDict()

#The game map is an ordered dictionary. The rooms are described as points on a grid.
##When X incerases, the player moves East.
##When X decreases, the player moves West.
##When Y increases, the player moves North.
##When Y decreases, the player mooves South.
game_map[(0,1)] = first_room
game_map[(0,2)] = poor_house
game_map[(0,3)] = last_room



#This function determines which tile is at which loction. It is utilized from game.py
def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return game_map[(x,y)]
    except KeyError:
        return None

'''
Player
-------------------------------------------------------------------------------
'''

new_player = Player([rusty_dagger, rusty_helmet, moth_eaten_pants, stained_shirt, buttered_bread])