class GameFunctionality:

    def __init__(self):
        self.graphics: any

        self.signalManager: any

        self.continuarPartida: bool
        self.continuarTorneo: bool

        self.claveTorneo: str

        self.nombreDelJugador: str

        self.nombreTorneo: str

    def actualizarContinuarPartida(self, continuar: bool):
        self.continuarPartida = continuar

    def actualizarContinuarTorneo(self, continuar: bool):
        self.continuarTorneo = continuar

    def getGraphics(self):
        return self.graphics

    def setGraphics(self, graphics):
        self.graphics = graphics

    def getSignalManager(self):
        return self.signalManager

    def setSignalManager(self, signalManager):
        self.signalManager = signalManager

    def setClaveTorneo(self, clave: str):
        self.claveTorneo = clave

