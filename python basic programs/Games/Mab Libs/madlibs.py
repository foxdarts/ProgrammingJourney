# #string concatenation(putting strings together)


# vtuber = "foxdarts" #creates a variable for vtuber. yes this is a youtube chanel run by me as well.. gaming stuff is fun lol


# print("subscribe to " + vtuber) #basic and just prints

# print("subscribe to {}".format(vtuber)) #another great way to print the same information with a little more context puts vtuber info into the curly braces

# print(f"subscribe to {vtuber}") #and you guessed it. another way to print the same info. adds format before and places variable into curly braces.

#mablib starts here.  before pieces are to explain and provide insight


adjective = input("please provide a Adjective: ") #asks the user to provide a adjective for the mablib!
verb1 = input("Please provide a verb: ") #asks the user to provide a verb for their mablib
verb2 = input("Please provide a second verb: ") #asks the user to supply another verb for their madlib!
fperson = input("Please provide the name of someone famous: ") #asks the user for the name of a famous person as the actor within thier madlib!


madlib = f"computer programming is so {adjective}! it is very fun and makes me excited.  i love to {verb1}! please stay hydrated and {verb2} just like {fperson} loves to do!" #this is the code for the madlib that takes user input and has them create a story!

print(madlib) #prints the mablib
