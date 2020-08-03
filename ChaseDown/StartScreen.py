class StartMode(Mode):
    def appStarted(self):
        pass

    def keyPressed(self, event):
        if event.key == 'Space':
            self.setActiveMode(name='game')

    def playOnClick(self):
        self.setActiveMode(name='game')

    def pauseOnClick(self):
        self.setActiveMode(name='pause')

    def redrawAll(self, canvas):
        pass
