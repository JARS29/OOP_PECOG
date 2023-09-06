from psychopy import visual, core

##### Creating a first text stimuli. The first text appears by two seconds, then a second text is showed by two seconds too.

mylist= ['Hello', 'World']
win = visual.Window([400,400], color = 'black') #Creatin a monitor object

message = visual.TextStim(win, color = 'white') #Creating a text stimuli

message.setAutoDraw(True)  # automatically draw every frame

for i in mylist:
    message.setText(i)  # change properties of existing stim
    win.flip()      #Function for doing the changes.
    core.wait(2.0)  #time for the first

win.close() # Close the windows
