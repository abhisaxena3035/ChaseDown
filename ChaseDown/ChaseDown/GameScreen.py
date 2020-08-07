from cmu_112_graphics import *
import random
from User import *
from Chaser import *
from Features import *
import copy, math

def distance(x0, y0, x1, y1):
    return ((abs(x1-x0)**2) + (abs(y1-y0)**2))**0.5

# background image from http://cdn30.us1.fansshare.com/image/jetpackjoyride/jetpack-joyride-laser-jetpack-jetpack-joyride-1577465235.jpg
class GameMode(Mode):
    def appStarted(self):
        self.keys = []
        self.timer = 0
        self.steve = Steve(self)
        self.chaser = Chaser(self)
        self.powerUps = []
        self.barriers = []
        self.scrollX = 0
        self.background = self.loadImage('backdrop.png') #background image
        scale = 0.6
        self.background = self.scaleImage(self.background, scale)
        self.sizeX, self.sizeY = self.background.size
        self.backX = self.width/2 
        self.backgrounds = []
        self.moving = False
        self.score = 0
        self.bulletTimer = 0
        self.gameSpeed = 5

    def modeActivated(self):
        self.appStarted()
        

    def keyPressed(self, event):
        self.keys.append(event.key)
        for elem in self.keys:
            if event.key == 'Space':
                #increase height here
                self.steve.moveUp()
                self.moving = True

    def keyReleased(self, event) -> None:
        """when a key is released, it should be removed from the set
        that is being iterated through in keyPressed()"""
        if event.key in self.keys:
            self.keys.remove(event.key)
    
    def barrierCheck(self, barrier, x, y):
        checkSize = barrier.scale*20
        boundary = 38*barrier.scale
        
        if barrier.direction == 'l':
            checkX = barrier.x-(barrier.sizeX/2)-self.scrollX + boundary 
            checkY = barrier.y-(barrier.sizeY/2) + boundary
            while checkX<(barrier.x-self.scrollX+barrier.sizeX/2)-boundary and checkY<barrier.y+(barrier.sizeY/2)-boundary:
                if x >= checkX-checkSize and x <= checkX+checkSize:
                    if y >= checkY-checkSize and y <= checkY+checkSize:
                        print("why1")
                        return True
                checkX += 0.8
                checkY += 1

        elif barrier.direction == 'r':
            checkX = barrier.x+(barrier.sizeX/2)-self.scrollX - boundary 
            checkY = barrier.y-(barrier.sizeY/2) + boundary
            while checkX<(barrier.x-self.scrollX+barrier.sizeX/2)+15 and checkY<barrier.y+(barrier.sizeY/2)-boundary:
                if x >= checkX-checkSize and x <= checkX+checkSize:
                    if y >= checkY-checkSize and y <= checkY+checkSize:
                        print("why2")
                        return True
                checkX -= 0.8
                checkY += 1

        elif barrier.direction == 'h':
            checkX = barrier.x-(barrier.sizeX/2)-self.scrollX + boundary
            while checkX<(barrier.x-self.scrollX+barrier.sizeX/2)-boundary:
                if x >= checkX-checkSize and x <= checkX+checkSize:
                    if y >= barrier.y-checkSize and y <= barrier.y+checkSize:
                        print("why3")
                        return True
                checkX += 1

        elif barrier.direction == 'v':
            checkY = barrier.y-(barrier.sizeX/2) + boundary
            while checkY<(barrier.y + barrier.sizeY/2)-boundary:
                if x >= barrier.x-checkSize-self.scrollX and x <= barrier.x+checkSize-self.scrollX:
                    if y >= checkY-checkSize and y <= checkY+checkSize:
                        print("why4")
                        return True
                checkY += 1

        return False
        
    def collidesWith(self, other, x, y):
        if isinstance(other, Barrier) : #should calculate if they are colliding
            return self.barrierCheck(other, x, y)                
        if isinstance(other, Bullet): #should calculate if they are colliding
            if other.y >= y-(self.sizeY/2) and other.y <= y+(self.sizeY/2):
                if (other.x-self.scrollX) >= x-(self.sizeX/2) and (other.x-self.scrollX) <= x+(self.sizeX/2):
                    return True
        return True

    def isValid(self, barriers, x, y):
        #return True
        #x, y
        for elem in barriers:
            if self.collidesWith(elem, x, y):
                return False
        for elem in self.chaser.bullets:
            if self.collidesWith(elem, x, y):
                return False
        return True
                
    def addBarriers(self, barriers):
        check = False
        cushion = 5
        while not check:
            check = True
            currY = random.randint(74,328)
            currDirection = random.choice(['r','l','h','v'])
            currScale = (random.randint(2,7))/10
            currX = (546 + self.scrollX) + (360*currScale) + cushion
            
            if len(barriers) > 0:
                prevBarr = barriers[len(barriers)-1]
                if prevBarr.direction != 'h':
                    if distance(currX, currY, prevBarr.x, prevBarr.y) < (prevBarr.sizeY)+(currScale*450):
                        check = False
                else:
                    if distance(currX, currY, prevBarr.x, prevBarr.y) < (prevBarr.sizeX)+(currScale*450):
                        check = False
            cushion += 5
            if check:
                print(currX, currY)
                return Barrier(self, currX, currY, currDirection, currScale)

    def checkMoves(self, barriers, x, y, count=1):
        #if player able to get to the right end of screen return true or problem state
        #else
        #get possible moves up/down
        # is valid would check if is not colliding: 
        #recursive call of next move x, y
        # return problemState
        #if (len(self.barriers)>0) and (x-self.scrollX >= self.barriers[len(self.barriers)-1].x+self.barriers[len(self.barriers)-1].sizeX):
        if len(barriers) > 0 and x > 546: #x > barriers[len(barriers)-1].x - self.scrollX:
            print("here")
            return barriers
        for move in [12,-7]:
            if self.isValid(barriers, x+5, y+move):
                if count > 0:
                    barriers.append(self.addBarriers(barriers))
                solution = self.checkMoves(barriers, x+5, y+move, count-1)
                if solution != None:
                    return solution
                barriers.pop()
        return None


    def checkBullets(self):
        for bullet in self.chaser.bullets:
            if bullet.x-self.scrollX > 580:
                self.chaser.bullets.remove(bullet)
            else:
                bullet.move()
    
    def timerFired(self):
        #will have to adjust based on seconds and time 
        #into the game
        self.timer += 1
        self.bulletTimer += 1
        for elem in self.chaser.bullets:
            if self.steve.collidesWith(elem):
                self.setActiveMode('game over')
                print("collided")
        for elem in self.barriers:
            if (elem.x + elem.sizeX) - self.scrollX < 0:
                self.barriers.remove(elem)
            if self.steve.collidesWith(elem):
                self.setActiveMode('game over')
                print("collided")
        if self.timer % 30 == 0:
            tempBarriers = copy.copy(self.barriers) 
            tempBarriers = self.checkMoves(tempBarriers, self.steve.x, self.steve.y)
            if tempBarriers != None:
                self.barriers = tempBarriers
        self.checkBullets()
        if self.bulletTimer % ((random.randint(7,11))*10) == 0 and self.bulletTimer != 0:
            self.chaser.shoot()
            self.bulletTimer = 0
            self.checkBullets()
        """if self.timer%100 == 0:
            self.gameSpeed += 1"""
        self.scrollX += 5
        self.backX += 5
        self.chaser.move()
        self.score += 1
        if self.keys == []: self.moving = False
        if not self.moving: self.steve.drop()
        
        
        

    def redrawAll(self, canvas):
        """for elem in self.powerUps:
            elem.render(canvas)"""

        canvas.create_image(
            self.width/2,
            self.height/2,
            image=ImageTk.PhotoImage(self.background))

        canvas.create_text(30,10,text="Score: " + str(self.score), fill='white')

        for elem in self.barriers:
            elem.render(canvas)
        
        for elem in self.powerUps:
            elem.render(canvas)

        self.steve.render(canvas)

        self.chaser.render(canvas)

        #renders all elements of the screen

