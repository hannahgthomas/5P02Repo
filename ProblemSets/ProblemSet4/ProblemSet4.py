# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 09:01:52 2025

@author: thomh
"""
# %% Load Packages

import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

# I might need to add other packages for question 6

# %% 
"""
Question 1 - Creating and Exploring Data with NumPy

"""

# %% Participant IDs

subID = np.arange(start=1, stop=41, step=1)

# https://numpy.org/devdocs/reference/generated/numpy.arange.html

# %% Two Conditions: "congruent" and "incongruent"

conditions = np.array(['congruent', 'incongruent'])

# https://numpy.org/doc/stable/reference/generated/numpy.array.html

# %% Reaction Times:

rtCon = np.random.normal(loc=520, scale=70, size = 2000)

rtIncon = np.random.normal(loc=610, scale=70, size = 40*50)

# https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html

# %% Adding Noise to RTs

noiseCon = np.random.uniform(low=-20, high = 20, size=2000)

noiseIncon = np.random.uniform(low=-20, high = 20, size=2000)

# https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html

rtConNoise = (rtCon + noiseCon)

rtInconNoise = (rtIncon + noiseIncon)

'''
NOTE: I've included how I completed each piece outside of the function b/c that's how I did it originally
Then I kept it b/c I documented it nicely :P
'''

# %%

def trialDataRandomization(subID):
    data = [] # placeholder
    for subject in subID: # loops through each participant from the sudID list

        # RT data
        rtCon = np.random.normal(loc=520, scale=70, size=50) # Generates 50 congruent RTs
        rtIncon = np.random.normal(loc=610, scale=70, size=50) # Generates 50 incongruent RTs

        # Noise data
        noiseCon = np.random.uniform(low=-20, high=20, size=50) # Creates a uniform distributed noise for 50 trials
        noiseIncon = np.random.uniform(low=-20, high=20, size=50)
        
        # Adds the noise to the RT data, creating a new list to store them

        rtConNoise = rtCon + noiseCon
        rtInconNoise = rtIncon + noiseIncon
        
        # Loops through each RT and creates a row for each trial (basically a list of trial data)
        for rt in rtConNoise:
            data.append([subject, "congruent", rt])


        for rt in rtInconNoise:
            data.append([subject, "incongruent", rt])
            
    return pd.DataFrame(data, columns=["participant", "condition", "rt"]) # Returns a pandas data frame assigning labels to the lists

df = trialDataRandomization(subID)

'''
https://www.datacamp.com/tutorial/synthetic-data-generation

This example showed me how I wanted my data to be structured, I followed the Techniques for Synthetic Data Generation, particularly
2. Rule-based generation as it created a function.

https://www.geeksforgeeks.org/python/create-a-dataframe-from-a-numpy-array-and-specify-the-index-column-and-column-headers/

This helped me realize that I needed to create lists for the trial data, as every example had data within lists. 
'''
# %%

# By placing this within a function, I could test it out for one participant at time.

df1 = trialDataRandomization('1')

# %% df.head()

df.head(10) # prints the first 10 rows

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html

df.describe()

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html

# %%
"""
Question 2 - Loading and Cleaning Data with Pandas

"""
# %% Remove trials using indexing

cleanDF = df.mask((df["rt"] > 800) | (df["rt"] < 300)) # Boolean indexing, evalutes true or false

# https://www.w3schools.com/python/pandas/ref_df_mask.asp

"""
This a bit different then how I indexed and removed RTs during Problem Set 2, I filtered through them instead which does not create NaN values

"""

# %% Print the number of trials removed

print("Number of Trials removed =", cleanDF["rt"].isnull().sum()) # counts the number of Na values

# https://www.geeksforgeeks.org/python/count-nan-or-missing-values-in-pandas-dataframe/ 

# %% Create a cleaned DataFrame

by_participant = cleanDF.groupby(["participant", "condition"])["rt"].mean().reset_index()

'''
EXPLAINATION OF FUNCTION: 
    
cleanDF.groupby will group the data by participant number and condition, since there is two conditions it will automatically create both

the participant argument allows for group by to grab participant number

["rt"].mean().reset_index() computes the mean RT for each participant, seperately by condition it is the aggregation operation, applying mean function

reset_index) rests the index of the data frame, which used to be 4000

I'm familar with this as the function group_by() in R I utilize a lot. Especially when data is organized in long format like this. 

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html
# https://www.geeksforgeeks.org/pandas/python-pandas-dataframe-groupby/
'''
# %% 
"""
Question 3 - Merging DataFrames

