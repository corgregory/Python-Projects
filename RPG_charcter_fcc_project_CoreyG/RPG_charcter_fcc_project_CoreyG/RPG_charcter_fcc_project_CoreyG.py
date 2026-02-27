"""
Build an RPG Character
In this lab you will practice the basics of Python by building a small app that creates a character for an RPG adventure.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

You should have a function named create_character.
The function should accept, in order, a character name followed by three stats: strength, intelligence, and charisma.
The character name should be validated:
If the character name is not a string, the function should return The character name should be a string.
If the character name is an empty string, the function should return The character should have a name.
If the character name is longer than 10 characters, the function should return The character name is too long.
If the character name contains spaces, the function should return The character name should not contain spaces.
The stats should also be validated:
If one or more stats are not integers, the function should return All stats should be integers.
If one or more stats are less than 1, the function should return All stats should be no less than 1.
If one or more stats are more than 4, the function should return All stats should be no more than 4.
If the sum of all stats is different than 7, the function should return The character should start with 7 points.
If all values pass the verification, the function should return a string with four lines:
the first line should contain the character name
lines 2-4 should start with the stat abbreviation, STR, INT or CHA (in this order), then a space, and then a number of full dots (●) equal to the value of the stat, and a number of empty dots (○) to reach 10. Example: if the value of strength is 3 there must be 3 full dots followed by 7 empty dots. The dots are given in the editor.
Here's the string that should be returned by create_character('ren', 4, 2, 1):

ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
"""

#This project has a checklist to make sure each of the "user stories" are fulfilled.
#I used w3 schools, stack over flow, and forums on FCC website to help me finish this project.

# the full dot and empty dot variables were provided in the project
full_dot = '●'
empty_dot = '○'

#I decided to put the name verification in its own function to clean up the code
#This function helps secure input validation but checking that the name meets requirements.
def verify_name(name):
    if not isinstance(name, str):
        return "The character name should be a string"
    if "" == name:
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"


# this function will verify the values of 3 stats for a character
# this function wasnt working properly at first because I had to take the 
# stats and place them into a list so I can iterate thru each one
def verify_stats(strength,intelligence,charisma):   
    Cstats = [strength, intelligence, charisma]  
    if not all(isinstance(stat,int) for stat in Cstats):
        return "All stats should be integers" 
    if any(stat < 1 for stat in Cstats):
        return "All stats should be no less than 1"
    if any(stat > 4 for stat in Cstats):
        return "All stats should be no more than 4"
    if sum(Cstats) != 7:
        return "The character should start with 7 points"

#this function creates your character and also uses the verify_stats and
#verify_name functions to make sure the information about the character is Valid input
def create_character(character_name, strength,  intelligence, charisma):
    name = verify_name(character_name)
    if name:
        return name
    stats = verify_stats(strength, intelligence, charisma)
    if stats:
        return stats
    def stat_bar(value):
        #this formula is to display the correct number of solid and empty dots
        #based on the stat number for each stat
        return full_dot * value + empty_dot * (10 - value)

    result = f"{character_name}\n"
    result += f"STR {stat_bar(strength)}\n"
    result += f"INT {stat_bar(intelligence)}\n"
    result += f"CHA {stat_bar(charisma)}"
    return result

    

print(create_character('ren',4,2,1))

