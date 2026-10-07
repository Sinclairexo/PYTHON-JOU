# def greet_user():
#     print ("Hello! Welcome to the program.")
#     print ("This is me starting Functions.")


# print ("Start")
# greet_user()
# print ("Finish")

# PARAMETERS
# def greet_user(first_name, last_name):
#     print (f"hello {first_name} {last_name}!")
#     print ("Welcome to the program.")


# print ("Start")
# greet_user("Enzo", "Mendez")
# print ("End")

# KEYWORD ARGUEMENTS

# def greet_user(first_name, last_name):
#     print (f"hello {first_name} {last_name}!")
#     print ("Welcome to the program.")


# print ("Start")
# greet_user(last_name="Enzo", first_name = "Mendez")
# # USE THE KEYWORD ARGUEMENT BEFORE THE POSTIONAL ARGUEMENT
# print ("Finish")  

# RETURN STATEMENT

# def square(number):
#     return number * number

# print (square(3))

# EXERCISE ON FUNCTIONS

# def multiply(a, b):
#     return a * b

# print (multiply(4, 5))

# def check_age (age):
#     if age >= 18:
#         return "adult"
#     elif age >= 13:
#         return "teenager"
#     else:
#         return "child"


# print (check_age(14))


# EXCEPTION HANDLING
# HOW TO HANDLE ERRORS IN PYTHON

# try:
#     age = int(input('Enter your age: '))
#     print (age)
# except ValueError:
#     print("Please enter a valid number.")

# DATA CLASSES (POINT)

# class Point: 
#     def move(self):
#         print("move")

#     def draw(self):
#         print("draw")


# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()


# point2 = Point()
# point2.x = 1
# print (point2.x)

# CREATING AN POINT BJECT X OR Y COORDINATE

# from unicodedata import name


# class Point: 
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y



#     def move(self):
#         print("move")

#     def draw(self):
#         print("draw")


# point = Point(10, 20)
# print (point.x)


# EXERCISE

# class Person:
#     def __init__(self, name):
#         self.name = name



#     def talk(self):
#         print(f"Hi, my name is {self.name}")


# john  = Person("John Smith")
# print (john.name)
# john.talk()



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# person1 = Person("John", 30)
# print (person1.name)
# print (person1.age)    


# INHERITANCE

# class Mammal:
#     def walk(self):
#         print ("walk")


# class Dog(Mammal):
#     def bark(self):
#         print ("bark")


# class Cat(Mammal):
#     def meow(self):
#         print ("meow")


# dog1 = Dog() 
# dog1.walk()

# MODULES IN PYTHON 

# import converter

# print(converter.kg_to_lbs(20))

# EXERCISE








