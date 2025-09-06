# Cake calculator in python

# define a function 

def cake_calculator(available_flour, available_sugar ):
    # define the recipe requirements
   
   flour_per_cake = 100 # units
   sugar_per_cake = 50  # units
   maximum_cakes_by_flour = available_flour // flour_per_cake
   maximum_cakes_by_sugar = available_sugar // sugar_per_cake


# the actual number of cakes is limited by the ingredient in shortest supply
   cakes_made = min(maximum_cakes_by_flour, maximum_cakes_by_sugar)

# let's see what's left in the pantry
   flour_left = available_flour - (cakes_made * flour_per_cake)
   sugar_left = available_sugar - (cakes_made * sugar_per_cake)
  
   return [cakes_made, flour_left, sugar_left]