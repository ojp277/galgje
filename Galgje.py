import math
import time
import random
import os


woord = input ("Geef een woord : ")

letters = len(woord)
streepjes = letters * "_ "

os.system('cls')
print ("De lengte van het woord is", (letters), "letters lang!")
print ("Raad het woord : " + streepjes)
time.sleep(10)
