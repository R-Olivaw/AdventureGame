from collections import OrderedDict
import random
import world, items, enemies, npc, puzzles, utilities
from player import Player

'''
Items
-------------------------------------------------------------------------------
'''

#Consumables
health_potion = items.HealingPotion("Health Potion", 20, 9)
dank_potion = items.HealingPotion("Dank Potion", 42, 0)
sandwich = items.Food("Sandwich", 15, 5)

#Armor
rusty_dagger = items.Sword("Rusty Dagger", "A blunt dagger covered in rust\n", 5, 0)
rusty_knife = items.Dagger("Rusty Knife", "It will give you tetnis", 3, 0) 
silver_sword = items.Sword("Silver Sword", "A gleaming silver sword\n", 15, 10)
cool_sword = items.Sword("Cool Sword", "A pretty cool sword", 4, 1)    
shit_helmet = items.Helmet("Shit helmet", "A shitty helmet", 1, 0)                
rusty_helmet = items.Helmet("Rusty Helmet", "A rusty ass helmet", 4, 0)   
bronze_helmet = items.Helmet("Bronze Helmet", "A shiny helmet\n", 5, 2)
bronze_chest = items.Chest("Bronze Chest Plate", "A shiny chest plate\n", 10, 5)
rusty_chest_plate = items.Chest("Rusty Chest Plate", "Not good armor", 3, 0)
bronze_shield = items.Sheild("Bronze Shield", "A shiny shield\n", 10, 5)
broken_sheild = items.Sheild("Broken Sheild", "Busted ass shield", 2, 0)
bronze_boots = items.Boots("Bronze Boots", "Shiny boots\n", 5, 2)
shit_boots = items.Boots("Shit boots", "Shitty boots", 1, 0)
leather_boots = items.Boots("Leather boots", "Worn out boots", 2, 0)
cotton_pants = items.Pants("Cotton Pants", "Plain pants", 0, 0)

#Quest items
trophy_of_zenorath = items.Quest_Object("Trophy of Zenorath", "A trophy that once belonged to Zenorath", 100)

#Loot items
rare_gem = items.Loot("Rare Gem", "A kinda rare gem", 30)



'''
Enemies
-------------------------------------------------------------------------------
'''

#Monsters
crazed_duck = enemies.BasicMonster("Crazed Duck", 10, 3, 0)
crazed_duck_2 = enemies.BasicMonster("Crazed Duck", 10, 3, 0)
crazed_rat = enemies.BasicMonster("Crazed Rat", 8, 3, 0)
crazed_cow = enemies.BasicMonster("Crazed Cow", 12, 4, 0)
crazed_chicken = enemies.BasicMonster("Crazed Chicken", 9, 3, 0)
rabid_stoat = enemies.BasicMonster("Rabid Stoat", 20, 6, 0)
hell_creature = enemies.BasicMonster("Hell Creature", 50, 12, 0)

#Random Monsters
r_crazed_duck = enemies.BasicMonster("Crazed Duck", 10, 3, 0)
r_crazed_rat = enemies.BasicMonster("Crazed Rat", 8, 3, 0)
r_crazed_cow = enemies.BasicMonster("Crazed Cow", 12, 4, 0)
r_crazed_chicken = enemies.BasicMonster("Crazed Chicken", 9, 3, 0)

'''
NPCs
-------------------------------------------------------------------------------
'''

#Random dude
steve = npc.Villager("Steve Duncun",
                     "male",
                     0,
                     [sandwich])

#Trader
frank = npc.Trader("Franklin Duncun",
                   1000,
                   [health_potion,
                    health_potion,
                    health_potion,
                    health_potion,
                    health_potion,
                    bronze_boots,
                    sandwich])

'''
Dialog tile
-------------------------------------------------------------------------------
'''

steve_hole = world.InhabitedTile(0, -2,
                                 [steve],
                                 utilities.boxer.make_text_box("A dank hole where a dirty man lives. His name is Steve Duncun."),
                                 utilities.boxer.make_text_box("In the real game, people like me will be able to say more than one line.\nBut we'll still only be a few lines of unfeeling code.'"))

'''
Tiles
-------------------------------------------------------------------------------
'''
start_room = world.StartTile(0, 0, "\nAn empty room.")

quest_giver_room = world.QuestTile(1, 0, )

empty_room = world.EmptyTile(2, 0, "\nAnother empty room.")

find_desired_item_room = world.FindItemTile(2, -1, )

barrier_room = world.SOMETHING(1, 1, )

nothing_room = world.EmptyTile(1, 2, "\nThere's nothing here!")

trader_room = world.TraderTile(3, 0, frank, "\nA room with a Frank in it.")

victory_room = world.VictoryTile(1, 3, "\nYOU DID EEEET!")

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
game_map[(0,0)] = start_room
game_map[(1,0)] = quest_giver_room
game_map[(2,0)] = empty_room
game_map[(2,-1)] = find_desired_item_room
game_map[(1, 1)] = barrier_room
game_map[(1, 2)] = nothing_room 
game_map[(3, 0)] = trader_room
game_map[(1, 3)] = victory_room



#This function determines which tile is at which loction. It is utilized from game.py
def tile_at(x, y):
    try:
        return game_map[(x,y)]
    except KeyError:
        return None

'''
Player
-------------------------------------------------------------------------------
'''

new_player = Player()
new_player.inventory.weapon_inventory.ls.append(rusty_knife)
new_player.inventory.boots_slot.ls.append(shit_boots)