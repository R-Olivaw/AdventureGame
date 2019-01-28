# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 17:27:18 2019

@author: Alexa
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


class SteveTile(MapTile):
    def __init__(self, x, y, npc_list, description):
        self.x = x
        self.y = y
        self.description = description
        self.npc_list = npc_list
        
    def intro_text(self):
        text = self.description
        return text
    
    def dialog_tree(self):
        import utilities
        print(utilities.boxer.make_text_box("\n'I'm crazy Steve!'\n\n"))
        
        convo_over = False
        
        while not convo_over:
            print("\n1. 'Please don't hurt me!'\n2. 'I'll hurt you!'\n3. 'Whatever, weirdo...'\n")
            ans = input('Answer: ')
            
            if ans == '1':
                print(utilities.boxer.make_text_box("\n'AH HA HA HA HAAAAH!\n\n"))
                convo_over = True
                
            elif ans == '2':
                print(utilities.boxer.make_text_box("\n'AHHHHH!\n\n"))
                convo_over = True
                
            elif ans == '3':
                print(utilities.boxer.make_text_box("\n HA HOO HOO HOO...\n\n"))
                convo_over = True
            else:
                print(utilities.boxer.make_text_box("\n'AUH?'\n\n"))
                