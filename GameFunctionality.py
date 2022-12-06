from SignalManager import SignalManager


class GameFunctionality:

    graphics: any

    signalManager: any

    continuarPartida: bool
    continuarTorneo: bool

    claveTorneo: str

    nombreDelJugador: str = None

    nombreTorneo: str = None


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

    def setClaveTorneo(self, clave : str):
        self.claveTorneo = clave

