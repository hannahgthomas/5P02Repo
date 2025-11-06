from psychopy import visual, event, core, data, gui
from psychopy.tools.filetools import fromFile
import random
import numpy as np

# If you set up the window specifications to be white, it would make the task more better. 

# Experiment setup
expName = 'VisualSearch'
dlg = gui.Dlg()
dlg.addText('Enter SubjectID:') # I added this, not able to see what was being entered. This might be due to me having an older version of Psychopy. 
dlg.addField('SubjectID:')
dlg.addText('Trials Per Condition')
dlg.addField('Trials Per Cond:')
ok_data = dlg.show()
if dlg.OK:  # or if ok_data is not None
    print(ok_data)
else:
    print('user cancelled') # I added this
#if not dlg.OK:
    #core.quit()

sub_ID = ok_data['SubjectID:'] # I'm not sure you were storing the dlg information anywhere, it is being stored in a dictionary but were indexing it like a list [0] and [1]. 
trials = int(dlg.data['Trials Per Cond:']) 
fileName = sub_ID + "_" + expName
dataFile = open(fileName + '.csv', 'w') # I'm sure there is something to improve on here 
dataFile.write('SetSize,TP, RT, Correct, Missed\n')

win = visual.Window([1920, 1080], fullscr=False, units='pix')

# Stimuli and conditions
conditions = [5, 8, 12]
stim_size = 30 #using pix will depend on the monitor size I believe
T = visual.ImageStim(win, 'Stimuli/T.png', size=stim_size)
L = visual.ImageStim(win, 'Stimuli/L.png', size=stim_size)

# Everything prints at once, feedback, RT, at the same time as the stimuli itself. 

# Draw stimuli at random positions/orientations
def pos_and_ori(target, distract, samp_size): # awesome that you defined this within a function
    samplelist = list(range(-180, 180, 25)) 
    x = random.sample(samplelist, samp_size) # where does samp_size come from?
    y = random.sample(samplelist, samp_size)
    for n in range(0, samp_size - 1): 
        orientations = [0, 90, 180, 270]
        orin = random.choice(orientations)
        distract.ori = orin
        distract.pos = (x[n], y[n])
        distract.draw()
    for n in range(samp_size - 1, samp_size):
        target.pos = (x[n], y[n])
        target.draw()
    return distract, target

# Determine if target is present on a given trial
def targ_pres(trial_list, total_trials, distract, target, condition_index):
    pres_or_not = random.choice(trial_list) # what is trial list? where is it used
    trial_list.remove(pres_or_not)
    if pres_or_not <= np.median(total_trials): # is this how you set target to appear 50% of the time? If an odd number is it does not technically work but good way. 
        targ_there = 0
        stimuli = pos_and_ori(distract, distract, condition) 
    else:
        targ_there = 1
        stimuli = pos_and_ori(target, distract, condition)
    return targ_there, stimuli

# Get response and RT
def KeyGet(trial_duration=2.0, rt=None, resp=None):
    startTime = core.getTime()
    while core.getTime() - startTime < trial_duration and resp is None:
        keys = event.getKeys(keyList=['a', 'd', 'escape'])
        if keys:
            key = keys[0]
            rt = core.getTime() - startTime
            if key == 'a':
                resp = 'a'
                break
            elif key == 'd':
                resp = 'd'
                break
            elif key == 'escape':
                core.quit()
        core.wait(0.01)
    if resp is None:
        resp = 'no_response'
        rt = 999 # Could just set rt to blank
    return resp, rt

# Evaluate response accuracy and feedback
def Response(resp, rt, targ_there):
    if resp == 'd' and targ_there == 1:
        corr = 1
        feedback = 'Correct!'
        response_time = round(rt, 2) # Good use of round
    elif resp == 'a' and targ_there == 1:
        corr = 0
        feedback = 'Incorrect!'
        response_time = round(rt, 2)
    elif resp == 'a' and targ_there == 0:
        corr = 1
        feedback = 'Correct!'
        response_time = round(rt, 2)
    elif resp == 'd' and targ_there == 0:
        corr = 0
        feedback = 'Incorrect'
        response_time = round(rt, 2)
    elif resp == 'no_response':
        corr = 0
        feedback = 'No Response'
        response_time = 'NA'
    return corr, feedback, response_time

