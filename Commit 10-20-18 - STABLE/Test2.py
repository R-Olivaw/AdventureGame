import items, world, utilities, npc

shit_helmet = items.Helmet("Shit helmet", "A shitty helmet", 1, 0)                
rusty_helmet = items.Helmet("Rusty Helmet", "A rusty ass helmet", 4, 0)   
dank_potion = items.HealingPotion("Dank Potion", 42, 15)
rusty_knife = items.Dagger("Rusty Knife", "It will give you tetnis", 3, 0) 
cool_sword = items.Sword("Cool Sword", "A pretty cool sword", 4, 1)    
rusty_chest_plate = items.Chest("Rusty Chest Plate", "Not good armor", 3, 0)
cotton_pants = items.Pants("Cotton Pants", "Plain pants", 0, 0)
shit_boots = items.Boots("Shit boots", "Shitty boots", 1, 20)
leather_boots = items.Boots("Leather boots", "Worn out boots", 2, 40)
broken_sheild = items.Sheild("Broken Sheild", "Busted ass shield", 2, 0)
trophy_of_zenorath = items.Quest_Object("Trophy of Zenorath", "A trophy that once belonged to Zenorath", 100)
rare_gem = items.Loot("Rare Gem", "A kinda rare gem", 30)

rusty_key = items.Door_Key("Rusty Key", "A rusty key", 0, 666)

'''
player.py
'''

#This class acts as a list.
#The max_length variable is checked by tile functions to determine if the inventory can hold more items.
#The acceptable_class variable is checked by tile functions to select and pair items to inventories.
class InventoryList:

    def __init__(self, max_length, acceptable_class):
        #This variable denotes the maximum number of items that the list can hold.
        #Tile functions will check this before giving the player an item.
        self.max_length = max_length
        #This variable will check a string to see if it matches the type variable of an item class
        self.acceptable_class = acceptable_class
        #The actual list of items
        self.ls = []

    def get_list(self):
        return self.ls
   
#The player's inventory is a separate class from the player.
#This class builds an inventory composed of IventoryList instances.        
class PlayerInventory:
    
    def __init__(self):
        
        #Weapon inventory
        self.weapon_inventory = InventoryList(1, 'weapon')
        
        #Armor slots
        self.helmet_slot = InventoryList(1, 'helmet')
        self.chest_slot = InventoryList(1, 'chest')
        self.pants_slot = InventoryList(1, 'pants')
        self.boots_slot = InventoryList(1, 'boots')
        self.sheild_slot = InventoryList(1, 'sheild')
        
        #Main armor inventory - an unordered list containing specific InventoryList instances
        self.armor_inventory = [self.helmet_slot,
                                self.chest_slot,
                                self.pants_slot,
                                self.boots_slot,
                                self.sheild_slot]
        
        #Consumables inventory
        self.consumables_inventory = InventoryList(10, 'consumable')
        
        #Quest items inventory
        self.quest_inventory = InventoryList(10, 'quest_item')
        
        #Loot items inventory
        self.valuables_inventory = InventoryList(100, 'loot')
        
        #Main inventory - an unordered list containing specific InventoryList instances
        self.inventory_index = [self.weapon_inventory,
                          self.consumables_inventory,
                          self.quest_inventory,
                          self.valuables_inventory]
    
    #This function fills the player's armor slots with an initial loadout.
    #Change the variables to create a new starting loadout.
    #If you're building a new game, you'll make to sure these variables match the starting equipment you want a new player to have.
    #I don't know what happens if one of these empty.    
    def build_starting_inventories(self, weapon, helmet, chest, pants, boots, sheild):
        
        self.weapon_inventory.ls.append(weapon)
        
        self.helmet_slot.ls.append(helmet)
        
        self.chest_slot.ls.append(chest)
        
        self.pants_slot.ls.append(pants)
        
        self.boots_slot.ls.append(boots)
        
        self.sheild_slot.ls.append(sheild)
   
         
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
            if slot.ls:
                self.armor = self.armor + slot.ls[0].protection
                
                    
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
        room = testgame.tile_at(self.x, self.y)
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
        room = testgame.tile_at(self.x, self.y)
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
                
    def trade(self):
        room = testgame.tile_at(self.x, self.y)
        room.check_if_trade(self)
        
    def examine_puzzle(self):
        room = testgame.tile_at(self.x, self.y)
        room.initiate_puzzle(self)
        
    def examine_clues(self):
        room = testgame.tile_at(self.x, self.y)
        room.look_around()
        
    def talk(self):
        room = testgame.tile_at(self.x, self.y)
        room.dialog_tree()

