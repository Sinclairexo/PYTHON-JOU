# a = 23
# b = 144

# if a < b:
#     print ("a is less than b")


# number = 20
# if number > 0:
#     print ("the number is negative") 

# age = 20
# if number >= 20:
#     print ("You are the same age as an adult")
#     print ("You can drink now")
#     print ("This is my real age")


# a = input ("What is the first number: ")
# b = input ("What is the second number: ")

# if a > b:
#     print ("A is better")
# elif a < b:
#     print ("B is the greater number")


# a = 23
# b = 13

# if a > b:
#     print ("A is better")
# elif a < b:
#     print ("B is the greater number")

# age =20
# if age < 12:
#     print ("You are younger than me")
# # elif age > 20:
# #     print ("You are an old man")
# elif age < 18:
#     print("You are a child")
# elif age < 20:
#     print ("You are not young")
# elif age >= 20:
#     print("You are the normal age")

# day = 3
# if day == 1:
#     print ("Monday")
# elif day == 2:
#     print ("Tuesday")
# elif day == 3:
#     print ("wednesday")
# elif day == 4:
#     print ("Thursday")


# ELSE STATEMENT
# a = 5
# b = 8
# if a > b:
#     print ("This statement is not true")
# else:
#     print ("b is greater than a")


# NUMBER GUESSSING HELPER PROJECT
# secret_number = 7
# guess = int(input("Guess the number (1-10): "))

# if guess == secret_number:
#     print ("The Number you guessed is correct:) ")
# elif guess > secret_number:
#     print ("Apologies, The number you guessed is too high ")
# else:
#     print ("You guessed it wrong, it is too low ")


# a = 25
# b = 13

# if a > b:
#     print ("25 is greater than 13")
# else:
#     print ("It is not greater")


# # number = int(input ("Enter a number: "))

# # if number > 0:
# #     print ("The number is positive")
# # elif number < 0:
# #     print ("The number is negative")
# # else:
# #     print ("zero")



# # Grade Calculator
# while True:
#     entry = input ("Enter a score between 0 and 100 or q to quit: ")
#     if entry == 'q':
#         break
#     try:
#         entry = int(entry)
#     except ValueError:
#         print ("Please enter a valid number or 'q' to quit.")
#         continue

#     if entry > 100 or entry < 0:
#         print ("invalid score")
#     elif entry >= 70:
#         print ("A")
#     elif entry >= 60:
#         print ("B")
#     elif entry >= 50:
#         print ("C")
#     elif entry >= 44:
#         print ("D")
#     else:
#         print ("F")

username = "admin"
password = "admin123"
while True:
    username_input = input ("Enter your username: ")
    password_input = input ("Enter your password: ")

    if username_input == username and password_input == password:
        print ("Login successful")
        break
    else:
        print ("Invalid username or password. Please try again.")
username = input ("Enter your username: ")
password = input ("Enter your password: ")

if username == "admin" and password == "admin123":
    print ("Login successful")
elif username != "admin" and password == "admin123":
    print ("user not found!!!!")
elif username =='admin' and password != "admin123":
    print ("Invalid password")  
else:
    print ("Invalid username and password")