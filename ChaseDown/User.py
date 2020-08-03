class Steve(object):
    def __init__(self, app):
        self.app = app
        self.x = self.app.width/2
        self.y = self.app.height/2
        #self.image from online

    def moveSideways(self):
        self.x += 5
        #moves sideways with scroll

    def moveUp(self):
        self.y += 5
        #when space is pressed in controller

    def render(self, canvas):
        pass
    #create steve graphics here