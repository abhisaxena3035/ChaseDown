from cmu_112_graphics import *
from GameScreen import *
from StartScreen import *
from User import *
from Chaser import *
from Features import *
from GameOver import *
from PauseScreen import *
import random

class ChaseDownApp(ModalApp):
    def appStarted(self):
        self.addMode(GameMode(name='game'))
        self.addMode(PauseMode(name='pause'))
        self.addMode(StartMode(name='start'))
        self.addMode(GameOverMode(name='game over'))
        self.setActiveMode('game')
        self.score = 0
        self.coins = 0
        #stores access to score and coins so that 
        #all modes can use itcheckX = barrier.x+(barrier.sizeX/2)-self.app.scrollX + 15



    def getState(self):
        pass
    #used to test if necessary
if __name__ == "__main__":
    ChaseDownApp(width=546, height=406)
