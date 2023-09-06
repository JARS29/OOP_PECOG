from psychopy import visual, core, sound
import os

##### Creating an audio stimuli. The first audio is reproduced and afterwards a second audio is played.
path=os.path.abspath('')
sound1='\media\hello.wav'
sound2='\media\world.wav'
image1='media\hello.png'
image2='media\world.png'


win = visual.Window(size=[800,800],     #Creating a monitor object
                    color='white')

img1 = visual.ImageStim(win=win,        #Creating a image stimuli
                        image=os.path.join(path,image1),
                        units='pix',
                        size=(200,200))
message = visual.TextStim(win,
                          text='hello',
                          pos=(0,0.5),
                          color='black') #Creating a text stimuli

message.setAutoDraw(True)
img1.setAutoDraw(True)

aud1 = sound.Sound(value=path+sound1,   #Creating an audio stimuli
                   volume=1)

aud2 = sound.Sound(value=path+sound2,
                   volume=1)

aud1.play()                     #Playig the first audio
win.flip() 
core.wait(aud1.getDuration())   #Wait until the audio duration
aud2.play()                     #Playing the second audio
img1.setImage(os.path.join(path,image2))
message.setText('world')  # change properties of existing stim
win.flip()
core.wait(1.0)                  #Duration of the stimuli
aud2.stop()
win.close()                     # Close the windows
