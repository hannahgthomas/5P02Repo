# Posner Cueing Tasks

from psychopy import visual, event, core, data # necessary libraries
win = visual.Window([2880, 1800], fullscr=True, units='pix') # create a window

import random

# insert here - make a text file to save data

respClock = core.Clock()

#initialise some stimuli
# create (but don't draw a stimulus)
fixation = visual.Circle(win, size = 5,
    lineColor = 'white', fillColor = 'lightGrey')
# create a second stimulus
probe = visual.GratingStim(win, size = 80, # 'size' is 3xSD for gauss,
    pos = [300, 0], # we'll change this later
    tex = None, mask = 'gauss',
    color = 'green')
# create a third stimulus
cue = visual.ShapeStim(win,
    vertices = [[-30, -20], [-30, 20], [30, 0]],
    lineColor = 'red', fillColor = 'salmon')
# define some attributes for the stimuli 
info = {} # a dictionary
info['fixTime'] = 0.5 # seconds
info['cueTime'] = 0.2
info['probeTime'] = 0.2
# create a single trial

# run multiple trials

side = [1,2]
orient = [1,2]

for trial in range(5):
    
    random.shuffle(side)
    random.shuffle(orient)
    fixation.draw()
    win.flip()
    core.wait(info['fixTime'])
    
    if orient[0] == 1:
        cue.ori = 0
    else: 
        cue.ori = 180

    cue.draw() # cue.ori = 180
    win.flip()
    core.wait(info['cueTime'])
    
    if side[0] == 1:
        probe.pos = [300, 0]
    else:
        probe.pos = [-300, 0]

    fixation.draw() # would need to be fixation.pos(-300, 0) 
    probe.draw()
    win.flip()
    respClock.reset()
    
    #clear screen
    win.flip()
    #wait for response
    keys = event.waitKeys(keyList = ['left', 'right', 'escape'])
    resp = keys[0] # take first response
    rt = respClock.getTime()
    
    #calculate accuracy
    if (resp == 'left' and side[0] == 2) or (resp == 'right' and side[0] == 1):
        corr = 1
    else:
        corr = 0
        
# writing files
dataFile.write(INSERT HERE)

dataFile.close()

















