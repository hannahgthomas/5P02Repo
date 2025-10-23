# Import packages

from psychopy import visual, core, event

# Create window

win = visual.Window([1920, 1080], fullscr = True, monitor = "legionMonitor", screen = 1, color = [1, 1, 1], units = "norm")

# Create Stimuli

# Make the fixation cross stim
fixation = visual.TextStim(win, text= '+', pos=(0, 0), color = 'black')

# Make the message stim
message = visual.TextStim(win, text= 'GO!', pos=(0, 0), color = 'green')

#Collect responses
respClock = core.Clock()

#Draw fixation
fixation.draw()
win.flip()
core.wait(1.0) # wait for 1s
respClock.reset() # reset response clock

win.flip()

message.draw() # show message

win.flip()

keys = event.waitKeys(keyList=['space']) # wait until 'space' to end event
resp = keys[0]
rt = respClock.getTime() # store rt of key press

# create stim to display rt

rt_print = visual.TextStim(win, text= '', pos=(0, 0), color = 'green')

if keys == 'space': # I could only get this to work once I included an if statement
    rt = rt 

rt_print.text = rt # Assign the rt

win.flip()
rt_print.draw() # Draw the rt

win.flip()
core.wait(5.0) # wait 5s



