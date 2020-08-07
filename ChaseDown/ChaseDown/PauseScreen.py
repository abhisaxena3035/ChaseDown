from cmu_112_graphics import *
import random

class PauseMode(Mode):
    def appStarted(self):
        self.challenges = [Challenge() for i in range(3)]

    def redrawAll(self, canvas):
        pass
        #need to draw button to return to gameplay
        #need to draw all of the challenges where they should me
            #maybe create a helper function
        #have check box if they are completed
        #need to have some kind of tracker for self.score
        #and self.coins