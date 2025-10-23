# Import Packages

from psychopy import visual, core, event, data, gui

import numpy as np

# Create a Window

win = visual.Window([1920, 1080], fullscr = True, monitor = "legionMonitor", screen = 1, color = [1, 1, 1], units = "norm")

# This needs to be specified to the monitor you are using, I'm sure there is a more universal way but I could only figure out how to do this manually. 
mon_wid = 1920 # width of current monitor
mon_hei = 1080 # height of current monitor

# Calculate size of stimuli based on monitor size
height = 0.1 # can be smaller or larger
width = height * (mon_hei / mon_wid) 

# NOTE: Originally I was just specifying size as (0.1, 0.1) which matched the dimensions of the images. 
# Then I realized that by using norm units, a square needed to be set to the ratio of the monitor dimensions.
# https://www.psychopy.org/general/units.html


# --- General Experiment Directory and GUI --- #

info = {} # empty directory

info['participant'] = '' # blank key
info['n of trials per condition'] = '' # blank key
dlg = gui.DlgFromDict(info) # take input for the keys in the dictionary
if not dlg.OK:
    core.quit()
    
# Setting up file name used in Experiment Handler
    
filename = f"VisualSearch_{info['participant']}" # now, the file will save with the participant ID that was entered

# Saving the values from the info dictionary to variables

participant_id = info['participant']
n_trials = info['n of trials per condition'] # This is entered into the trial loop in place of nReps

# --- Instructions Screen --- #

instr_txt = ("You will be presented with an array of letter Ls, on some trials a letter T will present. \n On trials where the T is present, press 't' on your keyboard to respond")
instr = visual.TextStim(win, text=instr_txt, pos=(0, 0.2), color = 'black') # Assigns instructions to a text stimuli

# Empty msg stimuli which is used for instructions and feedback
msg = visual.TextStim(win, text=' ', pos=(0, -.4), color = 'red')

# Presenting Instructions Screen 
instr.draw()
msg.text = "press the space bar to start the practice trials" # 
msg.draw()
win.flip()
event.waitKeys(keyList=['space']) # Wait until space bar is pressed


# --- Experiment Handler --- #

# Experiment Handler allows for multiple loops and handlers. 

# https://www.psychopy.org/api/data.html

# I got this from the Demos > experiment control > experimentHandler.py

thisExp = data.ExperimentHandler(name='VisualSearch',
                version='0.1',
                runtimeInfo=None,
                originPath=None,
                saveWideText=True, # saves the csv file
                dataFileName=filename) # specified above
                

# --- Condition Dictionary --- #

# From Trial Handler, you can either upload a csv file which is used as a dictionary, instead I just made a dictionary here.

conditionList = [
    {"n_dist": 8, "n_target": 0, "set_size": 8},
    {"n_dist": 7, "n_target": 1, "set_size": 8},
    {"n_dist": 12, "n_target": 0, "set_size": 12},
    {"n_dist": 11, "n_target": 1, "set_size": 12},
    {"n_dist": 14, "n_target": 0, "set_size": 14},
    {"n_dist": 13, "n_target": 1, "set_size": 14} 
    ]
    
# NOTE: I have set this up so that there are 3 set sizes, but actually two versions of each condition (1 target absent + 1 target absent).
# This ensures that the distractors appear 50% of the time, but I'm sure there is a better way to design this. 
    
# Define Orientation and Collect Responses

ori_rand = [0, 90, 180, 270] # randomizes the orientation

respClock = core.Clock() # creates the response clock

# --- Practice Trials --- #

# I made a seperate trial handler for the practice trials, since I did not want to save these trials.

# NOTE: Since I just copied an earlier version of my experimental trial handler, I commented the experimental trials more in depth. 

practice = data.TrialHandler(trialList = conditionList, # trialList a list of dictionaries specifying conditions 
                            method = 'random', # Random shuffle on each repeat
                            nReps = 2) # Specify that there will be 2 * 6 = 12 practice trials
                            

for thisTrial in practice: 
    n_dist = thisTrial['n_dist']
    n_target = thisTrial['n_target']
    
    # Create trial stimuli
    dist_list = []
    target_list = []
    
    for i in range(n_dist):
        dist = visual.ImageStim(win, image = 'stimuli/L.png', pos = (np.random.uniform(-0.8, +0.8), np.random.uniform(-0.8, +0.8)), size = (width, height), ori = np.random.choice(ori_rand))
    
        while any(dist.overlaps(placed) for placed in dist_list): # placed = dist already within the list 
            dist.pos = (np.random.uniform(-0.8, +0.8), np.random.uniform(-0.8, +0.8)) # I think this will ensure the stimulus does not overlap, if dist overlaps placed, then reposition dist. 
        dist_list.append(dist)
        
    
    for i in range(n_target):
        target = visual.ImageStim(win, image = 'stimuli/T.png',pos = (np.random.uniform(-0.8, +0.8), np.random.uniform(-0.8, +0.8)), size = (width, height))
        target_list.append(target)
        
    # Draw stimuli
    
    for dist in dist_list:
        dist.draw()
    
    for target in target_list:
        target.draw()
    
    win.flip()
    
    # Collect Responses
    
    respClock.reset()
    keys = event.waitKeys(maxWait = 2.0, keyList=['t', 'escape'],
    timeStamped = respClock)
    
    if keys is None:
        key, rt = None, np.nan
    else:
        key, rt = keys[0] # time stamps key press for reaction time
    
    if key == 'escape': # exits the experiment 
        win.close()
        core.quit()
    
    # Scoring
    if  n_target == 1 and key == 't':
        corr = 1
        feedback = "correct!"
    elif n_target == 0 and key == 't':
        corr = 0
        feedback = "incorrect!"
    elif n_target == 1 and key != 't':
        corr = 0
        feedback = "incorrect!"
    elif n_target == 0 and key != 't':
        corr = 1
        feedback = "correct!"
    else:
        corr = np.nan
        
    msg.text = feedback
    msg.draw()
    win.flip()
    core.wait(0.7)

