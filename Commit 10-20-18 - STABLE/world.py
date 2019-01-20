"""
This is the game world.

It contains tile subclasses that are arraged in a grid (list). The player moves through the world with the move function in the player module.

"""
#This is the base map tile class. It should never be made directly!
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def intro_text(self):
        pass
        
    def modify_player(self, player):
        pass
    
    def check_armor(self, player, enemy):
        pass
    
    def dialog_tree(self):
        pass

"""
Neutral classes
 * These tiles should NEVER contain a modify_player function!
------------------------------------------------------------------------------
"""

#The tile where the player begins at the start of a new game.
class StartTile(MapTile):
    def __init__(self, x, y, description):
        self.x = x
        self.y = y
        self.description = description
        
        
    def intro_text(self):
        text = self.description
        return text
        
#-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
#This tile affects the player in no way. The player can move through it to another tile.
class EmptyTile(MapTile):
    def __init__(self, x, y, description):
        self.x = x
        self.y = y
        self.description = description
        
    def intro_text(self):
        text = self.description
        return text
    
#-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
#This tile contains some number of non-violent npcs.
#dialog refers to a chat function in dialog.py
class InhabitedTile(MapTile):
    def __init__(self, x, y, npc_list, description, dialog):
        self.x = x
        self.y = y
        self.description = description
        self.dialog = dialog
        self.npc_list = npc_list
        
    def intro_text(self):
        text = self.description
        return text
    
    def dialog_tree(self):
        print(self.dialog)
      
"""
Victory tile
* This tile ends the game.
-------------------------------------------------------------------------------
"""
#Ends the game.    
class VictoryTile(MapTile):
    def __init__(self, x, y, description):
        self.x = x
        self.y = y
        self.description = description
        
    def modify_player(self, player):
        player.victory = True
    
    def intro_text(self):
        text = self.description
        return text
"""
-------------------------------------------------------------------------------
"""
"""
Puzzle tiles below
-------------------------------------------------------------------------------
"""
#Contains a riddle or something. When the player enters the correct word or phrase, they get a reward.
class PuzzleTile(MapTile):
    
    def __init__(self, x, y, puzzle_start_text, puzzle_question_text, puzzle_password, reward_item):
        self.x = x
        self.y = y
        
        self.reward_item = reward_item
        
        self.puzzle_start_text = puzzle_start_text
        self.puzzle_question_text = puzzle_question_text
        self.puzzle_password = puzzle_password
        
        self.puzzle_solved = False
    
    def distribute_reward(self, player):          
        reward_item_type = self.reward_item.type
        
        if reward_item_type in ['helmet', 'chest', 'pants', 'boots', 'sheild']:
            main_search_inventory = player.inventory.armor_inventory
        else:
            main_search_inventory = player.inventory.inventory_index
        for sub_inventory in main_search_inventory:
            if sub_inventory.acceptable_class == reward_item_type:
                selected_inventory = sub_inventory
        
        if len(selected_inventory.ls) >= selected_inventory.max_length:
            print("You see a {}, but you can't carry any more.\nDo you want to swap it for something?".format(self.reward_item.name))
            
            while True:
                user_input = input("[Y/N]: ")
                
                if user_input in ['N', 'n']:
                    print("You leave the {}.".format(self.reward_item.name))
                    return
                
                elif user_input in ['Y', 'y']:
                    for i, item in enumerate(selected_inventory.ls, 1):
                        print("\n" + ("- " * 3) + "{}. {}".format(i, item.name))
                   
                    while True:
                        #We ask the player to choose an item by referencing it's number in the list.
                        user_input = input("\n" + ("- " * 3) + "Choose an item: ")
                        #If the user chooses to quit, we return.
                        try:
    
                            #We assign the player's choice to a variable
                            player_choice = int(user_input)
                            chosen_item = selected_inventory.ls[player_choice - 1]
                            
                            selected_inventory.ls.remove(chosen_item)
                            selected_inventory.ls.append(self.reward_item)
                            print("You picked up the {}!".format(self.reward_item.name))
                            self.puzzle_solved = True
                            return
                                
                        except ValueError:
                            print("Invalid choice!")
                
                else:
                    pass            
        else:
            selected_inventory.ls.append(self.reward_item)
            print("You receive {}".format(self.reward_item.name))
            self.puzzle_solved = True
            return
            
    def initiate_puzzle(self, player):
        while not self.puzzle_solved:
            print(self.puzzle_start_text)
            print(self.puzzle_question_text)
            ans = input("Answer (Q to quit): ").lower()
            
            if ans in ['q', 'Q']:
                print("\nYou leave.")
                return
            
            elif ans != self.puzzle_password:
                print("\nIncorrect!")                
            
            else:
                print("\nCorrect!")
                self.puzzle_solved = True
                self.distribute_reward(player)
                           
        

