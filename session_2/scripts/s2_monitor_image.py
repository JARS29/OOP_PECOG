from psychopy import visual, core
import os

##### Creating an image stimuli. The first image appears by two seconds, then a second one is showed by two seconds too.
path=os.path.abspath('')
image1='media\hello.png'
image2='media\world.png'

win = visual.Window(size=[400,400],     #Creating a monitor object
                    color='white')

img1 = visual.ImageStim(win=win,        #Creating a image stimuli
                        image=os.path.join(path,image1),
                        units='pix',
                        size=(200,200))

img1.setAutoDraw(True)      # automatically draw every frame

win.flip()                  #Function for doing a frame change.

core.wait(2.0)              #time for the first stimuli.

img1.setImage(os.path.join(path,image2))  #change properties of the existing stimuli object

win.flip()

core.wait(2.0)

win.close() # Close the windows


######