'''
world.py
'''

class FindItemTile(world.MapTile):
    def __init__(self, x, y, item, first_description, last_description):
        self.x = x
        self.y = y
        self.item = item
        self.item_claimed = False
        self.first_description = first_description
        self.last_description = last_description
 
    def intro_text(self):
        text1 = self.first_description
        text2 = self.last_description
        if self.item_claimed:
            return text2
        else:
            return text1
        
    def inspect_item(self, player):
        #If the item has not been picked up yet...
        if not self.item_claimed:
            #------------------------------------------------------------------
            #And if that item is armor...
            if self.item.type in ['helmet', 'chest', 'pants', 'boots', 'sheild']:
                #We search through slots in the armor inventory
                for slot in player.inventory.armor_inventory:
                    #And find the slot that matches the item type...
                    if slot.acceptable_class == self.item.type:
                        #We assign the right slot to a new variable...
                        selected_slot = slot
                        #And if the selected slot is empty...
                        if not selected_slot.ls:
                            #We mark the tile clear...
                            self.item_claimed = True
                            #Give the player the item...
                            selected_slot.ls.append(self.item)
                            #And inform them.
                            print("You picked up {}!".format(self.item.name))
                            #Then move on.
                            return
                        #And if the selected slot is filled...
                        else:
                            while True:
                                #We ask if they would like to swap out their current item for the new item...
                                print("You found {}! Do you want to swap it for your {}? [Y / N]".format(self.item.name, selected_slot.ls[0].name ) )
                                ans = input("Input: ").lower()
                                #If they reply in the affirmative...
                                if ans == 'y':
                                    #We clear the selected slot...
                                    selected_slot.ls.clear()
                                    #Mark the tile clear...
                                    self.item_claimed = True
                                    #Put the item into the selected slot...
                                    selected_slot.ls.append(self.item)
                                    #Inform the plater...
                                    print("You picked up {}!".format(self.item.name) )
                                    #Then move on.
                                    return
                                #If they reply in the negative...
                                elif ans == 'n':
                                    #We inform them they have left the item...
                                    print("You leave the {} and move on.".format(self.item.name))
                                    #Then move on...
                                    return
                                else:
                                    print("INVALID INPUT!")
                                    pass
            #------------------------------------------------------------------                    
            #And if that item is a weapon...
            elif self.item.type in ['weapon']:
                #And if the player's weapon inventory is empty...
                if not player.inventory.weapon_inventory.ls:
                    #We mark the tile cleared...
                    self.item_claimed = True
                    #We give the player the item...
                    selected_slot.append(self.item)
                    #Iform the player...
                    print("You picked up {}!".format(self.item.name))
                    #And move on.
                    return
                #And if they player's weapon inventory has no free slot...
                else:
                    while True:
                        selected_slot = player.inventory.weapon_inventory.ls
                        #We ask if they want to make a swap...
                        print("You found {}! Do you want to swap it for your {}? [Y / N]".format(self.item.name, selected_slot[0].name) )
                        ans = input("Input: ").lower()
                        #If they reply in the affirmative...
                        if ans == 'y':
                            #We clear the selected slot...
                            selected_slot.clear()
                            #Mark the tile clear...
                            self.item_claimed = True
                            #Put the item into the selected slot...
                            selected_slot.append(self.item)
                            #Inform the plater...
                            print("You picked up {}!".format(self.item.name) )
                            #Then move on.
                            return
                        #If they reply in the negative...
                        elif ans == 'n':
                            #We inform them they have left the item...
                            print("You leave the {} and move on.".format(self.item.name))
                            #Then move on...
                            return
                        else:
                            print("INVALID INPUT!")
                            pass
                    
             #-----------------------------------------------------------------
             #And if that item is a health item...
            elif self.item.type in ['consumable']:
                #We select the consumables inventory...
                selected_slot = player.inventory.consumables_inventory.ls
                #And if the player's consumable inventory contains free slots...
                if len(selected_slot) < player.inventory.consumables_inventory.max_length:
                    #We mark the tile cleared...
                    self.item_claimed = True
                    #Put the item into the selected slot...
                    selected_slot.append(self.item)
                    #Inform the player...
                    print("You picked up {}!".format(self.item.name))
                    #And move on.
                    return
                #And if the player's consumable inventory is full...
                elif len(selected_slot) >=  player.inventory.consumables_inventory.max_length:
                    #We inform the player that they are out of room...
                    print("You find {}, but you can't carry any more!".format(self.item.name))
                    #And move on...
                    return
                
            #-----------------------------------------------------------------
            #And if that item is a quest item...    
            elif self.item.type in ['quest_item']:
                #We select the quest items inventory...
                selected_slot = player.inventory.quest_inventory.ls
                #And if the player's quest items inventory contains free slots...
                if len(selected_slot) < player.inventory.quest_inventory.max_length:
                    #We mark the tile cleared...
                    self.item_claimed = True
                    #Put the item into the selected slot...
                    selected_slot.append(self.item)
                    #Inform the player...
                    print("You picked up {}!".format(self.item.name))
                    #And move on.
                    return
                #And if the player's quest items inventory is full...
                elif len(selected_slot) >=  player.inventory.quest_inventory.max_length:
                    #We inform the player that they are out of room...
                    print("You find {}, but you can't carry any more!".format(self.item.name))
                    #And move on...
                    return
                
            #-----------------------------------------------------------------
            #And if that item is a loot item...    
            elif self.item.type in ['loot']:
                #We select the valuables inventory...
                selected_slot = player.inventory.valuables_inventory.ls
                #And if the player's valuables inventory contains free slots...
                if len(selected_slot) < player.inventory.valuables_inventory.max_length:
                    #We mark the tile cleared...
                    self.item_claimed = True
                    #Put the item into the selected slot...
                    selected_slot.append(self.item)
                    #Inform the player...
                    print("You picked up {}!".format(self.item.name))
                    #And move on.
                    return
                #And if the player's quest items inventory is full...
                elif len(selected_slot) >=  player.inventory.valuables_inventory.max_length:
                    #We inform the player that they are out of room...
                    print("You find {}, but you can't carry any more!".format(self.item.name))
                    #And move on...
                    return
            #If something has gone horribly wrong...    
            else:
                print("***ERROR***ITEM***HAS***NO***TYPE***ERROR***")
        #If the tile's item has already been claimed, we move on.
        else:
            pass
    

