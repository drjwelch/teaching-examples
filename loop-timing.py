from time import process_time
#import timeit

def A():
    scores = [23000,12000,15000,18000]
    highscore = 0
    num_scores = len(scores)
    for x in range(num_scores):
        if scores[x] > highscore:
            highscore = scores[x]

def B():
    scores = [23000,12000,15000,18000]
    highscore = 0
    for x in scores:
        if x > highscore:
            highscore = x

def C():
    scores = [23000,12000,15000,18000]
    highscore = 0
    scoresleft = True
    pointer = 0
    while scoresleft:
        if scores[pointer]>highscore:
            highscore = scores[pointer]
        pointer = pointer+1
        if pointer == len(scores):
            scoresleft = False

def D():
    scores = [23000,12000,15000,18000]
    highscore = 0
    countdown = len(scores)
    while countdown>0:
        if scores[countdown-1]>highscore:
            highscore = scores[countdown-1]
        countdown = countdown-1

t = process_time()
for i in range(1000000):
    D()
print(process_time() - t)

#t = timeit.Timer("A()")
#print(t.timeit(10000))
#print(timeit.repeat("D()","from __main__ import D"))
