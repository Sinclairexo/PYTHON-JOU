# spam = 0
# if spam < 5:
#     print ("hello, world. ")
#     spam = spam + 1



# spam = 0
# while spam < 5:
#     print ("hello, world. ")
#     spam = spam + 1


# name = ''
# while name != "james":
#     print ("please type your name: ")
#     name = input ('>')
# print ("Thank you")


# while True:
#     print ("Please type in your name: ")
#     name = input ('<')
#     if name ==  "Enzo":
#         break
# print ("Thank you!!")


# while True:
#     print ("who are you? ")
#     name = input (">")
#     if name != 'james':
#         continue
#     print("Hello James, and what is the password: (hint: football)")
#     password = input(">")
#     if password == 'Chelsea':
#         break
#     print ("congrats, Access granted. ")


# name = ""
# while not name:
#     print ("Enter your name:")
#     name = input (">")
# print ("How many guest would you have: ")
# num_of_guests = int(input (">"))
# if num_of_guests:
#     print ("Be sure to have enough room for all of your guests.")
# print("Done")

# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")



# count = 0
# for number in range(1, 10):
#     if number % 2 == 0:
#         count += 1
#         print (number)
# print (f"we have {count} even numbers")

   
# successful = False
# for number in range (3):
#     print ("Attempt")
#     if successful:
#         print ("successful")
#         break 
# else:
#     print ("Not successful, try again")


# nested loops
# for x in range(6):
#     for y in range(4):
#         print (f"({x}, {y})")


# count = 0
# for number in range(1, 10):
#     if number % 2 == 0:
#         count += 1
#         print (number)
# print (f"we have {count} even numbers")


# prices = [10, 20, 30]


# total = 0
# for price in prices:
#     total += price
#     print (f"Total: {total}")

# GUESSING GAME USING WHILE LOOP
# secret_number = 9
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#     guess = int(input ("guess: "))
#     guess_count +=1 
#     if guess == secret_number:
#         print ("You Win!!")
#         break
# else:
#     print("You lose, Try again")

# CAR GAME
 
# command = ""
# started = False
# while True:
#     command = input ("> ").lower()
#     if command == "start":
#         if started:
#             print ("The car has already started")
#         else:
#             started = True
#             print ("Car started...")
#     elif command == "stop":
#         if not started:
#             print ("Car has already been stopped!!")
#         else:
#             started = False
#             print ("Car has stopped....")
#     elif command == "help":
#         print ("""
# start: To start the car
# stop:  To stop the car
# quit:  To end the operation
#         """)
#     elif command == "quit":
#         break
#     else:
#         print ("Apologies, I don't understand this command")


# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     output = ""
#     for count in range(x_count)
#     output += 'x'
#     print (output)

 
# numbers = [2, 4, 2, 6, 3, 9]
# largest = numbers[0]
# for number in numbers:
#     if number > largest:
#         largest = number
# print (largest)


# 2D LISTS

# matrix = [
#     [1, 2, 3],
#     [5, 6, 7],
#     [8, 9, 10]
# ]

# for row in matrix[0]:
#     for item in row:
#         print (item)

# LIST METHODS
# REMOVE DUPLICATES FROM A LIST

# numbers = [1, 3, 4, 4, 2, 6, 2]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)


# DICTIONARIES
# customer = {
#     "name" : "enzo",
#     "age" : 21,
#     "work" : "developer"
# }
# customer["name"] = "Jamie"  Changing the values of the dictionary
# print (customer.get("name"))


# phones = input ("phone: ")

# phones = {
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four"
# }

# output = ""
# for ch in phones:
#     output += phones.get(int(ch), "!") + " "
# print (output)


# students = {
#     "Enzo" : [85, 92, 78],
#     "Tunde" : [60, 55, 70],
#     "Amara" : [90, 88, 95],
#     "Chidi" : [40, 55, 45]
# }

# for names, scores in students.items():
#     total = 0
#     for score in scores:
#         total = total + score
#     average = total / len(scores)

#     print (f"{names} has an average score of {average}")


# EXERCISE ON DICTIONARIES AND LOOPS

# cart = {
#     "rice" : 1500,
#     "eggs" : 800,
#     "bread" : 600,
#     "milk" : 1200,
# }

# total = 0

# for item, price in cart.items():
  
#     total = total + price
#     print (f"{item}: {price}")

# print (f"Total: {total}")


# students = {
#     "John" : [85, 92, 78],
#     "Jane" : [90, 88, 95],
#     "Mike" : [60, 55, 70],
#     "Emily" : [40, 55, 45]
# }


# for name in students:
#     print (name)

#     total = 0


#     for score in students[name]:
#         total += score

#         print (score)

# print ("Total:", total)
# print ()


# products = {
#     "Laptop" : [1000, 1200, 1500],
#     "Phone" : [500, 600, 700],
#     "Tablet" : [300, 400, 500]
# }

# for product in products:
#     print (product)

#     total = 0

#     for price in products[product]:
#         print (price)
#         total += price


#     average = total / len(products[product])
#     print ("average price:", average)
#     print ()



# products = {
#      "Laptop" : [1200, 1500, 1800],
#      "Phone" : [500, 700, 900],
#      "Tablet" : [300, 450, 600]
#  }



# for product in products:
#     print (product)

#     total = 0

#     for price in products[product]:
#         total += price

#     print ("Total:", total)
#     print ("")

# # DICTIONARY EXERCISE
# students = {
#     "john" : "85",
#     "jane" : "90",
#     "mike" : "60",
#     "emily" : "40"
# }

# input_name = input ("Enter a student's name: ")

# while input_name not in students:
#     print ("student not found, please try again: ")
#     input_name = input ("Enter a student's name: ")
# print (students.get(input_name, "Student not found"))