"""
# %% Compute the mean RT for each condition without groupby

# Congruent 

congruentDF = by_participant.mask(by_participant["condition"] == "incongruent")

meanCon = (congruentDF["rt"].mean())

print("Mean for the Congruent Condition =",round(meanCon, 2))

# Incongruent

IncongruentDF = by_participant.mask(by_participant["condition"] == "congruent")

meanIncon = (IncongruentDF["rt"].mean())

print("Mean for the Incongruent Condition =",round(meanIncon, 2))


# %% Add accuracy column

# The method used to calculate cleaned data grouped it to a df of 80 rows, I would need to use the cleanDF that I made earlier but drop the unused columns

# B/c I'm adding back trial data

cleanDF = cleanDF.dropna() 

len(cleanDF)

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html

accuracy = [0, 1]

random.choices(accuracy, weights=(0.2, 0.8))

accList = random.choices(accuracy, weights=(0.2, 0.8), k = len(cleanDF))

cleanDF.insert(3, "accuracy", accList)

# https://www.geeksforgeeks.org/python/choose-elements-from-list-with-different-probability-in-python/
# https://www.w3schools.com/python/ref_random_choices.asp

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html - inserting columns

# %% mean RT accurate conditions

# Creating a new df with only accurate trials

accDF = cleanDF.mask(cleanDF["accuracy"] == 0) 

accDF = accDF.dropna()

accDF.groupby(["condition"])["rt"].mean().reset_index() 

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html

# in R, I would not have created a new data frame. First, I'd filter it to accuracy = 1, then run my groupby function. Handy for instances where you only want accurate trials.

# Below, I do filter through the data, but I couldn't figure out how to combine filter and group by 

# %%
"""
Question 4 - Plotting with Matplotlib

"""
# %% Histogram 

fig = plt.figure(figsize=(10, 5))

axes1 = fig.add_subplot(1, 2, 1)
axes2 = fig.add_subplot(1, 2, 2)


axes1.hist(cleanDF[cleanDF["condition"] == "congruent"]["rt"], bins=8, color ='lightcoral', edgecolor = 'black')
axes1.set_title("congruent")
axes1.set_ylabel("count")
axes1.set_xlabel("rt (ms)")



axes2.hist(cleanDF[cleanDF["condition"] == "incongruent"]["rt"], bins = 8, color = 'skyblue', edgecolor = 'black')
axes2.set_title("incongruent")
axes2.set_ylabel("count")
axes2.set_xlabel("rt (ms)")

plt.show()

# My understanding is that a histogram is for distribution of trial data, all observations. But maybe
# you meant to use the by_participant?

# https://www.geeksforgeeks.org/python/how-to-plot-a-pandas-dataframe-with-matplotlib/

# For specifically matplot and pandas df

# https://www.geeksforgeeks.org/pandas/ways-to-filter-pandas-dataframe-by-column-values/

# filtering the data frame to only certain conditions is really helpful! I couldn't figure out how to use it for group.by above 

# %% Bar Graph

n =  40

# Compute sd for each condition

sdCon = (by_participant[by_participant["condition"] == "congruent"]["rt"].std())

sdIncon = (by_participant[by_participant["condition"] == "incongruent"]["rt"].std())

# Compute SE for each condition

seCon = sdCon / np.sqrt(n)

seIncon = sdIncon / np.sqrt(n)

# Create a data frame with means per condition for plotting

data = {'condition': ['congruent', 'incongruent'], 'mean': [meanCon, meanIncon]}
barDF = pd.DataFrame(data) # Convert into a pd df

# Plotting data

plt.bar(barDF['condition'], barDF['mean'], yerr = [seCon, seIncon], color = ["lightcoral", "skyblue"]) 
plt.title("Mean RT by Condition")
plt.xlabel("condition")
plt.ylabel("RT (ms)")

plt.show()

# https://www.geeksforgeeks.org/python/how-to-plot-a-pandas-dataframe-with-matplotlib/ - plotting with a pd data frame

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html

# https://numpy.org/doc/stable/reference/generated/numpy.std.html - standard deviation

# https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt - square root

# %%
# Example using the sd, to demonstrate what the error bars should look like
plt.bar(barDF['condition'], barDF['mean'], yerr = [sdCon, sdIncon], color = ["lightcoral", "skyblue"], capsize = 5)
plt.title("Mean RT by Condition")
plt.xlabel("condition")
plt.ylabel("RT (ms)")

plt.show() 

# %%
"""
B/c of how I generated my reaction time data, per participant with a mean of 520 and sd of 70, the sample sd it relatively small (~8ms).