# --- End of Practice Screen --- #
instr.text = "You have completed the practice trials"
msg.text = "Press 'space' to begin the experimental trials"
instr.draw()
msg.draw()
win.flip()
event.waitKeys(keyList=['space'])
    
# --- TrialHandler - Experimental --- #

# https://www.psychopy.org/api/data.html

# For reference, I used the Demos > experiment control > TrialHandler.py

trials = data.TrialHandler(trialList = conditionList, # trialList a list of dictionaries specifying conditions 
                            method = 'random', # Random shuffle on each repeat
                            nReps = n_trials) # Taken as input from the GUI dialogue, if input is 2 then there will actually be 12 trials (since conditions = 6) 

thisExp.addLoop(trials) # without this, it does not save the data from the trial loops

# --- Trial Loop --- #
for thisTrial in trials:
    # Empty list for number of distractors and targets
    n_dist = thisTrial['n_dist']
    n_target = thisTrial['n_target']
    
    # Empty list to place stimuli 
    dist_list = []
    target_list = []
    
    for i in range(n_dist): # for the number of distractors specified (if n_dist = 8, then 8 stimuli are created)
        dist = visual.ImageStim(win, image = 'stimuli/L.png', 
        pos = (np.random.uniform(-0.8, +0.8), np.random.uniform(-0.8, +0.8)), # I was having a difficult time with the stimuli being off screen, so I randomized it to a smaller range than 1.0, 1.0
        size = (width, height), # Makes this specific to monitor size specified manually earlier 
        ori = np.random.choice(ori_rand)) # Randomly selects 
    
        while any(dist.overlaps(placed) for placed in dist_list): # placed = dist already within the list 
            dist.pos = (np.random.uniform(-0.8, +0.8), np.random.uniform(-0.8, +0.8)) # I think this will ensure the stimulus does not overlap, if dist overlaps placed, then reposition dist. 
        dist_list.append(dist) # places the stimuli into the distractor list
        
    
    for i in range(n_target): # number of targets, if target = 0 then nothing is created
        target = visual.ImageStim(win, image = 'stimuli/T.png',pos = (np.random.uniform(-0.8, +0.8), np.random.uniform(-0.8, +0.8)), size = (width, height))
        target_list.append(target) # places the stimuli (or keeps it blank)
        
    # Draw stimuli
    
    for dist in dist_list:
        dist.draw()
    
    for target in target_list:
        target.draw()
    
    win.flip()
    
    # Collect Responses
    
    respClock.reset() # resets RT clock
    keys = event.waitKeys(maxWait = 2.0, # time out after 2.0
        keyList=['t', 'escape'], # allowable keys
        timeStamped = respClock) # records time that key is pressed (used for RT)
    
    if keys is None: # Does not assign a key or RT when no key is pressed
        key, rt = None, np.nan
    else:
        key, rt = keys[0] # time stamps key press for reaction time
    
    if key == 'escape': # exits the experiment 
        win.close()
        core.quit()
    
    # Scoring
    if  n_target == 1 and key == 't':
        corr = 1
        feedback = "correct!"
    elif n_target == 0 and key == 't':
        corr = 0
        feedback = "incorrect!"
    elif n_target == 1 and key != 't':
        corr = 0
        feedback = "incorrect!"
    elif n_target == 0 and key != 't':
        corr = 1
        feedback = "correct!"
    else:
        corr = np.nan
        
    msg.text = feedback # prints the feedback 
    msg.draw()
    win.flip()
    core.wait(0.7) # duration of feedback presentation
    
    # Specifying what data to add to our data file
    trials.addData('corr', corr) 
    trials.addData('feedback', feedback)
    trials.addData('rt', rt)
    trials.addData('participant_id', participant_id)
    
    thisExp.nextEntry() # save per trial data, start next trial


# --- OVERALL NOTES: 

# I tried to use the forums, but a lot of posts are about builder not coder. Therefore, they were not all that helpful. I used the built in Demos more often.

# I was unable to accomplish printing to the screen acuracy and average RTs after the experiment is done as I ran out of time. 

# I sometimes have a hard time getting the dialogue box to not appear behind the screen, I'd love to know how to fix that!

# --- ADDITIONAL SOURCES:

# Dialogue boxes - https://www.psychopy.org/api/gui.html

# waitKeys - https://www.psychopy.org/api/event.html

# numpy documentation:
    # np.random.choice - https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html
    # np.random.uniform - https://numpy.org/doc/2.2/reference/random/generated/numpy.random.uniform.html 
        # NOTE: I was trying to use just random, but it would only take integers. 

# text stim - https://www.psychopy.org/api/visual/textstim.html

# overlapping stimuli - https://www.psychopy.org/api/visual/imagestim.html#psychopy.visual.ImageStim.overlaps 
    # returns True if stimuli overlaps another
    
# this workshop was really helpful in designing my loops and using trial handler - https://workshops.psychopy.org/3days/day3/codingAnExperiment.html
