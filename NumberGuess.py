"""
This is a simple program that compare a users guess to two rolled dice
Author: Larz
"""

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Whats your guess? "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print ("The max possible is %d") % max_val
  guess = get_user_guess()
  if guess > max_val:
    print ("Your guess is invalid")
  else:
    print("Rolling...")
    sleep(2)
    print ("Roll 1: %d") % first_roll
    sleep(1)
    print ("Roll 2: %d") % second_roll
    total_roll = first_roll + second_roll
    print ("Result...")
    sleep(1)
    if guess > total_roll:
      print("This is rigged...")
    else:
      print ("Haha I won")

roll_dice(6) 
