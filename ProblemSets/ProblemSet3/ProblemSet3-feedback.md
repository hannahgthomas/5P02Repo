# PSYC 5P02- Introduction to Programming for Psychology
## Fall 2025

### Problem Set #3

### Rubric:
* Accuracy & Efficiency: 50%
* Explanation and documentation: 50%

--- 
###  Feedback:

* I noticed you (and a lot of other students) used this convention for turning variables into strings: `filename = f"VisualSearch_{info['participant']}"`. To me a much easier convention would be to simply concatenate: `filename = 'VisualSearch_" + str(info['participant'))`. Be sure to document if using a new method.  
* I'm glad to see you figured out the TrialHandler. My personal preference has always been to create conditions using code and then building out the trial list that way, but I suppose it makes sense to use the tools available to you.
* Your code for the practice and the trials is exactly the same. Perhaps this is because of the way you've implemented your loops with the `trialHandler`. But even still there are probably ways you could have used functions or methods to limit the redundancy. _Even_ if you had just put the majority of the code from inside the loop into a function you could have just called that function twice. But you could also use if statements perhaps to run different loops or different number of trials depending on whether it's the practice block or not
* The re-using of code is particularly problematic because you've hard-coded a number of things were you might have wanted to use some global variables instead. e.g., I think the code `np.random.uniform(-0.8, +0.8)` is repeated 12 times? The `0.8` value could have easily been a global variable that you define once. That way if you want to change it, the value changes consistently for both the practice and main experiment, and you don't have to find and replace 12 values!
* You also could easily combine your feedback statements into fewer statements using something like: `if  (n_target == 1 and key == 't') or (n_target == 1 and key != 't'):`
* I like the use of loops and a list to define all distractors. 
* The dialogue box might appear behind the screen because you're creating the screen first. I believe you also have your window projecting to screen 1, which if you have two monitors set up will be your secondary monitor, whereas the dialogue box would appear on the primary monitor. So if you only have one monitor the screen will cover the dialogue box. 
* **Overall:** Good work. Does the majority of what I asked for in a mostly efficient way (< 300 lines of code, even with the repeated practice and experiment code). Try to make use of functions of methods to improve efficiency, and try to avoid hard-coding values where possible.

**Accuracy & Efficiency:** 20/25
**Explanation and documentation:** 24/25
**Total:** 44/50
