from SignalManager import SignalManager
from graphics.Graphics import Graphics


class GameFunctionality:

    graphics: Graphics

    signalManager: SignalManager

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

    def setGraphics(self, graphics: Graphics):
        self.graphics = graphics

    def getSignalManager(self):
        return self.signalManager

    def setSignalManager(self, signalManager: SignalManager):
        self.signalManager = signalManager

    def setClaveTorneo(self, clave : str):
        self.claveTorneo = clave