This makes the error bars basically non-existent. 

If I had drawn a sample of RT's across all trials with that specification, I would end up with something more like what I presented above.

However, I think it was difficult to differentiate between whether those parameters were for each participant, or the entire sample (results for this question vary a lot)

Since if you do it per participant, like I did, you lose variability within the sample. 

A potential solution I thought of, was to first generate a mean and SD for each participant within the parameters, then 
generate their trial data from that.
"""

# %%
"""
Question 5 - Plotting with Seaborn

"""

# %% Violin Plot

violin = sns.violinplot(data=by_participant, x="condition", y="rt", hue = "condition")

violin.set_title('Violin Plot of mean RT by condition')

# https://seaborn.pydata.org/generated/seaborn.violinplot.html
# %% Line Plot

line = sns.lineplot(data=by_participant, x="condition", y="rt", hue="participant", legend = "auto")

line.set_title('Line Plot of mean RT by condition')

# I did request legend as "full" it was huge, so I opted to include the auto legend. 

# https://seaborn.pydata.org/generated/seaborn.lineplot.html
# %%
"""
Question 6 - Curve Fitting: Visual Working Memory Capacity

"""
# %%

from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

load = np.array([1, 2, 3, 4, 5, 6]) 
k = np.array([0.9000, 1.8000, 2.7000, 3.5000, 3.1966, 3.7939])

# Defining two-stage model

def twoStageModel(x, a, b, k_break): 
    y_vals = [] # list of y values 
    for load in x: # loops through each memory load value, determines if capacity limit is reached
        if load <= k_break:
            y = a * load + b    # K is increasing with load
        else:
            y = a * k_break + b   # K stays constant)
        y_vals.append(y)
    return np.array(y_vals)

# Fitting the two-stage model using curve_fit  
twoParam, twoCovar = curve_fit(twoStageModel, load, k)

# Predicted y values for each capacity limit (x) - plotting
fit_twoStage = twoStageModel(load, twoParam[0], twoParam[1], twoParam[2])

# Plotting the two-stage model
plt.plot(load, k, 'o', label='data')
plt.plot(load, fit_twoStage, '-', label='two stage model')


# Defining exponetial model
def expModel(x, A, B, C):
    return A * (1 - np.exp(-B * x)) + C

# Fitting the exponetial model using curve_fot
expParam, expCovar = curve_fit(expModel, load, k)

# Predicted y values for each capacity limit (x) - plotting
fit_exp = expModel(load, expParam[0], expParam[1], expParam[2])

# Plotting the exponetial model

plt.plot(load, fit_exp, '-', label='exp model')

# Labelling plot
plt.legend()
plt.xlabel('working memory load')
plt.ylabel('working memory capacity (k)')
plt.title('Curve Fitting: Working Memory Capacity')

# Printing relevant model parameters

print('Two Stage Model Parameters:', 'A =', round(twoParam[0], 2), 'B =', round(twoParam[1], 2), 'k break =', round(twoParam[2], 2)) 

print('Exponential Model Parameters:', 'A =', round(expParam[0], 2), 'B =', round(expParam[1], 2), 'C =', round(expParam[2], 2)) 


# https://www.geeksforgeeks.org/machine-learning/scipy-curve-fitting/#google_vignette

# for this question, I also followed the Gaussan example from lecture. 
