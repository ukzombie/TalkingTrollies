import os

basket_b = '0008342310' # Basket B - Non Sticker

basket_a = '0010580093' # Basket A - Sticker


#while True:

for x in range(0, 10):
    
    x = ''
    x = raw_input()

    if x == basket_a:
        print 'this is basket a'
        os.system("espeak 'basket a'")
    elif x == basket_b:
        print 'this is basket b'
        os.system("espeak 'basket b'")


    