class QuestTile(world.MapTile):
    
    def __init__(self, x, y, quest_giver, desired_item, reward, uncompleted_text, completed_text):
        self.x = x
        self.y = y
        self.quest_giver = quest_giver
        self.desired_item = desired_item
        self.reward = reward
        self.uncompleted_text = uncompleted_text 
        self.completed_text = completed_text
        self.quest_complete = False
        
    def intro_text(self):
        text = self.uncompleted_text if not self.quest_complete else self.completed_text
        return text
    
    def dialog_tree(self, player):
        if not self.desired_item in player.inventory.consumables_inventory.ls:
            print("You approach {}. {} sniffs the air around you.\n'No {}? Bring me {}!'".format(self.quest_giver.name, self.quest_giver.pronoun.capitalize(), self.desired_item.name, self.desired_item.name))
            return
        else:
            print("You approach {}. {} sizes you up for a moment, then asks 'Got any {}?'".format(self.quest_giver.name, self.quest_giver.pronoun.capitalize(), self.desired_item.name))
            print("1. Lie\n2. Give {}".format(self.desired_item.name))
            ans = input("Choice: ")
            
            while True:
                try:
                    if ans == '1':
                        print("You tell {} you don't have any {}.\n'Like hell you don't.' {} says.\nYou leave.".format(self.quest_giver.name, self.desired_item.name, self.quest_giver.name))
                        return
                    elif ans == '2':
                        player.inventory.consumables_inventory.ls.remove(self.desired_item)
                        player.inventory.quest_inventory.ls.append(self.reward)
                        print("{} snatches the {}. After {} devours it, {} hands you a {}.".format(self.quest_giver.name, self.desired_item.name, self.quest_giver.pronoun, self.quest_giver.pronoun, self.reward.name))
                        return
                    else:
                        print("Make a selection!")
                        return
                except ValueError:
                    print("INVALID!")
                    
                    
