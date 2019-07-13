# Hex multiply code (with two bugs)

# For each of the keys before the 'Z'
# convert from hex to denary
# multiply together and store the answer in q
# The right answer for the keys above is in the variable answer
# When the bugs are fixed q==answer

# The code is hard to follow by hand, so use the debugging techniques
# you know to check the steps in the calculation and find where it goes wrong

keys = ('156D4F7A','AA78FC63','Z')
answer = 1028147980876764206

# Both bugs are below this line ... above here is all fine

q = 1
j = 0
while keys[j][0] != 'Z':
    p = 0
    for i in range(len(keys[j])-1):
        p = p*16 + "0123456789ABCDEF".index(keys[j][i+1])
    j += 1
    q *= p

# Both bugs are above this line ... below here is just to stop you cheating!

check = sum([int(x) for x in str(answer) if x in '012345'])

if q==answer and check*answer==14394071732274698884: print("You cracked it!")
else: print("Keep looking ...")