# Instructions
welcome = ''''
Welcome to the Visual Search Task

You will see an assortment of shapes in different positions and orientations.
Most will be 'L' shapes, but some may contain a 'T' shape.

If the T is present, press 'd'.
If the T is absent, press 'a'.

Respond quickly!
Press SPACE to begin 5 practice trials.
'''

instructions = visual.TextStim(win, color='white', text=welcome, units='norm', height=0.05)
instructions.draw()
win.flip()
keys = event.waitKeys(keyList=['space'])
core.wait(0.25)

# Something is wrong here, I just need to figure out how to change it. 
# Practice trials

n_practice = 5

#practice_trials = range(1, 6) # You don't need to use range, you can use BLANK to just set the number to 5. 
for condition in conditions:
    appear = list(practice_trials)
    #for prac_trials in practice_trials:
    for prac_trials in range(n_practice):
        targ_there, stimuli = targ_pres(appear, practice_trials, L, T, condition) # somewhere in here, you need to draw your list of practice trials then win.flip. I'd also add a core.wait as well. 
        win.flip() # adding this, draws your trial itself first, then presents your feedback and RT after. 
        resp, rt = KeyGet()
        corr, feedback, response_time = Response(resp, rt, targ_there)
        cor_feedback = visual.TextStim(win, text=feedback, pos=(0, 30), height=40)
        back_rt = visual.TextStim(win, text=response_time, pos=(0, -30), height=40)
        cor_feedback.draw()
        back_rt.draw()
        win.flip()
        core.wait(0.5)

# Main experiment instructions
welcome = ''''
Practice complete! Now for the real trials.

Press SPACE to begin.
'''
instructions = visual.TextStim(win, color='white', text=welcome, units='pix', height=10)
instructions.draw()
win.flip()
keys = event.waitKeys(keyList=['space'])
core.wait(0.25)

# Trial setup
total_trials = range(1, trials + 1) # check this out, range takes the arguments (start, stop, and step) which you have specified as +1, which is the default you can leave blank. You could just do range(trials)
rt_list, corr_list, miss_rt_list = [], [], [] # making these empty?
random.shuffle(conditions)

# Main experiment loop
for condition in conditions:
    appear = list(total_trials)
    for trial in total_trials:
        targ_there, stimuli = targ_pres(appear, total_trials, L, T, condition) # again need to add win.flip() # Is stimuli used here?
        resp, rt = KeyGet()
        win.flip() # required here as well 
        corr, feedback, response_time = Response(resp, rt, targ_there)
        cor_feedback = visual.TextStim(win, text=feedback, pos=(0, 30), height=40)
        back_rt = visual.TextStim(win, text=response_time, pos=(0, -30), height=40)
        cor_feedback.draw()
        back_rt.draw()
        win.flip()
        core.wait(0.5)

        if rt != 999: # this is smart way to use your rt label, forget what I said
            rt_list.append(rt)
            miss_rt = 0
            corr_list.append(corr)
        else:
            miss_rt_list.append(1)
            miss_rt = 1
            corr_list.append(0)

        dataFile.write('%i, %i, %.3f, %i, %i\n' % (condition, targ_there, rt, corr, miss_rt))

dataFile.close()

# NOTE: How does the experiment decide if the target is there 50% of the time?

# Final feedback
average_rt = round(np.mean(rt_list), 2)
average_corr = round(np.mean(corr_list), 2)
total_miss = sum(miss_rt_list)

avg_rt_text = f'average rt: {average_rt}'
avg_corr_text = f'average correct: {average_corr}'
miss_text = f'no response on {total_miss} trials'
leave_text = 'press SPACE to exit'

cor_avg_back = visual.TextStim(win, text=avg_corr_text, pos=(0, 50), height=20)
rt_avg_back = visual.TextStim(win, text=avg_rt_text, pos=(0, -10), height=20)
miss_tot_back = visual.TextStim(win, text=miss_text, pos=(0, -35), height=20)
exit_text = visual.TextStim(win, text=leave_text, pos=(0, -100), height=20)

cor_avg_back.draw()
rt_avg_back.draw()
miss_tot_back.draw()
exit_text.draw()

win.flip()
keys = event.waitKeys(keyList=['space'])
win.close()
core.quit()

# Good job adding the feedback and RT. 

# The set size, condition does not randomize per trial, it runs in more of sequential/random for set size, but they appear in multiples of 3. 

# No escape function? 
