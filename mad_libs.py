print ("welcome to Mad libs!")
print ("I'll ask you for some words, then tell you a story. \n")

noun = input ("Give me a noun: ")
plural_noun = input ("Give me a plural noun: ")
verb = input ("Give me a verb: ")
Adjective = input ("Give me an adjective: ")
place = input ("Name me a place: ")
number = input ("Pick a number: ")

story = f"""
Once upon a time in {place}, there lived a {Adjective} {noun}. Every morning, it would {verb} exactly {number} times before breakfast. The other {plural_noun} in the village thought this was very strange, but the {noun} didn't care about it one bit
The end. 
"""

print (story)
