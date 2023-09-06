from psychopy import visual, core

##### Creating a first text stimuli. The first text appears by two seconds, then a second text is showed by two seconds too.


win = visual.Window(size=[400,400],
                    color='black') #Creatin a monitor object

message = visual.TextStim(win=win,
                          text='hello') #Creating a text stimuli

message.setAutoDraw(True)  # automatically draw every frame

win.flip()      #Function for doing the changes.

core.wait(2.0)  #time for the first

message.setText('world')  # change properties of existing stim

win.flip()

core.wait(2.0)

win.close() # Close the windows


######