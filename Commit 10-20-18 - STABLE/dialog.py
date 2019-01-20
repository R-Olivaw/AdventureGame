# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 16:20:43 2018

@author: Alex
"""
class TestDialog():    
    def activate(npc_list):
        print("\nYou see two people. Who do you want to speak with?\n\n1. {}\n2. {}".format(npc_list[0].name, npc_list[1].name))
        ans = input("\nAnswer: ")
    
        if ans == '1':
            print("\nYou turn to {}. {} smiles and farts.".format(npc_list[0].name, npc_list[0].pronoun.capitalize()))
            print("\n'Since the accident, I no talk good.'")
            choice = input("\n1: 'How'd you hurt yourself?'\n2: 'Did you just do what I think you did?'\n3: 'Goodbye.'\n\nAnswer: ")
    
            if choice == '1':
                print("\n{} farts.\n\n'How did I what my what?', {} asks.".format(npc_list[0].name, npc_list[0].pronoun))
                return
            elif choice == '2':
                print("\n{} nods, grimaces, farts again.".format(npc_list[0].name))
                return
            elif choice == '3':
                print("\n{} waves and farts.".format(npc_list[0].name))
                return
            else:
                print("\nINVALID!")
                return
    
        if ans == '2':
            print("\nYou say hello to {}.\n\n{} smiles.".format(npc_list[1].name, npc_list[1].pronoun.capitalize()))
            print("\n'Nice day, isn't it', {} asks.".format(npc_list[1].pronoun))
            choice = input("\n1: 'Yes, it is!'\n2: 'No, it is not.'\n3. 'I do not wish to speak with ye, wench!'\n\nAnswer: ")
    
            if choice == '1':
                print("\n'Shame there's nothing to do...' {} says.".format(npc_list[1].name))
                return
            elif choice == '2':
                print("\n'Perfect weather to stay indoors...' {} says.".format(npc_list[1].name))
                return
            elif choice == '3':
                print("\n'Oh my...No one's talked to me like that in a long time...' {} says.".format(npc_list[1].name))
                return
            else:
                print("\nINVALID!")
                return
    
        else:
            print("\nINVALID!")
            return