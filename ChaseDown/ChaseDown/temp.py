def barrierCheck(self, barrier, x, y):
    if barrier.direction == 'h':
        checkX = barrier.y-(barrier.sizeX/2)
        for i in range(barrier.sizeX):
            checkX += 1
            if x == checkX and y == barrier.y:
                return True
        return False
    elif barrier.direction == 'v':
        checkY = barrier.y-(barrier.sizeY/2)
        for i in range(barrier.sizeY):
            checkY += 1
            if x == barrier.x and y == checkY:
                return True
        return False
    elif barrier.direction == 'r':
        checkX = barrier.x-(barrier.sizeX/2)
        checkY = barrier.y-(barrier.sizeY/2)
        while checkX < barrier.x+(barrier.sizeX/2) and checkY < barrier.y+(barrier.sizeY/2):
            if x == checkX and y == checkY:
                return True
            checkX += 1
            checkY += 0.8
    else:
        checkX = barrier.x+(barrier.sizeX/2)
        checkY = barrier.y-(barrier.sizeY/2)
        while checkX < barrier.x+(barrier.sizeX/2) and checkY < barrier.y+(barrier.sizeY/2):
            if x == checkX and y == checkY:
                return True
            checkX -= 1
            checkY += 0.8
                


    def collidesWith(other, x, y):
        if isinstance(other, Barrier) : #should calculate if they are colliding
            return barrierCheck(other, x, y)                
        if isinstance(other, Bullet): #should calculate if they are colliding
            if other.y >= y-(self.sizeY/2) and other.y <= y+(self.sizeY/2):
                if other.x >= x-(self.sizeX/2) and other.x <= x+(self.sizeX/2):
                    return True
            return False