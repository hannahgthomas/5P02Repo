# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 13:34:43 2025

@author: thomh
"""

'''
Question 1:

(a) Generate 100 normally distributed values with a mean of 0.7 and a standard deviation of .2.

(b) Create a function that calculates the mean and standard deviation some list of values, and remove any values that exceed 2.5 SDs of the mean, recursively, 
until there are no outliers to remove. Note: The numbers to be trimmed should be an argument passed to the function.

(c) Apply the function created in (b) to the the list of 100 numbers you generated in (a). Produce the mean, SD, and number of outliers removed by the procedure.

'''
# %% Import Packages

import numpy as np

# %% Question 1: (a) Generate 100 normally distributed values with a mean of 0.7 and a standard deviation of .2.

# Here, I've set up mean and sd as global variables, but I could just explicitly list them in the rng.normal argument 

mean = 0.7

sd = 0.2

rng = np.random.default_rng() # random number generator

x = rng.normal(mean, sd, 100) 

y = rng.normal(0.7, 0.2, 100) 

'''
the rng.normal() function takes the following arguments:
    loc = mean
    scale = standard deviation
    size = # of observations / sample

https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html#numpy-random-generator-normal

'''

# %% Checking Values

np.mean(x) # the mean is not exactly 0.7, but it's close. That's because we are just pulling RANDOM numbers from a normal distribution with a mean of 0.7 and SD of 0.2
# so we can still expect some variability. 

# https://numpy.org/doc/stable/reference/generated/numpy.mean.html

# %% Question 1: (b) Create a function that calculates the mean and standard deviation some list of values, and remove any values that exceed 2.5 SDs of the mean, recursively, 
# until there are no outliers to remove. Note: The numbers to be trimmed should be an argument passed to the function.

def cleaningFunc(data, sd_cutoff = 2.5): # define my cleaning function - the arguments are data (array) and sd_cutoff can be modified but 2.5 is the default
    print('cleaningFunc output:')
    
    loop_num = 0 # Creating a counter variable
    
    while True: # Use while because we don't know how many times we want to run this code
        loop_num += 1 # each time the loop_num increases by 1
        print('loop #', loop_num) # This allows me to count the number of times the while loop goes through
        # Calculate mean
        mean = np.mean(data) 
        print('Original Mean:', mean) # Originally, I tried to do ('Original Mean:' + mean) but you cannot concatenate between a string and number(float)
        
        # Calculate standard deviation
        sd = np.std(data)
        print('Original SD:', sd)
        
        # Specify outlier cutoffs
        sd_cut_above = mean + sd_cutoff*sd # this will automatically change based on what sd_cutoff is
        print(sd_cutoff, 'cutoff ABOVE the mean:', sd_cut_above)
        
        sd_cut_below = mean - sd_cutoff*sd
        print(sd_cutoff, 'cutoff BELOW the mean', sd_cut_below)
        
        # Slice the data to include only values that are within our SD cut off ranges, store this cleaned data into a new array
        cleaned_data = data[(data < sd_cut_above) & (data > sd_cut_below)] # this is how I would do this in R
        
        #Calculate new mean from cleaned_data
        new_mean = np.mean(cleaned_data) # using cleaned_data we just created
        print('Cleaned Mean:', new_mean)
        
        # Calculate the new standard deviation
        new_sd = np.std(cleaned_data)
        print('Cleaned SD:', new_sd)
        
        #Compare the difference in length between our original data and cleaned data to see how many outliers were removed
        num_outliers = len(data) - len(cleaned_data)
        print('Number of Outliers Removed:', num_outliers)
        
        if len(cleaned_data) == len(data): # This is our break conditional, if the loop does not trim anymore outliers then break the loop. 
        
            break
        data = cleaned_data # this updates the data after each cleaning 
        
        
    
    return cleaned_data # returns the final cleaned dataset 

# %%

'''
Notes:
    I was comfortable defining this function since it's something I do regularly in R.  I had defined the function properly but it only ran once. 
    It took me quite a bit of time to figure out how to apply the function I created into the while loop. Then even more to figure out how to break the loop. But by counting
    the number of outliers after each loop (instead of after). By making the if len(cleaned_data) == len(data): the conditional argument to while True I was able to apply
    the function recursively. 
    
    I do think there has to be a more efficient way to set up the break in the loop using the while statement, I think by defining the cleaning function itself then
    placing it within the loop I might have some redudances such as printing the results from each loop. However, this made it easy to debug the code to ensure it 
    was still removing outliers and that the mean and sd were actually getting smaller with each loop through.
    
https://realpython.com/python-while-loop/    
https://pieriantraining.com/counting-in-a-python-loop-a-beginners-guide/
https://medium.com/analytics-vidhya/removing-outliers-understanding-how-and-what-behind-the-magic-18a78ab480ff

'''
# %%

# Demonstrating that the function works

cleaned_x = cleaningFunc(x, sd_cutoff = 2) # storing the cleaned data frame into an array

'''
I wasn't sure if the function was working recursively, so I lowered the sd cutoff which should remove outliers and it does just that
'''

# %% Question 1 (c)
# Applying the function to the random distributed list made in part (a) 

cleaned_y = cleaningFunc(y, sd_cutoff = 2.5)

# %%
# Summary of the overall changes made, compared the original y list to the cleaned y list

print("summary of cleaning process:")
print("original mean:", y.mean())
print("new mean:", cleaned_y.mean())
print("original sd:", y.std())
print("new sd:", cleaned_y.std())
print("total outliers removed:", len(y) - len(cleaned_y))


# %%

"""
Question 2:
    
