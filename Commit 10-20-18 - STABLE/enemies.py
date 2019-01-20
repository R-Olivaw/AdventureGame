'''
This module contains the enemy class and all subclasses.
'''

#This is the base calss for all enemies. It should never be made directly.
class Enemy:
    def __init__(self):
        #raise NotImplementedError("DO NOT CREATE RAW ENEMIES!")
        pass
    
    def __str__(self):
        return self.name
    
    def is_alive(self):
        return self.hp > 0
    
"""
Monster Enemies
-------------------------------------------------------------------------------
"""        
class BasicMonster(Enemy):
    def __init__(self, name, hp, damage, armor):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armor = armor

"""
Human Enemies
-------------------------------------------------------------------------------
"""

#This is the only enemy class that has weapons or armor.
class Man(Enemy):
    def __init__(self, name, hp, gold, armor, damage, inventory):
        self.name = name
        self.hp = hp
        self.gold = gold
        self.armor = armor
        self.damage = damage
        self.inventory = inventory
        self.best_weapon = None
    
    #If the enemy has more than one weapon, it will attack with the most powerful one.    
    ##Designates the most powerful weapon.
    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        self.best_weapon = best_weapon
    
    #This function checks to see if the man_enemy instance (self) has armor.
    ##Then, it adds up the value of all armor pieces in inventory and assigns that value to the protection variable.    
    def armor_check(self):
        import items
        armor = [item for item in self.inventory if isinstance(item, items.Armor)]
        if not armor:
            pass
        else:
            for item in self.inventory:
                if item.protection:
                    self.armor += item.protection
    
    #This function checks to see if the man_enemy instance (self) has a weapon.
    ##Then, it adds up the value of all armor pieces in inventory and assigns that value to the protection variable.            
    def weapon_check(self):
        import items
        damage = [item for item in self.inventory if isinstance(item, items.Weapon)]
        if not damage:
            pass
        else:
            for item in self.inventory:
                if item.damage:
                    self.damage += item.damage
                    
    #Assign's the most powerful weapon's damage value to the enemy instance's damage value.                
    def calc_damage(self):
        self.most_powerful_weapon()
        self.damage = self.best_weapon.damage
        
                    
    def armor_reset(self):
        self.armor = 0