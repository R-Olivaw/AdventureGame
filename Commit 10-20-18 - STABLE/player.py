'''
This module contains the player class.

The user can input commands and interact with the world, enemies, items, etc.

'''
#Build the all instances in another file. Import here as main_map. Same in game.py.

import testgame as main_map

'''
Player Inventory class
-------------------------------------------------------------------------------
'''

#This class acts as a list.
#The max_length variable is checked by tile functions to determine if the inventory can hold more items.
#The acceptable_class variable is checked by tile functions to select and pair items to inventories.
class InventoryList:

    def __init__(self, max_length, acceptable_class, name):
        #This variable denotes the maximum number of items that the list can hold.
        #Tile functions will check this before giving the player an item.
        self.max_length = max_length
        #This variable will check a string to see if it matches the type variable of an item class
        self.acceptable_class = acceptable_class
        #A variable that displays in-game.
        self.name = name
        #The actual list of items
        self.ls = []

    def get_list(self):
        return self.ls
   
#The player's inventory is a separate class from the player.
#This class builds an inventory composed of IventoryList instances.        
class PlayerInventory:
    
    def __init__(self):
        
        #Weapon inventory
        self.weapon_inventory = InventoryList(1, 'weapon', 'Weapon Inventory')
        
        #Armor slots
        self.helmet_slot = InventoryList(1, 'helmet', 'Helmet Slot')
        self.chest_slot = InventoryList(1, 'chest', 'Chest Slot')
        self.pants_slot = InventoryList(1, 'pants', 'Pants Slot')
        self.boots_slot = InventoryList(1, 'boots', 'Boots Slot')
        self.sheild_slot = InventoryList(1, 'sheild', 'Sheild Slot')
        
        #Main armor inventory - an unordered list containing specific InventoryList instances
        self.armor_inventory = [self.helmet_slot,
                                self.chest_slot,
                                self.pants_slot,
                                self.boots_slot,
                                self.sheild_slot]
        
        #Consumables inventory
        self.consumables_inventory = InventoryList(10, 'consumable', 'Consumables Inventory')
        
        #Quest items inventory
        self.quest_inventory = InventoryList(10, 'quest_item', 'Quest Items Inventory')
        
        #Loot items inventory
        self.valuables_inventory = InventoryList(100, 'loot', 'Loot Inventory')
        
        #Main inventory - an unordered list containing specific InventoryList instances
        self.inventory_index = [self.weapon_inventory,
                          self.consumables_inventory,
                          self.valuables_inventory]
   


'''
Player class
-------------------------------------------------------------------------------
'''