#-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --                 

#This tile class provides clues to help players solve a puzzle tile.
class ClueTile(MapTile):
    def __init__(self, x, y, description):
        self.x = x
        self.y = y
        self.description = description
        
    def intro_text(self):
        text = self.description
        return text
    
    #Triggered from the player class.    
    def look_around(self):
        print("\n" + ("- " * 3) + "What do you want to examine? \n1: A little knickknack\n2: A boombox\n3: A funny smell")
        ans = input("\nPick: ")
        
        #Gives the player a few options to choose from. One contains a clue to help a corresponding puzzle.
        if ans == "1":
            print("\n" + ("- " * 3) + "A little glass bowl gleams on a shelf.")
        elif ans == "2":
            print("\n" + ("- " * 3) + "A song plays...'Baby don't hurt me...'")
        elif ans == "3":
            print("\n" + ("- " * 3) + "There's a poop in the corner of the room")
        else:
            print("INVALID")
        

"""
-------------------------------------------------------------------------------
"""
"""
QuestTiles below
-------------------------------------------------------------------------------
"""
#A tile that contains a quest giver. The npc wants an item. When they get it, the player is rewarded.
class QuestTile(MapTile):
    
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
            
#------------------------------------------------------------------------------
#This tile blocks player from moving if they do not possess a corresponding key item.
#Otherwise, if player possess the corresponding key, the tile move them forward - and lock behind them. Player can open it again, as long as they keep the key.
class LockedRoom(MapTile):
    
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
                    
#------------------------------------------------------------------------------
#This tile is ALWAYS located at y-1 or y+1 relative to its corresponging LockedRoom tile.
#Example: If LockedRoom's coordinates are (1, 2), SimpleTile's coordinates MUST be either (1, 1) or (1, 3)
class SimplePassage(MapTile):
    
    def __init__(self, x, y, description):
        self.x = x
        self.y = y
        self.description = description
        
    def intro_text(self):
        text = self.description
        return text
        
"""
Loot tiles below
-------------------------------------------------------------------------------
"""

#These tiles trigger as soon as the player enters the tile. They either give gold or an item.
class FindGoldTile(MapTile):
    def __init__(self, x, y, gold_amount, first_description, last_description):
        self.x = x
        self.y = y
        self.gold_amount = gold_amount
        self.first_description = first_description
        self.last_description = last_description
        #Once triggered, this will flip to True so the player cannot get items infintely.
        self.gold_claimed = False
    
    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold_amount
            print("\n" + ("- " * 3) + "+{} gold added.".format(self.gold_amount))
            
    def intro_text(self):
        if self.gold_claimed:
            return self.last_description
        
        else:
            return self.first_description
        