from basicmap import new_player

crusty_bread = items.Food('Crusty Bread', 20, 5)

frank = npc.QuestGiver('Frank', 'male', 400, [rusty_key])

#new_player.inventory.consumables_inventory.ls.append(crusty_bread)

room = QuestTile(0, 0, frank, crusty_bread, rusty_key, 'Frank has key!', 'Frank has bread!')

room.dialog_tree(new_player)

new_player.display_items_inventory()
        
        
'''        
class QuestTile(world.MapTile):    
    
    def __init__(self, x, y, quest_giver, desired_item, reward, uncompleted_text, completed_text):
        self.x = x
        self.y = y
        self.quest_giver = quest_giver
        self.desired_item = desired_item
        self.reward = reward
        self.uncompleted_text = uncompleted_text 
        self.completed_text = completed_text
        self.quest_complete = False
    
    def intro_text(self):
        text = self.uncompleted_text if not self.quest_complete else self.completed_text
        return text
    
    #If the player has the desired item, they will have the option to give it to the quest giver.
    def dialog_tree(self, player):
        if not self.quest_complete:
            greet = '\nHARUMPH!'
        else:
            greet = '\nDELICIOUS!'
        print(greet)
        
        if self.desired_item in player.inventory:
            print("\n{} looks excited.\n\n'Give me that {}, won't you?'".format(self.quest_giver.name, self.desired_item.name))
            ans = input("Give {} the {}? [Y/N]\n\nAnswer: ".format(self.quest_giver.name, self.desired_item.name)).lower()
            if ans in ["y", "yes"]:
                player.inventory.remove(self.desired_item)
                player.inventory.append(self.reward)
                print("\n{} takes the {} and grins.\n\n'Here, take this.'".format(self.quest_giver.name, self.desired_item.name))
                print("\nYou recieved {}!".format(self.reward))
                #sets the completed variable to True, so player cannot repeat the quest.
                self.quest_complete = True
                return
            else:
                #If the player changes their mind, we exit the loop.
                print("\n{} huffs. 'Fine! Begone!'".format(self.quest_giver.name))
                return
        else:
            if not self.quest_complete:
                print("\n{} frowns at your presence. 'Bring me {}, won't you? There's something in it for you!'".format(self.quest_giver.name, self.desired_item.name))
                return
            else:
                return
'''
            
#This tile blocks player from moving if they do not possess a corresponding key item.
#Otherwise, if player possess the corresponding key, the tile move them forward - and lock behind them. Player can open it again, as long as they keep the key.
class LockedRoom(world.MapTile):
    
    def __init__(self, x, y, unlocked_status, locked_text, unlocked_text, desired_key_id_code):
        self.x = x
        self.y = y
        self.unlocked_status = False
        self.locked_text = locked_text
        self.unlocked_text = unlocked_text
        self.desired_key_id_code = desired_key_id_code
    
    #Displays some text when the player enters the tile.    
    def intro_text(self):
        text = self.locked_text if not self.unlocked_status else self.unlocked_text
        return text    
    
    #This gets triggered by the check_for_key function if the player does not possesses the correct key.
    #It moves the player to the SimplePassage tile at self.y-1.    
    def block_player(self, player):
        print("\nYou don't have the correct key.\nYou leave.")
        player.place_in_map(self.x, self.y-1)
        return
    
    #This gets triggered by the check_for_key function if the player possesses the correct key.
    #It moves the player to the SimplePassage tile at self.y+1.         
    def pass_player(self, player):
        print("You pass through the door")
        player.place_in_map(self.x, self.y+1)
        return
    
    #This function is triggered from PLAYER.PY.
    #Checks the player's quest_item_inventory for keys, then checks those key's id_codes.
    #If id_codes match, trigger the pass_player function, if not, the block_player funciton.
    def check_for_key(self, player):
        key_inventory = player.inventory.quest_inventory.ls
        
        if len(key_inventory) == 0:
            self.block_player(player)
        else:
            for i in key_inventory:
                if i.id_code:                
                    if i.id_code == self.desired_key_id_code:
                        print("You unlock the door with the key.")
                        self.pass_player(player)
                    else:
                        self.block_player(player)
                else:
                    self.block_player(player)

