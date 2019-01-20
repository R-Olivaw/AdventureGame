'''
This module contains the Item class, the Consumable class, and all subclasses.

Players can find these items in rooms. They can affect the world through functions in the player module.


'''

#the base class for all items, except consumables. You should never make this class directly! Only subclasses!
class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
        self.salable = True
        
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}".format(self.name, self.description, self.value)
    
"""
Consumable subclasses below
-------------------------------------------------------------------------------
"""
#This is the base class for all consumable items. These items replenish the player's health up to the maximum of 100, per the heal function in the player module.    
class Consumable():
    def __init__(self):
        self.type = 'consumable'
    
    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)
    
class Food(Consumable):
    def __init__(self, name, healing_value, value):
        self.name = name
        self.healing_value = healing_value
        self.value = value
        self.protection = 0
        self.damage = 0
        self.salable = True
        self.type = 'consumable'
        
class HealingPotion(Consumable):
    def __init__(self, name, healing_value, value):
        self.name = name
        self.healing_value = healing_value
        self.value = value
        self.protection = 0
        self.damage = 0
        self.salable = True
        self.type = 'consumable'


"""
Loot classes below (Items with only Value, and no other attributes)
-------------------------------------------------------------------------------
"""

class Loot(Item):
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
        self.protection = 0
        self.damage = 0
        self.salable = True
        self.type = 'loot'
        
    def __str__(self):
        return "{}\n       =====\n       Value: {} Coin".format(self.name, self.value)
        
"""
Quest classes below (Cannot be traded. Have no value.)
-------------------------------------------------------------------------------
"""

class Quest_Object(Item):
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
        self.protection = 0
        self.damage = 0
        self.salable = False
        self.type = 'quest_item'
    
    def __str__(self):
        return "{}\n       =====\n       An interesting object.".format(self.name)

#------------------------------------------------------------------------------
#Every Door_Key instance should have a unique id_code. This id_code should correspond to a LockedRoom's desired_key_id_code.
#Keys are not salable, so once it enters the players inventory, it should be impossible to remove.
class Door_Key(Item):
    def __init__(self, name, description, value, id_code):
        self.name = name
        self.description = description
        self.value = value
        self.id_code = id_code
        self.protection = 0
        self.damage = 0
        self.salable = False
        self.type = 'quest_item'
        self.sub_type = 'key'

"""
Armor classes below
-------------------------------------------------------------------------------
"""

class Armor(Item):
    def __init__(self):
        self.salable = True
    
    def __str__(self):
        return "{}\n       =====\n       {}\n       Value: {}\n       Protection: {}\n       =====\n".format(self.name, self.description, self.value, self.protection)

class Sheild(Armor):
    def __init__(self, name, description, protection, value):
        self.name = name
        self.description = description
        self.value = value
        #MAX PROTECTION: 25
        self.protection = protection
        self.damage = 0
        self.salable = True
        self.type = 'sheild'
        self.type_description = 'a sheild'
        self.pronoun = 'it'
        
class Helmet(Armor):
    def __init__(self, name, description, protection, value):
        self.name = name
        self.description = description
        self.value = value
        #MAX PROTECTION 10
        self.protection = protection
        self.damage = 0
        self.salable = True
        self.type = 'helmet'
        self.type_description = 'a helmet'
        self.pronoun = 'it'
        
class Pants(Armor):
    def __init__(self, name, description, protection, value):
        self.name = name
        self.description = description
        self.value = value
        #MAX PROTECTION 15
        self.protection = protection
        self.damage = 0
        self.salable = True
        self.type = 'pants'
        self.type_description = 'pants'
        self.pronoun = 'them'
        
class Chest(Armor):
    def __init__(self, name, description, protection, value):
        self.name = name
        self.description = description
        self.value = value
        #MAX PROTECTION 30
        self.protection = protection
        self.damage = 0
        self.salable = True
        self.type = 'chest'
        self.type_description = 'a piece of chest armor'
        self.pronoun = 'it'
        
class Gauntlets(Armor):
    def __init__(self, name, description, protection, value):
        self.name = name
        self.description = description
        self.value = value
        #MAX PROTECTION 10
        self.protection = protection
        self.damage = 0
        self.salable = True
        self.type = 'gauntlets'
        self.type_description = 'gauntlets'
        self.pronoun = 'them'
        
class Boots(Armor):
    def __init__(self, name, description, protection, value):
        self.name = name
        self.description = description
        self.value = value
        #MAx PROTECTION 10
        self.protection = protection
        self.damage = 0
        self.salable = True
        self.type = 'boots'
        self.type_description = 'boots'
        self.pronoun = 'them'

"""
Weapon classes below
-------------------------------------------------------------------------------
"""
class Weapon(Item):
    def __init__(self, name, description, value, damage, protection):
        raise NotImplementedError("Do not create raw Weapon objects!")
        self.damage = damage
        self.protection = 0
        super().__init__(name, description, value)
        self.type = 'weapon'
        
    def __str__(self):
        return "{}\n       =====\n       {}\n       Value: {}\n       Damage: {}\n       =====\n".format(self.name, self.description, self.value, self.damage)
    
class Rock(Weapon):
    def __init__(self, name, description, damage, value):
        self.name = name
        self.description = description
        self.damage = damage
        self.value = value
        self.protection = 0
        self.type = 'weapon'
        self.salable = True
 
class Dagger(Weapon):
    def __init__(self, name, description, damage, value):
        self.name = name
        self.description = description
        self.damage = damage
        self.value = value
        self.protection = 0
        self.type = 'weapon'
        self.salable = True
        
class Sword(Weapon):
    def __init__(self, name, description, damage, value):
        self.name = name
        self.description = description
        self.damage = damage
        self.value = value
        self.protection = 0
        self.type = 'weapon'
        self.salable = True
        
class Axe(Weapon):
    def __init__(self, name, description, damage, value):
        self.name = name
        self.description = description
        self.damage = damage
        self.value = value
        self.protection = 0
        self.type = 'weapon'
        self.salable = True

class Torch(Weapon):
    def __init__(self, name, description, damage, value):
        self.name = name
        self.description = description
        self.damage = damage
        self.value = value
        self.protection = 0
        self.type = 'weapon'
        self.salable = True