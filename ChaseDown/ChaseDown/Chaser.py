from cmu_112_graphics import *
import random

#chaser image from https://www.iconfinder.com/icons/1475100/bad_bat_character_creature_evil_fantasy_gargoyle_icon
class Chaser(object):
    def __init__(self, app):
        self.app = app
        self.x = 30  #same as steve but always behind
        self.y = self.app.height/2
        self.image = self.app.loadImage('chaser.png')
        self.scale = 0.08
        self.image = self.app.scaleImage(self.image, self.scale)
        self.way = 'up'
        self.sizeX, self.sizeY = self.image.size
        self.bullets = []
        #self.image from online

    #def moveSideways(self):
        #self.x += 5
        #moves sideways with scrollX, but will move the same way as steve
        #will always be behind him

    def move(self):
        if self.way == 'up':
            if self.y - 8 - (self.sizeY/2) < 74:
                self.way = 'down'
                self.y = 74 + (self.sizeY/2)
            else:
                self.y -= 8
        else:
            if self.y + 8 + (self.sizeY/2) > 328:
                self.way = 'up'
                self.y = 328-(self.sizeY/2)
            else:
                self.y += 8
            

        #when steve increases in height the chaser should as well

    def shoot(self):
        #when called in play mode should shoot at Steve
        #will be another class for bullet
        self.bullets.append(Bullet(self.app, self.x, self.y))


    def render(self, canvas):
        canvas.create_image(
                self.x,
                self.y,
                image=ImageTk.PhotoImage(self.image))

        for elem in self.bullets:
            elem.render(canvas)
    #create Chaser graphics here

# laser image from https://flyclipart.com/download-png#image-229014.png
class Bullet(object):
    def __init__(self, app, iX, iY):
        self.app = app
        self.x = iX
        self.y = iY
        self.image = self.app.loadImage('laser.png')
        self.scale = 0.15
        self.image = self.app.scaleImage(self.image, self.scale)
        #this is the initial and final points
        #of the bullet
        #usually initial is where it is being shot fron
        # which is the chaser's position to the final
        #pos which is the user's position
        #if it doesn't hit it should go until it hits a wall

    def move(self):
        self.x += 40
    
    def render(self, canvas):
        #make bullet animate towards user
        canvas.create_image(
                self.x-self.app.scrollX,
                self.y,
                image=ImageTk.PhotoImage(self.image))

