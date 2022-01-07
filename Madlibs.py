"""
This program generates passages that are generated in mad-lib format
Author: Deez 
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."
print "it's starting"

name = raw_input("Who? ")
adj1 = raw_input("Adj? ")
adj2 = raw_input("Adj? ")
adj3 = raw_input("Adj? ")
verb = raw_input("Verb? ")
noun1 = raw_input("Noun? ")
noun2 = raw_input("Noun? ")
animal = raw_input("Animal? ")
food = raw_input("Food? ")
fruit = raw_input("Fruit? ")
superhero = raw_input("Superhero? ")
country = raw_input("Country? ")
dessert = raw_input("Dessert? ")
year = raw_input("Year? ")

print STORY % (name, adj1, adj2, animal, food, verb, noun1, fruit, adj3, name, superhero, name, country, name, dessert, name, year, noun2)
