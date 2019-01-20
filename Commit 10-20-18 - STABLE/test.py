from collections import OrderedDict

import basicmap as main_map

def get_available_actions(room, player):
    import world
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
    if (isinstance(room, world.QuestTile) or isinstance(room, world.InhabitedTile)):
        action_adder(actions, 'f', player.talk, "Talk")
    if isinstance(room, world.PuzzleTile) and not room.puzzle_solved:
        action_adder(actions, 'f', player.examine_puzzle, "Examine puzzle")
    if isinstance(room, world.ClueTile):
        action_adder(actions, 'f', player.examine_clues, "Examine the room")
    if isinstance(room, world.FindItemTile) and not room.item_claimed:
        action_adder(actions, 'r', player.inspect_item, "Inspect item")
    if player.hp < 100 and any(isinstance(x, items.Consumable) for x in inventory.consumables_inventory.ls):
        action_adder(actions, 'h', player.heal, "Heal")
    action_adder(actions, 'm', player.display_menu, "Menu")
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
            
            
#IN PLAYER.PY
            
def display_menu(self):
    print("""
          
    ───Menu────────────────────────────────────────────────────────────────────
    
    1. Display Weapon Inventory
    2. Display Armor Inventory
    3. Display Items Inventory
    4. Check Player Stats
    X. Exit
    
    ───────────────────────────────────────────────────────────────────────────
    
    """)
    
    ans = input("""
    
    Choice: 
                """)
        
    if ans == '1':
        self.display_weapon_inventory()
    elif ans == '2':
        self.display_armor_inventory()
    elif ans == '3':
        self.display_items_inventory()
    elif ans == '4':
        self.check_stats()
    elif ans in ['x', 'X', 'exit', 'Exit']:
        return
    else:
        print("Invalid Choice!")
        return