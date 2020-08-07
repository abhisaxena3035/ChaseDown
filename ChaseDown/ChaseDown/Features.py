from cmu_112_graphics import *
import random

#barrier image from https://jetpackjoyride.fandom.com/wiki/Zapper

class Barrier(object):
    
    def __init__(self, app, x, y, direction, scale):
        self.app = app
        # self.x should be made so that the person can escape
        # self.y should be made so that the user can go higher
        #or lower to escape it
        self.x = x
        self.y = y
        self.direction = direction
        if self.direction == 'r': self.image = self.app.loadImage('rdiagonal.png')
        if self.direction == 'l': self.image = self.app.loadImage('ldiagonal.png')
        if self.direction == 'h': self.image = self.app.loadImage('horizontal.png')
        if self.direction == 'v': self.image = self.app.loadImage('vertical.png')
        self.scale = scale
        self.image = self.app.scaleImage(self.image, self.scale)
        self.sizeX, self.sizeY = self.image.size
        #print(str(sizeX) + " " + str(sizeY))

    def render(self, canvas):
        canvas.create_image(
                self.x-self.app.scrollX,
                self.y,
                image=ImageTk.PhotoImage(self.image))
        #should make a line that displays where the user
        #cannot go unless they die

class PowerUp(object):
    def __init__(self, app):
        self.app = app
        #self.x should be on the screen and can be hit by user
        #self.y should be on the screen and can be hit by user
        #should not be blocked by another feature
        self.power = random.choice(['speed', 'robot', 'extra life'])
        #will probably add more cooler power

    def render(self, canvas):
        pass
    #create power up object here or image

class Challenges(object):
    def __init__(self):
        self.challenge = random.choice(['get 2 power ups', 'get 200 coins'])
        self.isComplete = False

    def complete(self):
        self.isComplete = True
        pass
    #check in game mode if the challenge is complete