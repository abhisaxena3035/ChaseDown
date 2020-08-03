class ChaseDownApp(ModalApp):
    def appStarted(self):
        self.addMode(GameMode(name='game'))
        self.addMode(PauseMode(name='pause'))
        self.addMode(StartMode(name='start'))
        self.setActiveMode('start')
        self.score = 0

    def getState(self):
        pass

