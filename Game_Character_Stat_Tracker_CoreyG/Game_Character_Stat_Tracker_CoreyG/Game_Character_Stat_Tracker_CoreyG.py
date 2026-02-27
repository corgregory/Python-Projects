"""
In this lab, you'll build a game character stats tracker. The program will allow you to create a character with specific attributes, update those attributes, and retrieve the current stats of the character.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

Create a class named GameCharacter that represents a game character and manages character stats.

When instantiated, a new GameCharacter object should have the following attributes:

_name set to the string given at the moment of the instantiation.
_health set to 100.
_mana set to 50.
_level set to 1.
Create a name property for read-only access to the character's name.

For the health property:

Define a getter that returns the current health.
Define a setter that prevents health from being set below 0, and caps the health at 100.
For the mana property:

Define a getter that returns the current mana.
Define a setter that prevents mana from being set below 0, and caps the mana at 50.
Create a getter for level to return the character's current level.

Define a method named level_up that:

Increases the character's level by 1.
Resets health to 100 and mana to 50 using their corresponding property setters.
Prints a message in the form of <name> leveled up to <level>! (where <name> and <level> should be replaced by the character's name and new level, respectively).
Define a __str__ method that returns a formatted string including:

The character's name.
The character's level.
The character's current health.
The character's current mana.
For example, a character named Kratos, right after the instantiation, should be represented as the following:

Name: Kratos
Level: 1
Health: 100
Mana: 50

"""




# I start do build my character class wiith its attributes.
#I had to remind myself here that only self and name are parameters
# because the game internally sets the default values for health mana and level
class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

# my name property will diplay "this" characters name
    @property
    def name(self):
        print(self._name)

# my health property returns the current value for health stat
    @property
    def health(self):
        return self._health
#the health  setter will make sure the health value is in a valid range,
#defaults to 0 or 100 if the value is less than 0 or greater than 100
#other wise it accepts the valid value as the stat value
    @health.setter
    def health(self,value):
        if value < 0:
            self._health = 0
        elif value > 100:
            self._health = 100
        else:
            self._health = value


# mana property gets the value for the mana stat
    @property
    def mana(self):
        return self._mana

# the mana setter defaults the value to 0 if its less than or defaults to
# 50 if the value is greater than otherwise it sets it to the value input
    @mana.setter
    def mana(self,value):
        if value < 0:
            self._mana = 0
        elif value > 50:
            self._mana = 50
        else:
            self._mana = value


# the level property gets the current level of the character
    @property        
    def level(self):
        return self._level


# the level up method adds one to the character lvl, reset the stats and
# prints a msg showing the character name and new lvl
    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self._name} leveled up to {self._level}!")

# my str method formats the chracter info to fufill the requirements for this lab
    def __str__(self):
        return f"Name: {self._name}\nLevel: {self._level}\nHealth: {self._health}\nMana: {self._mana}"


#test calls
hero = GameCharacter('Kratos')
print(hero)

hero.health -= 30
hero.mana -= 10
print(hero)

hero.level_up()
print(hero)