#This tile is ALWAYS located at y-1 or y+1 relative to its corresponging LockedRoom tile.
#Example: If LockedRoom's coordinates are (1, 2), SimpleTile's coordinates MUST be either (1, 1) or (1, 3)
class SimplePassage(world.MapTile):
    
    def __init__(self, x, y, description):
        self.x = x
        self.y = y
        self.description = description
        
    def intro_text(self):
        text = self.description
        return text
    




        
#IN GAME.PY:
'''
#PLACE THIS ABOVE THE ATTACK ROOM IF STATEMENT
if isinstance(room, world.LockedRoom):
    action_adder(actions, 't', player.try_door, "Try door")
        

#IN PLAYER.PY
        
        def try_door(self):
        room = main_map.tile_at(self.x, self.y)
        room.check_for_key(self)
            
'''            
'''                
class Locked_Room(world.MapTile):
    
    def __init__(self, x, y, unlocked_status, block_direction):
        self.x = x
        self.y = y
        self.unlocked_status = False
        self.block_direction = block_direction
        
    def define_coordinates(self):
        if unlocked_status = 'south':
            coord = (self.x, self.y - 1)
        elif unlocked_status = 'north':
            coord = (self.x, self.y + 1)
        elif unlocked_status = 'east':
            coord = (self.x + 1, self.y)
        elif unlocked_status = 'west':
            coord =(self.x - 1, self.y)
        
    def limit_player_movement(self, player):
        print("SORRY ROOM IS LOCKED.")
        ans = input("Leave? [Y/N]: ")
        while True:
            if ans not in ['Y', 'y']:
                print("You pause to consider the door.")
            else:
                self.define_coordinates()
                if self.coord == 
                    
    
    def check_for_key(self, player):
        pass 
'''
'''
IN GAME.PY

elif isinstance(room, world.Locked_Room) and (room.unlocked_status = False):
        action_adder(actions, 'l', player.leave_room, "Leave") 

elif isinstance(room, world.Locked_Room) and (room.unlocked_status = True):
    pass

IN PLAYER.PY

def leave(self):
        room = main_map.tile_at(self.x, self.y)
        room.limit_player_movement(self)

'''                               
                
'''                

player is in room adjacent to the locked room.
player has option to move to room.
When player moves to locked room tile and does NOT have the correct key instance, they are not able to move in blocked_direction.
    They are presented with text explaining the situation.
When player moves to locked room tile and HAS the correct key instance, the tile is basically an empty tile.
    They are presented with some text telling them the room was unlocked.

'''

'''
shit_helmet = items.Helmet("Shit helmet", "A shitty helmet", 1, 0)                
rusty_helmet = items.Helmet("Rusty Helmet", "A rusty ass helmet", 4, 0)   
dank_potion = items.HealingPotion("Dank Potion", 42, 15)
rusty_knife = items.Dagger("Rusty Knife", "It will give you tetnis", 3, 0) 
cool_sword = items.Sword("Cool Sword", "A pretty cool sword", 4, 1)    
rusty_chest_plate = items.Chest("Rusty Chest Plate", "Not good armor", 3, 0)
cotton_pants = items.Pants("Cotton Pants", "Plain pants", 0, 0)
shit_boots = items.Boots("Shit boots", "Shitty boots", 1, 20)
leather_boots = items.Boots("Leather boots", "Worn out boots", 2, 40)
broken_sheild = items.Sheild("Broken Sheild", "Busted ass shield", 2, 0)
trophy_of_zenorath = items.Quest_Object("Trophy of Zenorath", "A trophy that once belonged to Zenorath", 100)
rare_gem = items.Loot("Rare Gem", "A kinda rare gem", 30)

rusty_key = items.Door_Key('Rusty Key', 'A rusty key', 0)

'''
'''
Game.py
'''




