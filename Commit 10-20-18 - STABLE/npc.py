"""

This module contains NPC classes and subclasses.

"""

#This is the base class for NPCs. Do NOT make this class directly!
class NonPlayableCharacter():
    def __init__(self):
        pass
    
    def __str__(self):
        return self.name
    

"""
Trader-type NPCs
-------------------------------------------------------------------------------
"""

class Trader(NonPlayableCharacter):
    #gold is an integer and inventory is a list!
    def __init__(self, name, gender, gold, inventory):
        self.name = name
        self.gold = gold
        self.inventory = inventory
        self.gender = gender
        
        if self.gender == 'male':
            self.pronoun = 'he'
        elif self.gender == 'female':
            self.pronoun = 'she'
        else:
            self.pronoun = 'they'
        
"""
Questgiver-type NPCs
-------------------------------------------------------------------------------
"""
        
class QuestGiver(NonPlayableCharacter):
    def __init__(self, name, gender, gold, inventory):
        self.name = name
        self.gold = gold
        self.inventory = inventory
        self.gender = gender
        
        if self.gender == 'male':
            self.pronoun = 'he'
        elif self.gender == 'female':
            self.pronoun = 'she'
        else:
            self.pronoun = 'they'

"""
Non-essential NPCs
-------------------------------------------------------------------------------
"""

class Villager(NonPlayableCharacter):
    def __init__(self, name, gender, gold, inventory):
        self.name = name
        self.gold = gold
        self.inventory = inventory
        self.gender = gender
        
        if self.gender == 'male':
            self.pronoun = 'he'
        elif self.gender == 'female':
            self.pronoun = 'she'
        else:
            self.pronoun = 'they'

