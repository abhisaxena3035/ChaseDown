class GameMode(Mode):
    def appStarted(self):
        self.keys = []
        self.timer = 0
        self.steve = Steve()
        self.powerUps = []
        self.barriers = []
        self.scrollX = 0
        self.scrollY = 0
        

    def keyPressed(self, event):
        self.keys.append(event.key)
        for elem in self.keys:
            if event.key == 'space':
                #increase height here
                self.steve.moveUp()

    def timerFired(self):
        self.timer += 1
        self.score += 1
        self.powerUps.append(PowerUp())
        self.barriers.append(Barrier())
        self.scrollX += 5
        self.steve.moveSideways()
        

    def redrawAll(self, canvas):
        for elem in self.powerUps:
            elem.render(canvas)

        for elem in self.barriers:
            elem.render(canvas)

        self.steve.render()

