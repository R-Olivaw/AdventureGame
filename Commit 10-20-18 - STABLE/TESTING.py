class new_trader_tile(world.TraderTile):

    def __init__(self, x, y, trader, description):
        self.x = x
        self.y = y
        self.trader = trader
        self.description = description

    def intro_text(self):
        return self.description

    def player_is_selling(self, player):
        pass

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

    def check_if_trade(self, player):
        while True:
            print("\n" + ("- " * 3) + "Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input("\n" + ("- " * 3) + "Choice: ")
            if user_input in ['b', 'B']:
                self.player_is_buying(player)
            if user_input in ['s', 'S']:
                pass
            if user_input in ['q', 'Q']:
                return