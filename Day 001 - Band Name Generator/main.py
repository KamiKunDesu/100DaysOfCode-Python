'''
Day one of the 100 days of code python challenge - The objective of this project is to make a program
which takes the name of the City you grew up in, as well as the name of your pet, and uses it to make
a band name
'''

#Greeting
print('Welcome to the Band Name generator.')
print('Hopefully you can use this to come up with a band name - first, let\'s just get some info.')

#takes the name of the city you grew up in and stores it in a variable city_name
city_name = input("What is the name of the city which you grew up in? ")
print('')

#takes the name of your pet growing up and stores it in a variable pet_name
pet_name = input("What is the name of your pet? Or what was the name of your pet growing up? ")
print(f"\nA good name for your band might be: {city_name} {pet_name}")