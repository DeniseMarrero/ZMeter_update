# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:03:30 2020

@author: Denise
"""

## geting input from a user / only strings
name = input("enter your name: ")
age = input("enter your age: ")
print("Hello " + name + "! You are " + age)

##Building a basic calculator
#python by defult when using input it assigns a string
num1 = float(input("enter a namber: "))
num2 = float(input("enter another namber: "))

result = num1 + num2
print("the result is: " + str(result))

##Mad Libs Game
color = input("Enter a color: ")
plural_noun = input("enter a plural name: ")
celebrity = input("enter a celebrity name: ")

print("roses are " + color)
print(plural_noun+" are blue")
print("I love " +celebrity)

##Lists are structures to store info
# creating a list
friends = ["Denise","Alba","Martin","Oscar","Toby"]
print(friends)
for i in friends:
    print(i)
print(friends[-1])
print(friends[1:])
print(friends[1:3])
friends[1] = "Mike"

## List functions
lucky_numbers = [4,8,15,16,23,42]
friends = ["Kevin","Karen","Jim","Oscar","Toby","Kevin"]
#to add two lists together
friends.extend(lucky_numbers)
#add individual items onto the end of the list
friends.append("Creed")
#add indiidual item in the middle of a list
friends.insert(1,"Kelly")
#remove indiidual item in the middle of a list
friends.remove("Jim")
#Empty list
friends.clear()
#pop an item off the list: removes the last element of a list
friends.pop()
#Check if a certain value is on the list, it returns the position
friends.index("Kevin")
#count how many elements there are on a list
friends.count("Kevin")
#sort the list in ascending order in alphabecit order
friends.sort()
#Reverse a list
friends.reverse()
#copying a list
friends2 = freinds.copy()
print(friends)

##Tuple: is a type of data structure. is a container where we can store different values. Similar as to a list. 
#Creating a tuple. A tuple is INMUTABLE
coordinates = (4,5)
#Creating a list of tuples
coordinates = [(4,5),(6,7)]
print(coordinates[0])

## Funtionons
def sayhello() :
    print("Hello user")
#Calling the function  
sayhello()
#working with parameters
def sayhi(name,age):
    print("Hello " + name + ", you are " + str(age))
    
sayhi("Mike",70)

#Return statment. getting info back from a function
def cube(num):
    return num*num*num

result = cube(4)
    
print(result)

## If statement
is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither male or tall")
        
if is_male and is_tall:
    print("You are a tall male")
else:
    print("You either not male or tall")
    
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and (is_tall):
    print("You are not a male but you are tall")
else:
    print("You are not male and not tall")

## If statement & comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

max_num(int(input("Enter a number: ")),40,75)

## Calculator
num1 = float(input("Enter 1st number: "))
op = input("Enter an operator: ")
num2 = float(input("Enter 2nd number: "))

if op == "+":
    print (num1 + num2)
elif op == "-":
    print (num1 - num2)
elif op == "/":
     print (num1 / num2)
elif op == "*":
     print (num1 * num2)
else: 
    print("Invalid op")

##Dictionaries allow us to store info in key value pairs
monthConversions = {
        "Jan": "January",
        "Feb" : "February",
        "Mar" : "March",
}

print(monthConversions["mar"])

monthConversions = {
        0: "January",
        1 : "February",
        2 : "March",
}

print(monthConversions[0])


##While loop
i = 1
while i <= 10:
    print(i)
    i += 1

print ("Done with loop")

## Guessing game
secret_word = 'giraffe'
guess = "" # Empty string
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
    

if out_of_guesses:
    print("Out of guesses, you lose!")
else:
    print("You win")

# For loop
for letter in "Giraffe Academy":
    print(letter)


friends = ["Kevin","Karen","Jim","Oscar","Toby","Kevin"]
for friend in friends:
    print(friend)

for index in range(3,10):
    print(index)

for index in range(len(friends)):
    print(friends[index])


for index in range(5):
    if index == 0:
        print("First iteration")
    else: 
        print("Not 1st")

##Exponent function.
print(2**3)

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result*base_num
    return result

print(raise_to_power(2,3))
    
#2D lists & nested loops    
number_grid = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [0]
]    
    
print(number_grid[2][1])    
    
for row in number_grid:
    for column in row:
        print(column)
    
## Basic translator
def translate(phrase):
    translation = "" # empty string
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else: 
            translation = translation + letter
    return translation


print(translate(input("enter a prhase: ")))


## Try and except


try:  
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err: 
    print(err)
except ValueError:
    print("Invalid input")


# reading from external files
employee_file = open("employees.txt", "r")

print(employee_file.read())

employee_file.close()

#Writing and appending files
employee_file = open("employees.txt", "a") #adding text at the end
employee_file.write("\nKelly - Customer Servise")

employee_file = open("employees.txt", "w") #overwrite the entire file
employee_file.write("\nKelly - Customer Servise")

employee_file = open("employees1.txt", "w") #creating a new file
employee_file.write("\nKelly - Customer Servise")

#Modules and pip
#modules is a python file that we can import into our current python file
import useful_tools

print(useful_tools.roll_dice(10))

import docx
docx.

##Classes and objects. With classes we can define our own data type
from student import student

student1 = student("Jim","Accountat",3.1,False)
student2 = student("Phyllis","Busiess",3.8,False)
print(student1.name)
print(student2.gpa)

print(student1.on_honor_roll())

#Building a multiple choise quiz
from Question import Question
question_prompts = [
        "What color are apples? \n (a) Red/Green \n (b) Purple \n (c) Orange \n\n",
        "What color are bananas?\n(a )Teal\n(b) Magenta\(c) Yellow\n\n",
        "What color are strawberris?\n(a) Yellow\n(b) Red\(c) Blue\n\n",
]


questions = [
        Question(question_prompts[0], "a"),
        Question(question_prompts[1], "c"),
        Question(question_prompts[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct")
    
run_test(questions)

#from ASCII values to characters
data =[1, 32, 55, 2, 87, 69, 76, 67, 79, 77, 69, 3, 53, 65, 4, 1, 49, 52, 2, 90, 77, 101, 116, 101, 114, 52, 119, 32, 118, 32, 52, 46,
 50, 32, 67, 79, 82, 66, 73, 3, 55, 57, 4]
characters = [chr(ascii) for ascii in data]
''.join(characters)

#from characters to ASCII values
s.decode = "b'\x01 7\x02WELCOME\x035A\x04\x0114\x02ZMeter4w v 4.2 CORBI\x0379\x04'
ASCII = [ord(c) for c in s]

            
   

# to get how many 4 there are in data string / generator expression
data_pos = [i for i, n in enumerate(data) if n ==32]
data_num = len([i for i, n in enumerate(data) if n ==32])

### GUI

import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
        
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executable","*.exe"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text = app, bg="gray")
        label.pack()
        
def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root,bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely =0.1)

openFile = tk.Button(root, text="Open file", padx=10, 
                     pady=5, fg ="white",bg="#263D42", command = addApp )
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, 
                     pady=5, fg ="white",bg="#263D42", command=runApps )
runApps.pack()

root.mainloop()

with open ("save.txt", "w") as f:
    for app in apps:
        f.write(app + ",")



































































































    























