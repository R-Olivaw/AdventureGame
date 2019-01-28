'''
The main game. 

'''
#Build the all instances in another file. Import here as main_map. Same in player.py.
import testgame as main_map
from collections import OrderedDict


#This function shows the actions available to a player in a given tile    
def get_available_actions(room, player):
    import world, special_tiles
    import items
    inventory = player.inventory
    actions = OrderedDict()
    print("\nChoose an action:\n-----------------\n")
    if (isinstance(room, world.SingleEnemyTile) or isinstance(room, world.RandomEnemyTile)) and (room.enemy.is_alive()):
        action_adder(actions, 'a', player.attack, "Attack")
    elif isinstance(room, world.MultiEnemyTile) and (room.enemy1.is_alive() or room.enemy2.is_alive()):
        action_adder(actions, 'a', player.multi_attack, "Attack")
    elif isinstance(room, world.LockedRoom):
        action_adder(actions, 't', player.try_door, "Try door")
    else:
        if main_map.tile_at(room.x, room.y + 1):
            action_adder(actions, 'n', player.move_north, "Go north")
        if main_map.tile_at(room.x, room.y - 1):
            action_adder(actions, 's', player.move_south, "Go south")
        if main_map.tile_at(room.x + 1, room.y):
            action_adder(actions, 'e', player.move_east, "Go east")
        if main_map.tile_at(room.x - 1, room.y):
            action_adder(actions, 'w', player.move_west, "Go west")
    if isinstance(room, world.TraderTile):
        action_adder(actions, 't', player.trade, "Trade")
    if (isinstance(room, world.QuestTile) or isinstance(room, world.InhabitedTile) or isinstance(room, special_tiles.MapTile) ):
        action_adder(actions, 'f', player.talk, "Talk")
    if isinstance(room, world.PuzzleTile) and not room.puzzle_solved:
        action_adder(actions, 'f', player.examine_puzzle, "Examine puzzle")
    if isinstance(room, world.ClueTile):
        action_adder(actions, 'f', player.examine_clues, "Examine the room")
    if isinstance(room, world.FindItemTile) and not room.item_claimed:
        action_adder(actions, 'r', player.inspect_item, "Inspect item")
    if player.hp < 100 and any(isinstance(x, items.Consumable) for x in inventory.consumables_inventory.ls):
        action_adder(actions, 'h', player.heal, "Heal")
    if player.inventory.weapon_inventory:
        action_adder(actions, 'c', player.display_weapon_inventory, "Print Weapons Inventory")
    if player.inventory.armor_inventory:
        action_adder(actions, 'p', player.display_armor_inventory, "Print Armor Inventory")
    if player.inventory.inventory_index:
        action_adder(actions, 'i', player.display_items_inventory, "Print Items Inventory")
    action_adder(actions, 'ss', player.check_stats, "Check Stats")
    action_adder(actions, 'x', player.exit_game, "QUIT")
    return actions

#This function adds an action to the list of available actions
def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))

#This function prompts the player to make a choice, based on available actions    
def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        print( ("\n"*5) + ('\n* * * * * * * * * * *')  )
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid action!")
            

#Starts the game
def play():
    player = main_map.new_player
    #This will place the player anywhere on the map. Make sure it's a starting title!
    player.place_in_map(0, 0)
    while player.is_alive() and not player.victory:
        room = main_map.tile_at(player.x, player.y)
        player.armor_check()
        print(room.intro_text())
        room.modify_player(player)
        #Reset the player's armor calculation to zero, until next loop.
        player.armor_reset()
        #This part displays the available choices, or ends the game if the player dies.
        if player.is_alive() and not player.victory:
            pass
            choose_action(room, player)
        elif not player.is_alive():
            print("\nYour journey has come to a premature end.")
            
if __name__ == "__main__":     
    play()
