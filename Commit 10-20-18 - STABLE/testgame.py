from collections import OrderedDict
import random
import world, items, enemies, npc, puzzles, utilities, special_tiles
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
                   "male",
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

steve_hole = special_tiles.SteveTile(0, -2,
                                     [steve],
                                     utilities.boxer.make_text_box("A dank hole where a dirty man lives. His name is Steve Duncun."),
                                     )


'''
Tiles
-------------------------------------------------------------------------------
'''
new_item_tile = world.FindItemTile(0,0, leather_boots, utilities.boxer.make_text_box("A room with boots"), utilities.boxer.make_text_box("A room without boots.") )

entrance = world.StartTile(0, 0, utilities.boxer.make_text_box("The room feels empty, as if no one took the time to fill it in.") )
duck_room = world.SingleEnemyTile(1, 0, crazed_duck, utilities.boxer.make_text_box("A wild duck raises its beak in anger!"), utilities.boxer.make_text_box("A duck corpse rots on the floor."))
find_helmet_room = world.FindItemTile(2, 0, bronze_helmet, utilities.boxer.make_text_box("You find a shining bronze helmet!"), utilities.boxer.make_text_box("Just an empty, boring room."))
find_gold_room_1 = world.FindGoldTile(2, -1, random.randint(20,50), utilities.boxer.make_text_box("You find some money!"), utilities.boxer.make_text_box("Just a boring room."))
random_enemy_room = world.RandomEnemyTile(2, -2, r_crazed_duck, r_crazed_rat, r_crazed_cow, r_crazed_chicken,
                                          utilities.boxer.make_text_box("A wild duck raises its beak in anger!"), utilities.boxer.make_text_box("A duck corpse rots on the floor."),
                                          utilities.boxer.make_text_box("A wild rat raises its tiny claws in anger!"), utilities.boxer.make_text_box("A rat corpse rots on the floor."),
                                          utilities.boxer.make_text_box("A wild cow raises its hoof in anger!"), utilities.boxer.make_text_box("A cow corpse rots on the floor."),
                                          utilities.boxer.make_text_box("A wild chicken raises its beak in anger!"), utilities.boxer.make_text_box("A chicken corpse rots on the floor."))
find_weapon_room = world.FindItemTile(3, -2, silver_sword, utilities.boxer.make_text_box("You find a gleaming silver sword!"), utilities.boxer.make_text_box("An empty rooom in which the faint smell of glory lingers in the air."))
duck_room_2 = world.SingleEnemyTile(2, 1, crazed_duck_2, utilities.boxer.make_text_box("A wild duck raises its beak in anger!"), utilities.boxer.make_text_box("A duck corpse rots on the floor."))
find_potion_room = world.FindItemTile(2, 2, health_potion, utilities.boxer.make_text_box("You find a bottle of bubbly potion."), utilities.boxer.make_text_box("A slightly chilled room."))
trader_room = world.TraderTile(1, 2, frank, utilities.boxer.make_text_box("A dank, mossy room with a bearded dude in the corner.\nHis name is Frank Duncun. He mumbles to himself."))
rat_room = world.SingleEnemyTile(0, 2, crazed_rat, utilities.boxer.make_text_box("An evil rat squeaks at you!"), utilities.boxer.make_text_box("A dead rat lays splattered on the floor."))
find_sandwich_room = world.FindItemTile(-1, 2, sandwich, utilities.boxer.make_text_box("You found a surprisingly fresh sandwich!"), utilities.boxer.make_text_box("The smell of sandwich lingers in the air."))
find_chest_room = world.FindItemTile(-1, 1, bronze_chest, utilities.boxer.make_text_box("You found a shiny bronze chest plate!"), utilities.boxer.make_text_box("Nothing going on here."))
stoat_room = world.SingleEnemyTile(-2, 1, rabid_stoat, utilities.boxer.make_text_box("A rabid stoat lashes out!"), utilities.boxer.make_text_box("A foaming stoat head lays several feet from its bleeding body."))
find_gold_room_2 = world.FindGoldTile(-2, 0, random.randint(5,25), utilities.boxer.make_text_box("You found some money!"), utilities.boxer.make_text_box("An empty room without any money in it at all."))
password_room = world.PuzzleTile(-2, -1, "\nTHE PUZZLE HAS BEGUN!", "\nWHAT MAKES BARK?", "dog", cool_sword)
hell_room = world.SingleEnemyTile(-2, -2, hell_creature, utilities.boxer.make_text_box("A hell creature of unutterable detail swings it's unmentionable limbs in a spiral of death!"), utilities.boxer.make_text_box("The hell creature lays immobilized on the ground.\nIt will soon stir again!"))
end_room = world.VictoryTile(-3, -2, utilities.boxer.make_text_box("You have escaped from this place of horror!\nGood job, buddy!"))
nothing_room = world.EmptyTile(0, -1, utilities.boxer.make_text_box("Absolutely nothing here to describe."))
cow_room = world.SingleEnemyTile(0, -3, crazed_cow, utilities.boxer.make_text_box("A wild cow raises its hoof in anger!"), utilities.boxer.make_text_box("A cow corpse rots on the floor."))
find_shield_room = world.FindItemTile(1, -3, bronze_shield, utilities.boxer.make_text_box("You find a pretty cool shield!"), utilities.boxer.make_text_box("An empty room. Lame."))

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
game_map[(0,0)] = entrance
game_map[(1,0)] = new_item_tile
game_map[(2,0)] = find_helmet_room
game_map[(2,-1)] = find_gold_room_1
game_map[(2,-2)] = random_enemy_room
game_map[(3,-2)] = find_weapon_room
game_map[(2,1)] = duck_room_2
game_map[(2,2)] = find_potion_room
game_map[(1,2)] = trader_room
game_map[(0,2)] = rat_room
game_map[(-1,2)] = find_sandwich_room
game_map[(-1,1)] = find_chest_room
game_map[(-2,1)] = stoat_room
game_map[(-2,0)] = find_gold_room_2
game_map[(-2,-1)] = password_room
game_map[(-2,-2)] = hell_room
game_map[(-3,-2)] = end_room
game_map[(0,-1)] = nothing_room
game_map[(0,-2)] = steve_hole
game_map[(0,-3)] = cow_room
game_map[(1,-3)] = find_shield_room



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
