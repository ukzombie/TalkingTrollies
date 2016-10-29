import os
from array import *

basket_a_speak = ['Chocolate comes from cocoa, which is a tree. That makes it a plant. Therefore, chocolate is salad.','Damn, I forgot to go to the gym today. Thats 10 years in a row now...']

basket_b_speak = ['Im learning the hokey cokey. Not all of it. But  Ive got the ins and outs.','Ive got very sensitive teeth. Theyll probably be upset Ive told you.']

#os.system("espeak 'Hello'")
#Woman voice
os.system("espeak -ven+f1 -k5 -s150 'Hello'")
os.system("espeak -ven+f2 -k5 -s150 'Hello'")
os.system("espeak -ven+f3 -k5 -s150 'Hello'")
os.system("espeak -ven+f4 -k5 -s150 'Hello'")

#Mens Voice
os.system("espeak -ven+m1 -k5 -s150 'Hello'")
os.system("espeak -ven+m2 -k5 -s150 'Hello'")
os.system("espeak -ven+m3 -k5 -s150 'Hello'")
os.system("espeak -ven+m4 -k5 -s150 'Hello'")
os.system("espeak -ven+m5 -k5 -s150 'Hello'")
os.system("espeak -ven+m6 -k5 -s150 'Hello'")
os.system("espeak -ven+m7 -k5 -s150 'Hello'")

