from cmu_112_graphics import *
from Chaser import *
from Features import *
import random

def distance(x0, y0, x1, y1):
    return (((x1-x0)**2) + ((y1-y0)**2))**0.5

#user image from https://jetpackjoyride.fandom.com/wiki/Barry_Steakfries

class Steve(object):
    def __init__(self, app):
        self.app = app
        self.x = self.app.width/2 - 75
        self.y = self.app.height/2
        #self.image from online
        self.power = ""
        self.image = self.app.loadImage('barry.png')
        self.scale = 0.15
        self.image = self.app.scaleImage(self.image, self.scale)
        self.sizeX, self.sizeY = self.image.size
        #self.power should change if it collides with powerUp

    def moveSideways(self):
        self.x += 5
        #moves sideways with scroll

    def moveUp(self):
        if self.y - 12 - (self.sizeY/2) < 70:
            self.y = 70
        else: self.y -= 12
        #when space is pressed in controller

    def drop(self):
        if self.y + 7 + (self.sizeY/2) > 335:
            self.y = 335
        else: self.y += 7

    def changePower(self, other):
        self.power = other.power

    def barrierCheck(self, barrier):

        checkSize = barrier.scale*20
        boundary = 38*barrier.scale
        
        if barrier.direction == 'l':
            checkX = barrier.x-(barrier.sizeX/2)-self.app.scrollX + boundary 
            checkY = barrier.y-(barrier.sizeY/2) + boundary
            while checkX<(barrier.x-self.app.scrollX+barrier.sizeX/2)-boundary and checkY<barrier.y+(barrier.sizeY/2)-boundary:
                if self.x >= checkX-checkSize and self.x <= checkX+checkSize:
                    if self.y >= checkY-checkSize and self.y <= checkY+checkSize:
                        print("why1")
                        return True
                checkX += 0.8
                checkY += 1

        elif barrier.direction == 'r':
            checkX = barrier.x+(barrier.sizeX/2)-self.app.scrollX - boundary 
            checkY = barrier.y-(barrier.sizeY/2) + boundary
            while checkX<(barrier.x-self.app.scrollX+barrier.sizeX/2)+15 and checkY<barrier.y+(barrier.sizeY/2)-boundary:
                if self.x >= checkX-checkSize and self.x <= checkX+checkSize:
                    if self.y >= checkY-checkSize and self.y <= checkY+checkSize:
                        return True
                checkX -= 0.8
                checkY += 1

        elif barrier.direction == 'h':
            checkX = barrier.x-(barrier.sizeX/2)-self.app.scrollX + boundary
            while checkX<(barrier.x-self.app.scrollX+barrier.sizeX/2)-boundary:
                if self.x >= checkX-checkSize and self.x <= checkX+checkSize:
                    if self.y >= barrier.y-checkSize and self.y <= barrier.y+checkSize:
                        return True
                checkX += 1

        elif barrier.direction == 'v':
            checkY = barrier.y-(barrier.sizeX/2) + boundary
            while checkY<(barrier.y + barrier.sizeY/2)-boundary:
                if self.x >= barrier.x-checkSize-self.app.scrollX and self.x <= barrier.x+checkSize-self.app.scrollX:
                    if self.y >= checkY-checkSize and self.y <= checkY+checkSize:
                        return True
                checkY += 1

        return False
                


    def collidesWith(self, other):
        if isinstance(other, Barrier) : #should calculate if they are colliding
            return self.barrierCheck(other)                
        if isinstance(other, Bullet): #should calculate if they are colliding
            if other.y >= self.y-(self.sizeY/2) and other.y <= self.y+(self.sizeY/2):
                if (other.x-self.app.scrollX) >= self.x-(self.sizeX/2) and (other.x-self.app.scrollX) <= self.x+(self.sizeX/2):
                    return True
            return False
        if isinstance(other, PowerUp):
            pass

        return False
        #if collides then the game will be over

    def render(self, canvas):
        canvas.create_image(
                self.x,
                self.y,
                image=ImageTk.PhotoImage(self.image))

        
    #create steve graphics here
    #change based on power