#-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --                             
class FindItemTile(MapTile):
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
                                print("You found {} (Protection: {})!\nDo you want to swap it for your {} (Protection: {})? [Y / N]".format(self.item.name, self.item.protection, selected_slot.ls[0].name, selected_slot.ls[0].protection ) )
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
            
        
"""
-------------------------------------------------------------------------------
"""
"""
Trader tiles below
-------------------------------------------------------------------------------
"""
class TraderTile(MapTile):

    def __init__(self, x, y, trader, description):
        self.x = x
        self.y = y
        self.trader = trader
        self.description = description

    def intro_text(self):
        return self.description
    
    #--------------------------------------------------------------------------
    #This function runs if the player chooses to take the buyer's role in the transaction.
    def player_is_buying(self, player):
        for i, item in enumerate(self.trader.inventory, 1):
            print("\n" + ("- " * 3) + "{}. {} - {} Gold".format(i, item.name, item.value))
           
        while True:
            #We ask the player to choose an item by referencing it's number in the list.
            user_input = input("\n" + ("- " * 3) + "Choose an item or press Q to exit: ")
            #If the user chooses to quit, we return.
            if user_input in ['q', 'Q']:
                return
            else:
                try:
                    #We assign the player's choice to a variable
                    player_choice = int(user_input)
                    chosen_item = self.trader.inventory[player_choice - 1]
                    #We assign the chosen item's type to a unique variable
                    chosen_item_type = chosen_item.type
                    
                    #We perform a check to see if the chosen item is a piece of armor or another type of item.
                    if not chosen_item_type in ['sheild', 'helmet', 'pants', 'chest', 'gauntlets', 'boots']:
                        inventory_index = player.inventory.inventory_index
                    else:
                        inventory_index = player.inventory.armor_inventory
                    
                    #If the chosen item is priced higher than the player's inventory, we tell the player and return.
                    if chosen_item.value > player.gold:
                        print("That's too expensive!")
                        return

                    #If the player has enough money...
                    else:
                        #We find the correct inventory...
                        for slot in inventory_index:
                            if not slot.acceptable_class == chosen_item_type:
                                continue
                            else:
                                #And check to see if there's available space...
                                if not len(slot.ls) > slot.max_length:
                                    #We give money to the trader...
                                    player.gold -= chosen_item.value
                                    self.trader.gold += chosen_item.value
                                    #Then we exchange the item...
                                    slot.ls.append(chosen_item)
                                    self.trader.inventory.remove(chosen_item)
                                    print("You purchased {}!".format(chosen_item.name))
                                    return
                                else:
                                    print("You can't carry any more!")
                                    return
                                
                #If the player is an idiot, we let them try again.   
                except ValueError:
                    print("Invalid choice!")

    #--------------------------------------------------------------------------                    
    def player_is_selling(self, player):
        #We establish a counter variable. This will correctly enumerate the list of inventory options.
        counter = 0
        #We list the available inventories
        for i, item in enumerate(player.inventory.inventory_index, 1):
            print("\n" + ("- " * 3) + "{}. {}".format(i, item.name))
            counter += 1
        #We also list the armor inventory        
        print("\n" + ("- " * 3) + "{}. Armor Inventory".format(counter+1))
            
        #We ask the player to choose an inventory by referencing its number in the list.
        user_input = input("\n" + ("- " * 3) + "Choose an inventory or press Q to exit: ")
        try:
            if user_input in ['q', 'Q']:
                return
            else:
                player_choice = int(user_input)
                #If the player does not choose the armor inventory...
                if not player_choice == (counter+1):
                    #The number the player selects takes on the chosen_inventory variable.
                    chosen_inventory = player.inventory.inventory_index[player_choice - 1]
                    #We check to make sure the chosen inventory isn't empty...
                    if not chosen_inventory.ls:
                        #If it's empty, we alert the player and move on.
                        print("\n" + ("- " * 3) + "There's nothing to sell!")
                        return
                    else:
                        #If it's not empty, we keep going.
                        pass
                        
                    
                #If the player DOES choose the armor inventory...
                else:
                    #We open a display of available slots...
                    for i, item in enumerate(player.inventory.armor_inventory, 1):
                        print("\n" + ("- " * 3) + "{}. {}".format(i, item.name))
                    
                    #We ask the player for a selection...
                    user_input_two = input("\n" + ("- " * 3) + "Choose a slot or press Q to exit: ")
                    try:
                        if user_input_two in ['q', 'Q']:
                            return
                        else:
                            player_choice = int(user_input_two)
                            #The number the player chooses becomes the chosen_inventory variable.
                            chosen_inventory = player.inventory.armor_inventory[player_choice - 1]
                            if not chosen_inventory.ls or (len(chosen_inventory.ls) == 0):
                                #If it's empty, we alert the player and move on.
                                print("\n" + ("- " * 3) + "There's nothing to sell!")
                                return
                            else:
                                pass
                           
                    except ValueError:
                        print("Invalid choice!")
                        return
                    
        except ValueError:
            print("Invalid choice!")
            return
                        
        
        #Once the user has made their inventory selction - now assigned to the CHOSEN_INVENTORY variable...   
        while True:
            for i, item in enumerate(chosen_inventory.ls, 1):
                print("\n" + ("- " * 3) + "{}. {} - {} Gold".format(i, item.name, item.value))
            #We ask the player to choose an item by referencing its number in the list.
            user_input = input("\n" + ("- " * 3) + "Choose an item or press Q to exit: ")
            #If the user chooses to quit, we return.
            if user_input in ['q', 'Q']:
                return
            else:
                try:
                    #We assign the player's choice to a variable
                    player_choice = int(user_input)
                    chosen_item = chosen_inventory.ls[player_choice - 1]
                    
                    #We check to see if the item is salable...
                    if not chosen_item.salable:
                        print("You can't sell this item!")
                        return
                    else:
                        pass
                    
                    #We check to see if the trader has enough money to buy the item...
                    if chosen_item.value >= self.trader.gold:
                        print("The trader cannot afford this item!")
                        return
                    else:
                        pass
                    

                    #If the trader has sufficient funds and the item is salable...
                    #We remove the item from the player's inventory...
                    chosen_inventory.ls.remove(chosen_item)
                    #We give the item to the trader...
                    self.trader.inventory.append(chosen_item)
                    #We give the player the appropriate amount of gold...
                    player.gold += chosen_item.value
                    #We subtract that value from the trader's gold supply...
                    self.trader.gold -= chosen_item.value
                    #And we alert the player that the transaction has occured.
                    print("\n" + ("- " * 3) + "You recieved {} gold!".format(chosen_item.value))
                    return
                    
                    
                #If the player is an idiot, we let them try again.   
                except ValueError:
                    print("Invalid choice!")
                    return
                
    #--------------------------------------------------------------------------
    def check_if_trade(self, player):
        while True:
            print("\n" + ("- " * 3) + "Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input("\n" + ("- " * 3) + "Choice: ")
            if user_input in ['b', 'B']:
                self.player_is_buying(player)
            if user_input in ['s', 'S']:
                self.player_is_selling(player)
            if user_input in ['q', 'Q']:
                return
"""
-------------------------------------------------------------------------------
"""
"""
Enemy tiles below
-------------------------------------------------------------------------------
"""
class SingleEnemyTile(MapTile):
    def __init__(self, x, y, enemy, alive_text, dead_text):
        self.x = x
        self.y = y
        self.enemy = enemy
        self.alive_text = alive_text
        self.dead_text = dead_text
        
    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text
    
    def contains(self, list, filter):
        for x in list:
            if filter(x):
                return True
        return False            
    
    def modify_player(self, player):
        if self.enemy.is_alive():
            try:
                #If the player has armor, this block of code calculates how much it protects the player from enemy damage.
                ##Damage is reduced by one percent, per armor point.
                if player.armor > 0:
                    x = player.armor
                    x = 100 - x
                    x = (x * 0.01)
                    self.enemy.damage = (self.enemy.damage*x)
                    player.hp = player.hp - self.enemy.damage
                    print("\n" + ("- " * 3) + "Enemy does {:.0f} damage. You have {:.0f} HP remaining.".format(self.enemy.damage, player.hp))
                    #The next two lines reset the enemy's damage, so that when the combat loop runs again, the damage remains consistent. 
                    self.enemy.damage = (self.enemy.damage / x)
                    self.enemy.damage = (int(round(self.enemy.damage)))
                else:
                    #If the player has no armor, we simple subtract enemy damage from player hp.
                    player.hp = player.hp - self.enemy.damage
                    print("\n" + ("- " * 3) + "Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, player.hp))
            except ValueError:
                print("Something happened. I don't know.")  

#-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
class RandomEnemyTile(MapTile):
    def __init__(self, x, y, Enemy1, Enemy2, Enemy3, Enemy4,
                 enemy1_alive_text, enemy1_dead_text, 
                 enemy2_alive_text, enemy2_dead_text,
                 enemy3_alive_text, enemy3_dead_text,
                 enemy4_alive_text, enemy4_dead_text):
        import random
        r = random.random()
        self.x = x
        self.y = y
        self.enemy1 = Enemy1
        self.enemy2 = Enemy2
        self.enemy3 = Enemy3
        self.enemy4 = Enemy4
        self.enemy1_alive_text = enemy1_alive_text
        self.enemy1_dead_text = enemy1_dead_text
        self.enemy2_alive_text = enemy2_alive_text
        self.enemy2_dead_text = enemy2_dead_text
        self.enemy3_alive_text = enemy3_alive_text
        self.enemy3_dead_text = enemy3_dead_text
        self.enemy4_alive_text = enemy4_alive_text
        self.enemy4_dead_text = enemy4_dead_text
        
        if r < 0.50:
            self.enemy = self.enemy1
            self.alive_text = enemy1_alive_text
            self.dead_text = enemy1_dead_text
        elif r < 0.80:
            self.enemy = self.enemy2
            self.alive_text = enemy2_alive_text
            self.dead_text = enemy2_dead_text
        elif r < 0.95:
            self.enemy = self.enemy3
            self.alive_text = enemy3_alive_text
            self.dead_text = enemy3_dead_text
        else:
            self.enemy = self.enemy4
            self.alive_text = enemy4_alive_text
            self.dead_text = enemy4_dead_text
            
    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text
        
    def modify_player(self, player):
        if self.enemy.is_alive():
            try:
                #If the player has armor, this block of code calculates how much it protects the player from enemy damage.
                ##Damage is reduced by one percent, per armor point.
                if player.armor > 0:
                    x = player.armor
                    x = 100 - x
                    x = (x * 0.01)
                    self.enemy.damage = (self.enemy.damage*x)
                    player.hp = player.hp - self.enemy.damage
                    print("\n" + ("- " * 3) + "Enemy does {:.0f} damage. You have {:.0f} HP remaining.".format(self.enemy.damage, player.hp))
                    #The next two lines reset the enemy's damage, so that when the combat loop runs again, the damage remains consistent. 
                    self.enemy.damage = (self.enemy.damage / x)
                    self.enemy.damage = (int(round(self.enemy.damage)))
                else:
                    #If the player has no armor, we simple subtract enemy damage from player hp.
                    player.hp = player.hp - self.enemy.damage
                    print("\n" + ("- " * 3) + "Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, player.hp))
            except ValueError:
                print("Something happened. I don't know.")
                
#-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
#This enemytile class can have two enemies. They can be Man type or Monster type.
class MultiEnemyTile(MapTile):
    def __init__(self, x, y, enemy1, enemy2,
                 one_two_alive_text, one_alive_two_dead_text,
                 one_dead_two_alive_text, one_two_dead_text):
        self.x = x
        self.y = y
        #the next line is to keep the game from crashing. We'll sort this out once we make the dsl accept instances.
        self.enemy1 = enemy1
        self.enemy2 = enemy2
        self.one_two_alive_text = one_two_alive_text
        self.one_alive_two_dead_text = one_alive_two_dead_text
        self.one_dead_two_alive_text = one_dead_two_alive_text
        self.one_two_dead_text = one_two_dead_text
    
    #The intro text will change depending on the order enemies die.    
    def intro_text(self):
        if self.enemy1.is_alive() and self.enemy2.is_alive():
            text = self.one_two_alive_text
        elif self.enemy1.is_alive() and not self.enemy2.is_alive():
            text = self.one_alive_two_dead_text
        elif not self.enemy1.is_alive() and self.enemy2.is_alive():
            text = self.one_dead_two_alive_text
        else:
            text = self.one_two_dead_text
        return text
    
    #When the player enters the tile, both enemies attack simultaneously.     
    def modify_player(self, player):
        if self.enemy1.is_alive() or self.enemy2.is_alive():
            try:
                #This happens if both enemies are alive.
                if self.enemy1.is_alive() and self.enemy2.is_alive():
                    try:
                        if player.armor > 0:
                            #enemy1 attacks
                            x = player.armor
                            x = 100 - x
                            x = (x * 0.01)
                            self.enemy1.damage = (self.enemy1.damage*x)
                            player.hp = player.hp - self.enemy1.damage
                            print("\n" + ("- " * 3) + "{} does {:.0f} damage. You have {:.0f} HP remaining.".format(self.enemy1.name, self.enemy1.damage, player.hp))
                            #The next two lines reset the enemy's damage, so that when the combat loop runs again, the damage remains consistent. 
                            self.enemy1.damage = (self.enemy1.damage / x)
                            self.enemy1.damage = (int(round(self.enemy1.damage)))
                            
                            #enemy2 attacks
                            x = player.armor
                            x = 100 - x
                            x = (x * 0.01)
                            self.enemy2.damage = (self.enemy2.damage*x)
                            player.hp = player.hp - self.enemy2.damage
                            print("\n" + ("- " * 3) + "{} does {:.0f} damage. You have {:.0f} HP remaining.".format(self.enemy2.name, self.enemy2.damage, player.hp))
                            #The next two lines reset the enemy's damage, so that when the combat loop runs again, the damage remains consistent. 
                            self.enemy2.damage = (self.enemy2.damage / x)
                            self.enemy2.damage = (int(round(self.enemy2.damage)))
                        else:
                            #If the player has no armor, we simple subtract enemy damage from player hp.
                            player.hp = player.hp - self.enemy1.damage
                            print("\n" + ("- " * 3) + "{} does {} damage. You have {} HP remaining.".format(self.enemy2.name, self.enemy1.damage, player.hp))
                            player.hp = player.hp - self.enemy2.damage
                            print("\n" + ("- " * 3) + "{} does {} damage. You have {} HP remaining.".format(self.enemy2.name, self.enemy2.damage, player.hp))
                    except ValueError:
                        print("Something happend in World.MultiEnemyTile when both enemies are alive.")
                        
                #This happens if enemy1 is alive and enemy2 is dead.        
                elif self.enemy1.is_alive() and not self.enemy2.is_alive():
                    try:
                        if player.armor > 0:
                            #enemy1 attacks
                            x = player.armor
                            x = 100 - x
                            x = (x * 0.01)
                            self.enemy1.damage = (self.enemy1.damage*x)
                            player.hp = player.hp - self.enemy1.damage
                            print("\n" + ("- " * 3) + "{} does {:.0f} damage. You have {:.0f} HP remaining.".format(self.enemy1.name, self.enemy1.damage, player.hp))
                            #The next two lines reset the enemy's damage, so that when the combat loop runs again, the damage remains consistent. 
                            self.enemy1.damage = (self.enemy1.damage / x)
                            self.enemy1.damage = (int(round(self.enemy1.damage)))
                        else:
                            #If the player has no armor, we simple subtract enemy damage from player hp.
                            player.hp = player.hp - self.enemy1.damage
                            print("\n" + ("- " * 3) + "{} does {} damage. You have {} HP remaining.".format(self.enemy1.name, self.enemy1.damage, player.hp))
                    except ValueError:
                        print("Something happend in World.MultiEnemyTile when enemy1 is alive and enemy2 is dead.")
                
                #This happensif enemy1 is dead and enemy2 is alive.
                elif not self.enemy1.is_alive() and self.enemy2.is_alive():
                    try:
                        if player.armor > 0:
                            #enemy2 attacks
                            x = player.armor
                            x = 100 - x
                            x = (x * 0.01)
                            self.enemy2.damage = (self.enemy2.damage*x)
                            player.hp = player.hp - self.enemy2.damage
                            print("\n" + ("- " * 3) + "{} does {:.0f} damage. You have {:.0f} HP remaining.".format(self.enemy2.name, self.enemy2.damage, player.hp))
                            #The next two lines reset the enemy's damage, so that when the combat loop runs again, the damage remains consistent. 
                            self.enemy2.damage = (self.enemy2.damage / x)
                            self.enemy2.damage = (int(round(self.enemy2.damage)))
                        else:
                            player.hp = player.hp - self.enemy2.damage
                            print("\n" + ("- " * 3) + "{} does {} damage. You have {} HP remaining.".format(self.enemy2.name, self.enemy2.damage, player.hp))
                    except ValueError:
                        print("Something happend in World.MultiEnemyTile when both enemies are alive.")
                        
                else:
                    pass
            except ValueError:
                print("Something happened in World.MultiEnemyTile.")
                
#-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
#This maptile class uses an man enemy class as the enemy.               
class ManTile(MapTile):
    def __init__(self, x, y, man_enemy, alive_text, dead_text):
        self.x = x
        self.y = y
        self.man_enemy = man_enemy
        self.alive_text = alive_text
        self.dead_text = dead_text
        self.enemy_damage = self.enemy.calc_damage()
        self.enemy_armor = self.enemy.armor_check()
        
    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text
    
    #This is a little function that's used in the modify_player function to...?
    def contains(self, list, filter):
        for x in list:
            if filter(x):
                return True
        return False                    
    
    def modify_player(self, player):
        if self.enemy.is_alive():
            try:
                #If the player has armor, this block of code calculates how much it protects the player from enemy damage.
                ##Damage is reduced by one percent, per armor point.
                if player.armor > 0:
                    x = player.armor
                    x = 100 - x
                    x = (x * 0.01)
                    self.enemy.damage = (self.enemy.damage*x)
                    player.hp = player.hp - self.enemy.damage
                    print("\n" + ("- " * 3) + "Enemy does {:.0f} damage. You have {:.0f} HP remaining.".format(self.enemy.damage, player.hp))
                    #The next two lines reset the enemy's damage, so that when the combat loop runs again, the damage remains consistent. 
                    self.enemy.damage = (self.enemy.damage / x)
                    self.enemy.damage = (int(round(self.enemy.damage)))
                else:
                    #If the player has no armor, we simple subtract enemy damage from player hp.
                    player.hp = player.hp - self.enemy.damage
                    print("\n" + ("- " * 3) + "Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, player.hp))
            except ValueError:
                print("Something happened. I don't know.")
        
"""
-------------------------------------------------------------------------------
"""    