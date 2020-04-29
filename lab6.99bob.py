"""
%d is placeholder
"""

REFRAIN = '''
%d bottles of beer on the wall,
%d bottles of beer,
take one down, pass it around,
%d bottles of beer on the wall!
'''

bottles_of_beer = 100
while bottles_of_beer > 1:
    print (REFRAIN % (bottles_of_beer, bottles_of_beer,
        bottles_of_beer - 1))
    bottles_of_beer -= 1


#or

bottles_of_beer = 100
print ("There were 99 bottles of beer on the wall")
while bottles_of_beer > 1:
        print (bottles_of_beer, "bottles of beer on the wall,")
        print (bottles_of_beer, "bottles of beer,")
        print ("take one down, pass it around,")
        print (bottles_of_beer - 1, "bottles of beer on the wall!\n")
        bottles_of_beer -= 1