(a) Create a list with 10 names of hypothetical students (use only lists for now). Create a second list of 10 theoretical grades between 76 and 100. 
Assume the order of the grades is the same order of the list of names.

(b) Write a script that loops through each of the students, and then return's their letter grade based on this convention:

A+: >=90
85 >= A <90
80 >= A- <85
76 >= B+ < 80
"""
# %% Question 2: (a) list of students and grades

students = ["ali", "beatriz", "charles", "diya", "eric", "seth", "gabriel", "anna", "ella", "rory"]

grades = np.random.randint(76, 100, 10) 

'''
Based on the previous question, I wondered if I could use a random generator to create random grade values within the range of 76 to 100.

I found this stackoverflow and applied it here. While this wasn't required I can imagine that using this function to simulate data might be helpful later on.

https://stackoverflow.com/questions/22842289/generate-n-unique-random-numbers-within-a-range

'''
# %% Question 2: (b) return letter grade 


# creating a for loop to return letter grade
for i in range(len(students)): # will go through each student in the list
    student = students[i] # i indexes the position
    grade = grades[i] # does the same thing here
    
    if grade >= 90:
        print(student, "=", "A+")
    elif 85 <= grade < 90:
        print(student, "=", "A")
    elif  80 <= grade < 85:
        print(student, "=", "A-")
    elif  76 <= grade < 80:
        print(student, "=", "B+")

'''
  This code only works if the position is the same, since I'm indexing based on position. 
  I'm sure if the data was organized in a data frame then this would be easier.
  I know personally that indexing by position is risky so I explored other methods below. 
        
https://www.geeksforgeeks.org/python/python-iterating-two-lists-at-once/
https://www.w3schools.com/python/python_lists_loop.asp

'''
# %%

# It does seem that zip() is a function that can combine two lists and iterate over them in parallel

for name, grade in zip(students, grades):
    
    if grade >= 90:
        print(name, "=", "A+")
    elif 85 <= grade < 90:
        print(name, "=", "A")
    elif  80 <= grade < 85:
        print(name, "=", "A-")
    elif  76 <= grade < 80:
        print(name, "=", "B+")

# %%

for name, grade in zip(students, grades): # by using zip() the lists are paired, if not they are matched by position
    print(name, grade)
    
# %%

print(students, grades) # prints the list to the console

# %%

print(students[2], grades[2]) # demonstrates how the lists are based on position

# %%
"""
Question 3: Write a function called ‘gradeLookup’ that takes, as an input from the user, a student’s name. Then look up the info based on Question 2, 
and write to the command window the student’s name, numerical grade, and letter grade.

Bonus: Can you figure out a way to ensure that the name entered is one that exists in the list??
"""

# %% Question 3:
    

# Defining gradeLookup function    
def gradeLookup(student_name): #I originally tried to put input here, but I don't think you can call a function within a function?
    for name, grade in zip(students, grades): # Using zip to pair up the students and grades lists
        if name == student_name: # the student_name argument has to match a name in the list 
            if grade >= 90:
                letter_grade = "A+"
            elif 85 <= grade < 90:
                letter_grade = "A"
            elif  80 <= grade < 85:
                letter_grade = "A-"
            elif  76 <= grade < 80:
                letter_grade = "B+"
            print("student name:", name)
            print("numeric grade:", grade)
            print("letter grade:", letter_grade)

            return 
    print("student not found") # runs through entire students list if no match then print message. needs to be OUTSIDE of the loop itself (made that mistake)

'''                      
Notes:

    In my previous code, I had the if statements evaluate the grade value, then print the letter grade. However, I returned to our in class exercises from week 3 and realized 
that I could create a new variable called letter_grade to store those values. I was trying to print the student name, numeric, and letter grades but could not get a clean output 
it printed the result like this:
    
 A+ 
 student name: 
 numeric grade:
     
So I changed it to create the variable letter_grade but kept my original method as well to show multiple approaches. 
'''
# %%
# Question 3: Look up function

gradeLookup(input("Enter student name: ")) # this input becomes the argument student_name in the gradeLookup function

# %% 

"""
Question 4: Write a Python class called PersonalityProfile that stores a participant’s scores on each of the Big Five traits (Openness, Conscientiousness, Agreeableness, Extraversion, Neuroticism) on a scale from 1–5.

