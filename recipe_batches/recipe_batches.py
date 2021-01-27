#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  pass
  #fin the ingredians
  #print(recipe.keys())
  things_needed = []
  cam_make = []
  for x in recipe.keys():
      things_needed.append(x)
  #print(things_needed)
  #print(recipe[things_needed[0]])

  # NEED: how much the recipe needs
  # HAVE : how much of the ingreediant you have
  #CAN_MAKE : min value for have/need
  for i in things_needed:
      try:
          cam_make.append( ingredients[i] // recipe[i] )
      except KeyError: # to address no ingreadint in have list
          cam_make.append( 0 )

  #print(print(f"CAN MAKE: {cam_make}"))
  return sorted(cam_make)[0]


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
