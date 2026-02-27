"""
Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

You should create a class named Planet.
The Planet class should have an __init__ method that:
Has four parameters: self, name, planet_type, and star.
Raises a TypeError with the message name, planet type, and star must be strings if any of the arguments passed in is not a string type.
Raises a ValueError with the message name, planet_type, and star must be non-empty strings if any of the arguments passed in is an empty string.
Assigns the values passed in to the instance attributes name, planet_type, and star.
The Planet class should have an orbit method that returns a string in the format {name} is orbiting around {star}....
The Planet class should have a __str__ method that returns a string in the format Planet: {name} | Type: {planet_type} | Star: {star}.
You should create three instances of the Planet class named planet_1, planet_2, and planet_3.
You should print each planet object to see the __str__ method output.
You should call the orbit method on each planet object and print the result.

"""


# The plane class will be my template for creating 3 planet objects
class Planet:
    def __init__(self, name, planet_type, star):
# to start checking for valid inputs I made a planet_stats variable 
# to group the variables in a list so I can iterate through them to check 
# for valid input
        planet_stats = [name, planet_type, star]
# to get use to cleaner ways of using python I set this part up using the 
# all() functions. I understand I could have just looped through them
#but this way is alot cleaner and more precise.
        if not all(isinstance(stats,str) for stats in planet_stats):
            raise TypeError("name, planet type, and star must be strings")
        if not all(len(stat) > 0 for stat in planet_stats):
            raise ValueError("name, planet_type, and star must be non-empty strings")
        #the self keyword represents the object im working with 
        self.name = name 
        self.planet_type = planet_type
        self.star = star
    # my orbit method will return a string telling what planet is orbiting around what star
    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."
    #my __str__ method gets called behind the scene and returns info about a planet in a certain format.
    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}" 
# I made three instances or objects of class planet to test my code
planet_1 = Planet('earth','rock','sun')
planet_2 = Planet('pluto','dwarf planet', 'sun')
planet_3 = Planet('Jupiter','gas', 'sun')

#print(planet) calls the __str__ method on its own behind the scense to display planet's info
print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