Your class should include:

An __init__ method that initializes the five traits, as well as the participant number.

A method is_introvert() that returns True if the participant’s Extraversion score is less than 3, and False otherwise (feel free to make a similar method for all 5 traits).

Bonus: Create a method called summary() that returns a string describing the participant’s strongest trait (the one with the highest score).
"""
# %% Question 4:

# Defintion of class
class PersonalityProfile:
    # Initalize the attributes of the class
    def __init__(self, ID, Open, Cons, Agre, Extr, Neur): # I shortened these
        self.ID = ID
        self.Open = Open
        self.Cons = Cons
        self.Agre = Agre
        self.Extr = Extr
        self.Neur = Neur
    
    # Creating methods for scoring the traits
    def is_introvert(self):
        if self.Extr <= 3:
            return True
        else: 
            return False
    
    def is_open(self):
        if self.Open >= 3:
            return True
        else:
            return False
        
    def is_cons(self):
        if self.Cons >= 3:
            return True
        else:
            return False
    
    def is_agre(self):
        if self.Agre >= 3:
            return True
        else:
            return False
    def is_neur(self):
        if self.Neur >= 3:
            return True
        else:
            return False
        
    # Creating a summary to identify which score is the highest
    def summary(self):
        
        # Creating a list of the traits from the class attributes, skipping ID 
        scores = [self.Open, self.Cons, self.Agre, self.Extr, self.Neur] 
        
        # max identifies the highest numeric score in the scores list
        highest_score = max(scores)
        
        # evaluate if the highest score belongs to the score in that position
        if highest_score == self.Open:
            print("Strongest trait is Openness")
        elif highest_score == self.Cons:
            print("Strongest trait is Conscientiousness")
        elif highest_score == self.Agre:
            print("Strongest trait is Agreeableness")
        elif highest_score == self.Extr:
            print("Strongest trait is Extraversion")
        elif highest_score == self.Neur:
            print("Strongest trait is Neuroticism")
        
        
        return highest_score # I can't figure out how to have the return function not say "none" 
        
'''
I read through this documentation to get a better understanding of classes:
    
https://docs.python.org/3/tutorial/classes.html

I spent awhile on this summary portion. I'm sure there is way more efficient ways to do this, but I could think a way to identify
which score was the largest then using if statements to print which trait was the strongest.

https://www.w3schools.com/python/ref_func_max.asp

https://stackoverflow.com/questions/71753507/how-to-get-the-maximum-value-among-the-arguments-of-class-objects-in-python
'''
# %% Question 4: Creating some example data to show our class works

# the arguments we provide are assigned to the attributes we listed in the class

example1 = PersonalityProfile("99", 4, 3, 1, 5, 2)

# you can also directly specify the attribute and the value like this: 
example2 = PersonalityProfile(ID = "100", Open = 3, Cons = 4, Agre = 2, Extr = 1, Neur = 5)

# if we type
# PersonalityProfile(ID, Open, Cons, Agre, Extr, Neur) it shows the attributes within the class
    
# %% Question 4: Introversion method

print(example1.ID, "is an introvert:", example1.is_introvert())
print("extraversion score =", example1.Extr)

# %%
print(example2.ID, "is an introvert:", example2.is_introvert())
print("extraversion score =", example2.Extr)

# %% # Question 4: Summary Method

print("Participant:", example1.ID)
print("Highest Score =", example1.summary())

# %%
# another example that demonstrates that the summary works based on the position, now Neur is the strongest trait

print("Participant:", example2.ID)
print("Highest Score =", example2.summary())

# %%
'''
Overall Notes:
    I am still struggling with the indentation rules, as I'm used to R where I can use pipes like |> to specify the order of functions.
    I found myself placing some of my code outside of my loops. As I get more experience I'm sure I'll be able to debug my code faster.
    I'm not used to printing my result to the console, I usually store my results into tables so I spent a lot of time trying different methods. 
    
'''
