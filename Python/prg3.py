"""This program is a Class system of monsters. The classes ArmoredMonster and Slime monster both extend the Monster class. Each extension, of monster, has its own ability that
affects how it takes damage. Armored Monsters have 20 armor that works as extra health. Slime Monsters have the ability to become gelatinous to avoid damage. All monster objects
have the ability to make noise, take damage, make an attack sound, and can determine if they dead or alive."""
import random
class Monster:#Monster Class
    def __init__(self,name,noise,attack):#Creates Monster
        self.__name = name
        self.getHealth()
        self.getType()
        self.__noise = noise
        self.__attack = attack

    def make_noise(self):#Prints noise
        print(self.noise)

    def getHealth(self):#Sets inital health
        self.__health = 30
        return self.__health

    def getType(self):#Sets and returns monster type
        self.__type = 'Monster'
        return self.__type

    def isAlive(self):#Returns Boolean value that determines if a monster is dead or alive
        if self.health <= 0:
            return False
        else:
            return True

    def takeDamage(self,x):#Monster takes damage if it is not dead
        health = self.health
        health = health - x
        if health <= 0:#If monster has no health print that it is dead
            self.__health = 0
            print("Monster is dead.")
        else:#If monster is not dead print out its remaining health
            self.__health = health
            print("Health: ",self.health)
            
    @property
    def name(self):
        #Allows usage of self.name as variable and allows you to print the monster's name from repl
        return self.__name
    @property
    def noise(self):
        #Allows usage of self.noise as variable and allows you to print monster's noise from repl
        return self.__noise
    @property
    def attack(self):
        #Allows usage of self.attack as variable and allows you to print the monster's attack from repl
        return self.__attack
    @property
    def type(self):
        #Allows usage of self.type as variable and allows you to print the monster type from repl
        return self.__type
    @property
    def health(self):
        #Allows usage of self.health as variable and allows you to print the health of the monster from repl
        return self.__health
        
class ArmoredMonster(Monster):#Armored Monster Class
    def __init__(self, name,attack):#Creates Armored Monster
        super().__init__(name,'clank',attack)
        self.getHealth()
        self.getArmor()
        self.getType()
        self.getAbility()
        
    def getHealth(self):#Sets inital health
        self.__health = 30
        return self.__health
    
    def getType(self):#Sets and returns monster type
        self.__type = 'Armored Monster'
        return self.__type

    def getArmor(self):#Sets inital armor
        self.__armor = 30
        return self.__armor

    def getAbility(self):#Sets and prints ability
        self.__ability = "Armored Monsters have 20 armor that works as extra health."
        print(self.ability)
        return self.__health

    def takeDamage(self,x):
        health = self.health
        armor = self.armor
        if armor > 0:#Checks if monster still has armor
            if armor >= x:#Checks if armor is greater than damage
                self.__armor = (armor - x)#If so damage is dealt to only armor
                self.__health = 30
                print("Armor: ", self.__armor)#Prints remaining armor
                print("Health: ",self.__health)#Prints remaining health
            else:#If armor is less than damage
                x = (x - armor)#Remove remaining armor from damage
                health = (health - x)#Take remaining damage to health
                if health <= 0:#If health is zero or below Monster is dead
                    self.__health = 0
                    self.__armor = 0
                    print("Monster is dead.")
                else:#Print remaining healh
                    self.__health = health
                    self.__armor = 0
                    print("Health: ",self.__health)
        else:#If monster has no armor
            health = health -x
            #Take damage directly to health
            self.__health = health
            if self.health > 0:#If monster still has health print remaining health
                print("Health: ",self.__health)
            else:#If health is zero or below Monster is dead
                print("Monster is dead.")
    @property
    def health(self):
        #Allows usage of self.health as variable and allows you to print the health of the monster from repl
        return self.__health
    @property
    def armor(self):
        #Allows usage of self.armor as variable and allows you to print the armor of the monster from repl
        return self.__armor
    @property
    def type(self):
        #Allows usage of self.type as variable and allows you to print the monster's type from repl
        return self.__type
    @property
    def ability(self):
        #Allows usage of self.ability as variable and allows you to print the monster's abilities from repl
        return self.__ability
    
class SlimeMonster(Monster):#Slime Monster Class
    def __init__(self, name,attack):#Creates Slime Monster
        super().__init__(name,'gurgle',attack)
        self.getHealth()
        self.getType()
        self.getAbility()

    def getHealth(self):#Sets inital health
        self.__health = 20
        return self.__health
    
    def getType(self):#Sets and returns monster type
        self.__type = 'Slime Monster'
        return self.__type

    def getAbility(self):#Sets and prints ability
        self.__ability = "Slime Monsters have the ability to become gelatinous to avoid damage."
        print(self.ability)
        return self.__health

    def isSolid(self):#Randomly determines a Boolean value that determines if the monster is solid
        a = random.uniform(0,2)#Generates random number between zero and two
        if a < 1:#If a is less than one the monster is solid
            print("Monster is solid and will take damage.")
            return True
        else:#If a is greater or equal to one then the monster is not solid
            print("Monster became gelatinous and did not take damage.")
            return False
            
    def takeDamage(self,x):
        health = self.health
        if self.isSolid():#Checks if monster is solid 
            health = health - x
            #Monster only takes damage if it is solid
            if health <= 0:#If health is zero or below Monster is dead
                self.__health = 0
                print("Monster is dead.")
            else:#If monster is not dead print out its remaining health
                self.__health = health
                print("Health: ",self.__health)
                
    @property
    def health(self):
        #Allows usage of self.health as variable and allows you to print the health of the monster from repl
        return self.__health
    @property
    def type(self):
        #Allows usage of self.type as variable and allows you to print the monster's type from repl
        return self.__type
    @property
    def ability(self):
        #Allows usage of self.ability as variable and allows you to print the monster's abilities from repl
        return self.__ability
    
    
            
