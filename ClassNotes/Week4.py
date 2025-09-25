# -*- coding: utf-8 -*-
"""
Created Thursday, Sept 25th, 2025


"""

# using ! to execute bash commands 

# this is a comment

myVar = 'hello world' # writing hello world to myVar

# Loops: an instruction that repeats until a speciified condition is met

# In python, there are 2 types of loops:
    # - A *for* loop is a loop that runs for a preset number of times
    # - A *while* loop is a loop that is repeated as long as an expression is true 
        # Like an if statement, don't know how many times the expression will be looped through
        
# For loop

# i is being assigned a value that goes from 1 to 5 

for i in range(1,5): # has to end in the colon
    print(i) # everything afterwards needs to be indented to belong to that code

# ranges are not inclusive (0 to 10 goes from 0 to 9), 1 to 5 goes from 1 to 4

for i in range(1,5): # has to end in the colon
    print("I am in the loop")
    print(i)
    
print("I am out of the loop")

# Here is a new loop

myList = ["apple", "banana", "cherry"] # x is going to take the value of each item in that list
for x in myList:
    print(x)

# While loop

i = 1 # started at 1
while i < 6: # as soon as it hits six, it stops loop
    print(i)
    i +=1 # take the current value of the variable and add to whatever is on the right (i = (i+1))

# WARNING! if your condition is never true, you will get stick in the dread infinite loop!

# Loops
    # the *break* command will exit out of the loop entirely. E.g., 
    # if i == 3
    #      break
    
    # the *continue* command will skip the remaining commands in the loop and move on to the next loop iteration:

i = 0
while i < 6: # is i less than 6
    i += 1 # add 1
    if i == 3: # but if it's 3, then skip the remaining commands and start over
        continue
    print(i)

# Scope

# Scope refers to the region of the code in which a variable or resource is visible and accessible

# If a variables are decleared with a while or for loop, their scope exists inside that loop and nothing "above it"

# In a global scope, all entities are visible throughout the entire program

# EXERCISE 1: create a loop that returns the value of a local variable, then try to return the same value in the global scope

for i in range(0,5): # create new variable
    x = i # declare new variable x
    print(x)

print(i)
print(x)

# Python libraries

# base Python has limited capabilities

# by adding libraries to your script/session, you can expand on it's capabilities

# many of the things that you will want to do will come in the form of packaged libraries 

# libraries need to be importaned and named

import numpy as np

x = np.sqrt(4) # float is a floating point integer, floating decimal point

print(x)

# can use from...import to load specific items from a library module

# can refer to them directly without a library name as a prefix

# Random library/method

# One of the most common libraries you will use is the random library (method)
    # - e.g., randomizing stimuli, conditions, time, created simulated data

# important to remember that random number generators (RNGs) are seeded (tied to some other value)
    # - in Matlab the RNG state is set to the same value every time it is opened

# can set your seed to a specific value, or get the state of the RNG at a particular point in time

# EXERCISE 2: Generate different kinds of random values multiple times using both seeds and states

import random

# Random numbers are set to a given state, that you can return to at a given point

# Always make sure you know what the seed is, important to set the seed for replication

random.randint(0,10)

# look up Python manual for random and functions within random

# we can also see what these options are by typing random. then seeing the listed options

# random.normalvariate is important for normal distribution

# may come up on our assignment this week!

# Functions:
    # functions are modulat bits of code that carry out a particular task or operation
    # can be called repeatedly throughout your code
    # functions can also take arguments (inputs) and can return values (outputs)
    
# Making our own function

def nameprintfunc(name): # define our function with def, name our function, and () denotes what arguments this function takes
    print('The name is ' + name) 
    return name

nameprintfunc('Hannah') 

myName = nameprintfunc('Hannah')

def adderFunc(val): # x is in a local scope within that function - value is unreadable outside that function
    x = val + val
    print(x)
    return x
    
x = adderFunc(2)

# You can have multiple arguments separated by a comma

# You can also make some arguments option but setting a default value

# You can also return multiple values from a function

def adderFunc(val = 4): # 4 is the default value
    x = val + val
    print(x)
    return x
    
adderFunc() # returns the default value

adderFunc(2) # overwrites the default value

def adderFunc(val1, val2 = 4): # setting the val2 as 4 by default, can overwrite it, but would need to specify val1
    x = val1 + val2
    print(x)
    return x

# Multiple values

def adderFunc(val1, val2 = 4): # setting the val2 as 4 by default, can overwrite it, but would need to specify val1
    x = val1 + val2 # function for x
    y = (val1 + val2) * 2 # function for y
    return x, y 

a, b = adderFunc(10, 5) 

c = adderFunc(10, 5) # tuple

# tubles are unchangable 
# lists are changable

# We can define our own functions like so:

def adderFunc(val1, val2 = 4): # setting the val2 as 4 by default, can overwrite it, but would need to specify val1
   """Adds two numbers together
   
   """

help(adderFunc)

# Classes

"""
- classes are a way for combining data and functionality together
- it's a way for you to build flexibility into code and re-use common procedures

How classes work

- create a class 
- class has
    - attributes (data)
    - methods (operations)

- can create multiple instances of the class

"""

# self refers to *this object*

class car: # definition of a class

    def __init__(self, color = 'white'): # initalizes attributes of every instance of the class
        self.speed = 0 # self allows you to access variable from anywhere else in class
        self.color = color # color is defined by (optional) input 
        
    def drive(self): # a method for the object (car)
        self.speed = self.speed +1 
        
    def breaking(self):
        self.speed = self.speed -1

vw = car() # create an instance of the class

vw.speed
vw.drive

toyota = car('green')

carList = [car() for x in range(0,5)] # create a list of objects

carList[2].color

# Classes can be stored in a separate file
# import using the:
    # from filename import class

#%% cell 2


