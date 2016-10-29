import os
from random import randint
from array import *

basket_a = '0010580093' # Basket A - Sticker
basket_b = '0008342310' # Basket B - Non Sticker

basket_a_speak = ['Chocolate comes from cocoa, which is a tree. That makes it a plant. Therefore, chocolate is salad.','Damn, I forgot to go to the gym today. Thats 10 years in a row now...']
basket_b_speak = ['Im learning the hokey cokey. Not all of it. But  Ive got the ins and outs.','Ive got very sensitive teeth. Theyll probably be upset Ive told you.']

while True:

#for x in range(0, 10):

    x = raw_input()

    phrase_n = randint(0,1)

    if x == basket_a:
        
        phrase = basket_a_speak[phrase_n]
        
        os.system("espeak -ven+m1 -k5 -s150 '" + phrase + "'")
    elif x == basket_b:
        
        phrase = basket_b_speak[phrase_n]
        
        os.system("espeak -ven+f1 -k5 -s150 '" + phrase + "'")


    
