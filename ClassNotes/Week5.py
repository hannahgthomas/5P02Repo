# Week 5 - Psychopy Coder

# No fancy details in coder view

# Starting out - monitor set-up - the thing we draw our window to

# Using Psychopy outside of Psychopy

# $pip install python 

# Really simple experiment

from psychopy import visual, core # need to import the Psychopy library, also specific modules from psychopy 
win = visual.Window([400,400]) # Must create a window to draw to, assign a name, must include window size, can include other options
message = visual.TextStim(win, text = 'hello') # draw a stimulus to the back buffer, assign a label, specify type, assign to window and properties
message.autoDraw = True # Automatically draw every frame 
win.flip() # flip the stimulus to the screen - stimulus does not appear until buffer is "flipped" - time at which event happens
core.wait(2.0) # delay the next events from happening 
message.text = 'world' # Change properties of existing stim # change the .text property
win.flip() - flip it again 
core.wait(2.0) - wait

# We will almost always import visual, event, data, and core modules







