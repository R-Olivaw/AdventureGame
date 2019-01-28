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
        from utilities import boxer
        print(boxer.make_text_box("\n'Me Steve. This my spot. What you want?'\n\n"))
        
        convo_over = False
        
        while not convo_over:
            print("\n1. 'Is there any food here?'\n2. 'What're you doing here Steve?'\n3. 'Do you know how to get out of here?'\n4. 'Stay away from me, you wretch!'\n")
            ans = input('Answer: ')
            
            #------------------------------------------------------------------
            
            if ans == '1':
                print(boxer.make_text_box("\n'Hmph Mebbe?'\n\n"))
                print("\n1.'So...no?'\n2.'Whatever, man...'\n")
                rep = input('Answer: ')
                
                if rep == '1':
                    print(boxer.make_text_box("\n'Heh he heh...no.'\n\n"))
                    convo_over = True
                    
                elif rep == '2':
                    print(boxer.make_text_box("\n'Heh'\n\n"))
                    convo_over = True
                    
                else:
                    print(boxer.make_text_box("\n'Ahuh?'\n\n"))
                
            #------------------------------------------------------------------
            
            elif ans == '2':
                print(boxer.make_text_box("\n'Steve here to make sure they don't get out!'\n\n"))
                print("\n1. '...so what don't get out?'\n2. 'Ok, good luck with that...'\n\n")
                rep = input('Answer: ')
                
                if rep == '1':
                    print(boxer.make_text_box("\n'The chows...'\n\n"))
                    print("\n1. 'Like the dogs?'\n2. 'Ok, good luck with that!'")
                    con = input('Answer: ')
                    
                    if con == '1':
                        print(boxer.make_text_box("\n'Heh, yeah! Better watch out...'\n\n"))
                        convo_over = True
                    
                    elif con == '2':
                        print(boxer.make_text_box("\n'Oh, I eat 'em when I find 'em...'\n\n"))
                        convo_over = True
                    
                    else:
                        print(boxer.make_text_box("\n'Ahuh?'\n\n"))
                    
                elif rep == '2':
                    print(boxer.make_text_box("\n'Heh heh'\n\n"))
                    convo_over = True
                    
                else:
                    print(boxer.make_text_box("\n'Ahuh?'\n\n"))
                
            #------------------------------------------------------------------
                
            elif ans == '3':
                print(boxer.make_text_box("\n'Heh, you gonna need a sword...'\n\n"))
                print("\n1. 'Why?'\n2. 'Ok, thanks!'")
                con = input('Answer: ')
                
                if con == '1':
                    print(boxer.make_text_box("\n'Can't kill the devil with you hands...'\n\n"))
                    convo_over = True
                
                elif con == '2':
                    print(boxer.make_text_box("\n'Heh heh heh...\n\n"))
                    convo_over = True
                
                else:
                    print(boxer.make_text_box("\n'Ahuh?'\n\n"))
                
                
            #------------------------------------------------------------------
            
            elif ans == '4':
                print(boxer.make_text_box("\n'Arh! What Steve do to you?'\n\n"))
                print("\n1. 'Just stay away from me, you slug.'\n2. 'I'm sorry...'")
                con = input('Answer: ')
                
                if con == '1':
                    print(boxer.make_text_box("\n*HISSS*\n\n"))
                    convo_over = True
                
                elif con == '2':
                    print(boxer.make_text_box("\n*HISSS*\n\n"))
                    convo_over = True
                
                else:
                    print(boxer.make_text_box("\n*HISSS*\n\n"))
                    convo_over = True
            
            #------------------------------------------------------------------
            
            else:
                print(boxer.make_text_box("\n'AUH?'\n\n"))
                
