from psychopy import visual, core, sound
import os

##### Creating an audio stimuli. The first audio is reproduced and afterwards a second audio is played.
path=os.path.abspath('')
sound1='media/hello.wav'
sound2='media/world.wav'

win = visual.Window(size=[400,400],     #Creating a monitor object
                    color='white')

aud1 = sound.Sound(value=os.path.join(path,sound1),   #Creating an audio stimuli
                   volume=1)
aud2 = sound.Sound(value=os.path.join(path,sound2),
                   volume=1)

aud1.play()                     #Playig the first audio
core.wait(aud1.getDuration())   #Wait until the audio duration
win.flip()                      #Function for doing the changes
aud2.play()                     #Playing the second audio
core.wait(2.0)                  #Duration of the stimuli
win.flip()
win.close()                     # Close the windows


######
