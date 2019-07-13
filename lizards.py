import random

# Subprogram templates - for you to complete :)

def display_populations():
    pass

def update_blue():
    pass

def update_orange():
    pass

def update_yellow():
    pass
    
# Main program

oranges = 50
blues = 20
yellows = 10

lizards = [oranges, blues, yellows]

clock = 0

while sum(lizards) > 0 and clock < 100:

    oranges = update_orange(lizards)
    blues   = update_blue(lizards)
    yellows = update_yellow(lizards)
    
    lizards = [oranges, blues, yellows]
   
    display_populations(lizards)
    
    clock = clock + 1

print("Simulation ended")
