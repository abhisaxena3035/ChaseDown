from cmu_112_graphics import *
import random

class StartMode(Mode):
    def appStarted(self):
        pass

    def keyPressed(self, event):
        if event.key == 'Space':
            self.setActiveMode(name='game')
        #if space is pressed the game will start

    def playOnClick(self):
        self.setActiveMode(name='game')
        #start game if button is pressed

    def pauseOnClick(self):
        self.setActiveMode(name='pause')
        #will go to pause screen if pressed

    def redrawAll(self, canvas):
        pass
    #will create buttons here to move between start, pause, and play screen
