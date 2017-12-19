import math
import time
import random

randomwoorden = ["beeldscherm", "appel", "peer", "bier", "koffie", "coderclass"] 

woord = random.choice(randomwoorden)
letters = len(woord)

print ("Het woord is : " + (woord))
print ("De lengte van het woord is", (letters), "letters lang!")
