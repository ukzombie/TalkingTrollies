import os
from random import randint
from array import *
import time

basket_a = '0010580093' # Basket A - Sticker
basket_b = '0008342310' # Basket B - Non Sticker

#shopping items
newspaper = '0004002434'
marshmallows = '0001080972'
mint_tea = '0008032566'
rhubarb_and_custard = '0008043331'
energy_drink = '0008035839'
peroni = '0015644579'


baskets_hello = [
    'Oh Hello',
    'Hi There'
]

basket_a_speak = [
    'Chocolate comes from cocoa, which is a tree. That makes it a plant. Therefore, chocolate is salad.',
    'Damn, I forgot to go to the gym today. Thats 10 years in a row now...'
]

basket_b_speak = [
    'Im learning the hokey cokey. Not all of it. But Ive got the ins and outs.',
    'Ive got very sensitive teeth. Theyll probably be upset Ive told you.'
]

baskets_laughs = [
    'Ha Ha Ha Ha Ha Ha Ha',
    'He He He He He He He'
]


while True:

#for x in range(0, 10):

    x = raw_input() # get the input from the keyboard buffer which in our case is the raspberry

    time.sleep(1)

    phrase_n = randint(0,1) # this randonly picks a response

    if x == basket_a:
        
        # 1 Say Hello
        phrase = baskets_hello[phrase_n]
        os.system("espeak -ven+m1 -k5 -s150 '" + phrase + "'")
        # 2 Wait
        time.sleep(3)
        # 3 Say a Joke
        phrase = basket_a_speak[phrase_n]
        os.system("espeak -ven+m1 -k5 -s150 '" + phrase + "'")
        time.sleep(3)
     
    elif x == basket_b:

        # 1 Wait
        time.sleep(2)
        # 2 Say Hello Back
        phrase = baskets_hello[phrase_n]
        os.system("espeak -ven+f1 -k5 -s150 '" + phrase + "'")
        # 3 Wait
        time.sleep(7)
        # 4 Laugh at Joke
        phrase = 'Ha Ha Ha Ha Ha Ha Ha Ha Ha Ha Ha Ha'
        os.system("espeak -ven+f1 -k5 -s250 '" + phrase + "'")

    elif x == newspaper:
        print 'newspaper was detected'

    elif x == marshmallows:
        print 'marshmallows were detected'

    elif x == mint_tea:
        print 'mint tea was detected'

    elif x == rhubarb_and_custard:
        print 'rhubarb and custard was detected'

    elif x == energy_drink:
        print 'energy drink was detected'

    elif x == peroni:
        print 'peroni was detected'
