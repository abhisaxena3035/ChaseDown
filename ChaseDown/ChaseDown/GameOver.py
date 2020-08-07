from cmu_112_graphics import *
import random

class GameOverMode(Mode):
    def appStarted(self):
        pass

    def keyPressed(self, event):
        if event.key == 'r':
            self.setActiveMode('game')

    def startClick(self):
        self.setActiveMode('start')
        #if the user wants to play again

    def redrawAll(self, canvas):
        canvas.create_text(self.width/2, self.height/2, text="Game Over! Press 'R' to restart!")
        #draw score and name of app
        #draw the coins collected
        #draw the challenges that have been acheived
        #draw the button to return to the start screen
        #use self.startClick on the button