#This class is how the user interacts with the game.
class Player:
    
    def __init__(self):
        self.hp = 100
        self.gold = 10
        self.victory = False
        self.armor = 0
        self.inventory = PlayerInventory()
        
    def place_in_map(self, x, y):
        self.x = x
        self.y = y
    
    #This lets us know if the player is still alive.    
    def is_alive(self):
        return self.hp > 0
    
    #This checks if the player has armor, adds the protection values of all armor pieces, then adjusts player.armor accordingly.
    def armor_check(self):
        for slot in self.inventory.armor_inventory:
            try:
                if slot.ls:
                    self.armor = self.armor + slot.ls[0].protection
            except:
                pass
                    
    #This resets the player's armor back to zero.                
    def armor_reset(self):
        self.armor = 0
        
    #This changes coordinates based on the tile list in the world module.    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    #The following four functions move the player through the world, using the move function above.     
    def move_north(self):
        self.move(dx=0, dy=1)
    
    def move_south(self):
        self.move(dx=0, dy=-1)
        
    def move_east(self):
        self.move(dx=1, dy=0)
        
    def move_west(self):
        self.move(dx=-1, dy=0)
    
    #This function determines which weapon in the player's inventory is the most powerful.
    #Enemy tile classes will check this variable during enemy encounters.    
    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory.weapon_inventory.ls:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        return best_weapon
    
    def exit_game(self):
        print("\nAre you sure you want to quit the game?")
        ans = input("\n[Y/N]: ")
        
        while True:
            if ans in ['n', 'N']:
                return
            elif ans in ['y', 'Y']:
                from sys import exit
                exit(0)
            else:
                print("\nINVALID")
                return
    
    #Shows the player's weapon inventory and displays the most powerful one.    
    def display_weapon_inventory(self):
        print("""
      ---Weapons---({}/{})-----------------------------------------------------
      """.format( len(self.inventory.weapon_inventory.ls), self.inventory.weapon_inventory.max_length ))
        
        for item in self.inventory.weapon_inventory.ls:
            print('   * ' + str(item))
            
        best_weapon = self.most_powerful_weapon()
        
        print("""
        -----------------------------------------------------------------------      
        Your most powerful weapon is: {}.
        -----------------------------------------------------------------------
        """.format(best_weapon.name))
    
    #Displays the player's gold, consumables, valuables and quest items.    
    def display_items_inventory(self):
        print(""" 
      ───Inventory─────────────────────────────────────────────────────────────
      """)
        
        print("""
         ===[ GOLD: {} ]=======================================================
         """.format(self.gold))
        
        
        print("""
         ---Health Items---({}/{})---------------------------------------------
      """.format( len(self.inventory.consumables_inventory.ls), self.inventory.consumables_inventory.max_length ))
        
        for item in self.inventory.consumables_inventory.ls:
            print('   * ' + str(item))
            
        print("""
         ---Valuables---({}/{})------------------------------------------------
      """.format( len(self.inventory.valuables_inventory.ls), self.inventory.valuables_inventory.max_length ))
        
        for item in self.inventory.valuables_inventory.ls:
            print('   * ' + str(item))
            
        print("""
         ---Quest Items---({}/{})----------------------------------------------
      """.format( len(self.inventory.quest_inventory.ls), self.inventory.quest_inventory.max_length ))
        
        for item in self.inventory.quest_inventory.ls:
            print('   * ' + str(item))
    
    #Display's the player's armor slots.
    def display_armor_inventory(self):        
        print(""" 
      ───Armor─────────────────────────────────────────────────────────────────
      
          ---Helmet Slot-------------------------------------------------------
      """)
        
        for item in self.inventory.helmet_slot.ls:
            print('   * ' + str(item))
            
        print("""
          ---Chest Slot--------------------------------------------------------
        """)
        
        for item in self.inventory.chest_slot.ls:
            print('   * ' + str(item))
            
        print("""
          ---Pants Slot--------------------------------------------------------
        """)
        
        for item in self.inventory.pants_slot.ls:
            print('   * ' + str(item))
            
        print("""
          ---Boots Slot--------------------------------------------------------
        """)
        
        for item in self.inventory.boots_slot.ls:
            print('   * ' + str(item))
            
        print("""
          ---Sheild Slot--------------------------------------------------------
        """)
        
        for item in self.inventory.sheild_slot.ls:
            print('   * ' + str(item))
            
    #Theis function checks the player's inventory for consumables.
    ##It tells the player if there are no items available.
    ##If there are consumables, it generates a list, then prompts the player to make a choice.
    ##It then heals the player's hp, based on the item's stats, and deletes that item from the inventory.
    def heal(self):
        import items
        consumables = [item for item in self.inventory if isinstance(item, items.Consumable)]
        if not consumables:
            print("\n" + ("- " * 3) + "You don't have any items to heal you!")
            return
        print("\n" + ("- " * 3) + "Choose an item to use to heal: \n------------------------------------")
        for i, item in enumerate(consumables, 1):
            print("\n" + ("- " * 3) + "{}. {}".format(i, item))
        valid = False
        while not valid:
            choice = input("\n" + ("- " * 3) + "Selection: ")
            try:
                to_eat = consumables[int(choice) - 1]
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("\n\n" + ("- " * 3) + "Current HP: {:.0f}".format(self.hp))
                valid = True
            except (ValueError, IndexError):
                print("\n" + ("- " * 3) + "Invalid choice, try again.")
                
    #Deals damage to an enemy
    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = main_map.tile_at(self.x, self.y)
        enemy = room.enemy
        damage = best_weapon.damage
        print("\n" + ("- " * 3) + "You use {} against {}!".format(best_weapon.name, enemy.name))
        
        if not enemy.is_alive():
            print("\n" + ("- " * 3) + "\nYou killed {}!".format(enemy.name))
        else:
            try:
                #If the enemy has armor, this function will reduce player damage accordingly.
                if enemy.armor > 0:
                    x = enemy.armor
                    x = 100 - x
                    x = (x * 0.01)
                    damage = (damage*x)
                    enemy.hp = enemy.hp - damage
                    if enemy.hp < 0:
                        enemy.hp = 0
                    print("\n" + ("- " * 3) + "{} HP is {:.0f}!".format(enemy.name, enemy.hp))
                    #The next two lines reset the player's damage, so that when the combat loop runs again, the damage remains consistent. 
                    damage = (damage / x)
                    damage = (int(round(damage)))
                else:
                    #If the enemy has no armor, we simply subtract player damage from enemy hp.
                    enemy.hp = enemy.hp - damage
                    print("\n" + ("- " * 3) + "{} HP is {:.0f}!".format(enemy.name, enemy.hp))
            except ValueError:
                print("Something happened. I don't know.")
                
    #A modified version of the attack function. Lets the player choose which enemy to attack in a MultiEnemyTile.             
    def multi_attack(self):
        room = main_map.tile_at(self.x, self.y)
        best_weapon = self.most_powerful_weapon()
        enemy1 = room.enemy1
        enemy2 = room.enemy2
        damage = best_weapon.damage
        
        #This is what happens if both enemies are alive.
        if enemy1.is_alive() and enemy2.is_alive():
        
            player_input = input("\n" + ("- " * 3) + "Attack which enemy?\n\n1. {}\n2. {}\n\nAction: ".format(enemy1, enemy2))
            
            try:
                if player_input == "1":
                    try:
                        #If the enemy has armor, this function will reduce player damage accordingly.
                        if enemy1.armor > 0:
                            x = enemy1.armor
                            x = 100 - x
                            x = (x * 0.01)
                            damage = (damage*x)
                            enemy1.hp = enemy1.hp - damage
                            if enemy1.hp < 0:
                                enemy1.hp = 0
                            print("\n" + ("- " * 3) + "You use {} against {}!".format(best_weapon.name, enemy1.name))
                            print("\n" + ("- " * 3) + "{} HP is {:.0f}!".format(enemy1.name, enemy1.hp))
                            #The next two lines reset the player's damage, so that when the combat loop runs again, the damage remains consistent. 
                            damage = (damage / x)
                            damage = (int(round(damage)))
                        else:
                            #If the enemy has no armor, we simply subtract player damage from enemy hp.
                            enemy1.hp = enemy1.hp - damage
                            print("\n" + ("- " * 3) + "You use {} against {}!".format(best_weapon.name, enemy1.name))
                            print("\n" + ("- " * 3) + "{} HP is {:.0f}!".format(enemy1.name, enemy1.hp))
                            
                    except ValueError:
                        print("Something happened. I don't know.")
                    
                elif player_input == "2":
                    try:
                        #If the enemy has armor, this function will reduce player damage accordingly.
                        if enemy2.armor > 0:
                            x = enemy2.armor
                            x = 100 - x
                            x = (x * 0.01)
                            damage = (damage*x)
                            enemy2.hp = enemy2.hp - damage
                            if enemy2.hp < 0:
                                enemy2.hp = 0
                            print("\n" + ("- " * 3) + "You use {} against {}!".format(best_weapon.name, enemy2.name))
                            print("\n" + ("- " * 3) + "{} HP is {:.0f}!".format(enemy2.name, enemy2.hp))
                            #The next two lines reset the player's damage, so that when the combat loop runs again, the damage remains consistent. 
                            damage = (damage / x)
                            damage = (int(round(damage)))
                        else:
                            #If the enemy has no armor, we simply subtract player damage from enemy hp.
                            enemy2.hp = enemy2.hp - damage
                            print("\n" + ("- " * 3) + "You use {} against {}!".format(best_weapon.name, enemy2.name))
                            print("\n" + ("- " * 3) + "{} HP is {:.0f}!".format(enemy2.name, enemy2.hp))
                            
                    except ValueError:
                        print("Something happened. I don't know.")
                        
                else:
                    print("\n" + ("- " * 3) + "Invalid Action!")
                    
            except ValueError:
                print("Something happened in player.attack.")
        
        #This happens if enemy1 is alive and enemy2 is dead.
        elif enemy1.is_alive() and not enemy2.is_alive():
            try:
                #If the enemy has armor, this function will reduce player damage accordingly.
                if enemy1.armor > 0:
                    x = enemy1.armor
                    x = 100 - x
                    x = (x * 0.01)
                    damage = (damage*x)
                    enemy1.hp = enemy1.hp - damage
                    if enemy1.hp < 0:
                        enemy1.hp = 0
                    print("\n" + ("- " * 3) + "You use {} against {}!".format(best_weapon.name, enemy1.name))
                    print("\n" + ("- " * 3) + "{} HP is {:.0f}!".format(enemy1.name, enemy1.hp))
                    #The next two lines reset the player's damage, so that when the combat loop runs again, the damage remains consistent. 
                    damage = (damage / x)
                    damage = (int(round(damage)))
                else:
                    #If the enemy has no armor, we simply subtract player damage from enemy hp.
                    enemy1.hp = enemy1.hp - damage
                    print("\n" + ("- " * 3) + "You use {} against {}!".format(best_weapon.name, enemy1.name))
                    print("\n" + ("- " * 3) + "{} HP is {:.0f}!".format(enemy1.name, enemy1.hp))
                    
            except ValueError:
                print("Something happened. I don't know.")
                    
        #This happens if enemy1 is dead and enemy2 is alive.               
        elif not enemy1.is_alive() and enemy2.is_alive():
             try:
                #If the enemy has armor, this function will reduce player damage accordingly.
                if enemy2.armor > 0:
                    x = enemy2.armor
                    x = 100 - x
                    x = (x * 0.01)
                    damage = (damage*x)
                    enemy2.hp = enemy2.hp - damage
                    if enemy2.hp < 0:
                        enemy2.hp = 0
                    print("\n" + ("- " * 3) + "You use {} against {}!".format(best_weapon.name, enemy2.name))
                    print("\n" + ("- " * 3) + "{} HP is {:.0f}!".format(enemy1.name, enemy2.hp))
                    #The next two lines reset the player's damage, so that when the combat loop runs again, the damage remains consistent. 
                    damage = (damage / x)
                    damage = (int(round(damage)))
                else:
                    #If the enemy has no armor, we simply subtract player damage from enemy hp.
                    enemy2.hp = enemy2.hp - damage
                    print("\n" + ("- " * 3) + "You use {} against {}!".format(best_weapon.name, enemy2.name))
                    print("\n" + ("- " * 3) + "{} HP is {:.0f}!".format(enemy2.name, enemy2.hp))
                    
             except ValueError:
                print("Something happened. I don't know.")
                
    def check_stats(self):
        print(""" 
      ───Stats─────────────────────────────────────────────────────────────────
      """)
        
        print("""
      ---HEALTH ({0:.0f}/100)-------------------------------------------------------
      ---ARMOR ({1:.0f})------------------------------------------------------------
        """.format(self.hp, self.armor))
        
    def trade(self):
        room = main_map.tile_at(self.x, self.y)
        room.check_if_trade(self)
        
    def examine_puzzle(self):
        room = main_map.tile_at(self.x, self.y)
        room.initiate_puzzle(self)
        
    def examine_clues(self):
        room = main_map.tile_at(self.x, self.y)
        room.look_around()
        
    def talk(self):
        room = main_map.tile_at(self.x, self.y)
        room.dialog_tree()

    def inspect_item(self):
        room = main_map.tile_at(self.x, self.y)
        room.inspect_item(self)
        
    def try_door(self):
        room = main_map.tile_at(self.x, self.y)
        room.check_for_key(self)
